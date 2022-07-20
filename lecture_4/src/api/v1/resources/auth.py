from fastapi import APIRouter, Depends, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.services.users import UserServis, get_user_service
from src.api.v1.schemas.users import UserModel
from src.api.v1.schemas.auth import Login, Signup, Tokens


router = APIRouter()
security = HTTPBearer()


@router.post(
    path="/signup",
    response_model=UserModel,
    summary="Регистрация пользователя",
    tags=["auth"],
)
def signup(
    signup_data: Signup,
    user_service: UserServis = Depends(get_user_service)
        ) -> UserModel:
    user = user_service.create_user(user=signup_data)
    return user


@router.post(
    path="/login",
    response_model=Tokens,
    summary="Авторизация пользователя",
    tags=["auth"])
def login(
    login_data: Login,
    user_service: UserServis = Depends(get_user_service)
        ) -> UserModel:
    tokens = user_service.login_user(login_data=login_data)
    return tokens


@router.post(
    path="/refresh",
    response_model=Tokens,
    summary="Обновление токена",
    tags=["auth"],
)
def refresh(
    credentials: HTTPAuthorizationCredentials = Security(security),
    user_service: UserServis = Depends(get_user_service)
        ):
    expired_token = credentials.credentials
    tokens = user_service.refresh_token(expired_token)
    return tokens
