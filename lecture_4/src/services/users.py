import jwt
import uuid

from datetime import datetime
from functools import lru_cache
from fastapi import Depends
from passlib.hash import pbkdf2_sha256
from redis import Redis
from sqlmodel import Session


from src.db import AbstractCache, get_cache, get_session
from src.db.redis_storage import (
    get_active_refresh_token,
    get_blocked_access_token
    )
from src.models.user import User
from src.services import ServiceMixin
from src.api.v1.schemas.auth import Login, Signup, Tokens
from src.core.config import (
    JWT_ACCESS_EXP_SECONDS,
    JWT_REFRESH_EXP_SECONDS,
    JWT_SECRET_KEY,
    JWT_ALGORITHM
    )


class UserServis(ServiceMixin):
    def __init__(
        self,
        cache: AbstractCache,
        session: Session,
        blocked_access_tokens: Redis,
        active_refresh_tokens: Redis,
            ):
        self.cache: AbstractCache = cache
        self.session: Session = session
        self.blocked_access_tokens = blocked_access_tokens
        self.active_refresh_tokens = active_refresh_tokens

    def create_jwt(self, user):
        now = datetime.utcnow().timestamp()
        access_jwt = jwt.encode(
            {
                "username": user.username,
                "iat": now,
                "nbf": now,
                "exp": now + JWT_ACCESS_EXP_SECONDS,
                "jti": str(uuid.uuid4()),
                "sub": user.id,
            },
            JWT_SECRET_KEY,
            algorithm=JWT_ALGORITHM
        )
        refresh_token_id = str(uuid.uuid4())
        refresh_jwt = jwt.encode(
            {
                "iat": now,
                "nbf": now,
                "exp": now + JWT_REFRESH_EXP_SECONDS,
                "jti": refresh_token_id,
                "sub": user.id,
            },
            JWT_SECRET_KEY,
            algorithm=JWT_ALGORITHM
        )
        self.active_refresh_tokens.rpush(str(user.id), refresh_token_id)
        return Tokens(
            access_token=access_jwt,
            refresh_token=refresh_jwt,
        )

    def create_user(self, user: Signup):
        """Создать пользователя."""
        new_user = User(
            username=user.username,
            email=user.email,
            password_hash=pbkdf2_sha256.hash(user.password)
        )
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user

    def login_user(self, login_data: Login):
        user = self.session.query(User).filter(
            User.username == login_data.username
        ).first()
        if not user:
            raise ValueError
        if not pbkdf2_sha256.verify(login_data.password, user.password_hash):
            raise ValueError
        return self.create_jwt(user)

    def refresh_token(self, refresh_jwt):
        decode_token = jwt.decode(
            refresh_jwt,
            JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM]
        )
        user_id = decode_token.get('sub')
        token_id = decode_token.get('jti')
        active_tokens = self.active_refresh_tokens.lrange(str(user_id), 0, -1)
        if token_id in active_tokens:
            self.active_refresh_tokens.lrem(str(user_id), 0, token_id)
            user = self.session.query(User).filter(
                User.id == user_id
            ).first()
            return self.create_jwt(user=user)
        else:
            raise ValueError


@lru_cache()
def get_user_service(
    cache: AbstractCache = Depends(get_cache),
    session: Session = Depends(get_session),
    blocked_access_tokens: Redis = Depends(get_blocked_access_token),
    active_refresh_tokens: Redis = Depends(get_active_refresh_token),
) -> UserServis:
    return UserServis(
        cache=cache,
        session=session,
        blocked_access_tokens=blocked_access_tokens,
        active_refresh_tokens=active_refresh_tokens,
    )