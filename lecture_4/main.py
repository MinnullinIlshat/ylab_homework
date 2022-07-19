import redis
import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from src.schemas import AuthDetails
from src.auth import AuthHandler

from src.api.v1.resources import posts
from src.core import config
from src.db import cache, redis_cache

app = FastAPI(
    # Конфигурируем название проекта. Оно будет отображаться в документации
    title=config.PROJECT_NAME,
    version=config.VERSION,
    # Адрес документации в красивом интерфейсе
    docs_url="/api/openapi",
    redoc_url="/api/redoc",
    # Адрес документации в формате OpenAPI
    openapi_url="/api/openapi.json",
)


@app.get("/")
def root():
    return {"service": config.PROJECT_NAME, "version": config.VERSION}


@app.on_event("startup")
def startup():
    """Подключаемся к базам при старте сервера"""
    cache.cache = redis_cache.CacheRedis(
        cache_instance=redis.Redis(
            host=config.REDIS_HOST, port=config.REDIS_PORT, max_connections=10
        )
    )


@app.on_event("shutdown")
def shutdown():
    """Отключаемся от баз при выключении сервера"""
    cache.cache.close()


# Подключаем роутеры к серверу
app.include_router(router=posts.router, prefix="/api/v1/posts")

auth_handler = AuthHandler()
users = []

@app.post('/register', status_code=201)
def register(auth_details: AuthDetails):
    if any(x['username'] == auth_details.username for x in users):
        raise HTTPException(status_code=400, detail='Username is taken')
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    users.append({
        'username': auth_details.username,
        'password': hashed_password,
    })
    return 

@app.post('/login')
def login(auth_details: AuthDetails):
    user = None 
    for x in users:
        if x['username'] == auth_details.username:
            user = x 
            break 

    if (user is None) or (not auth_handler.verify_password(auth_details.password, user['password'])):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    token = auth_handler.encode_token(user['username'])
    return { 'token': token }

@app.get('/unprotected')
def unprotected():
    return { 'hello': 'world' }


@app.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return { 'name': username}



if __name__ == "__main__":
    # Приложение может запускаться командой
    # `uvicorn main:app --host 0.0.0.0 --port 8000`
    # но чтобы не терять возможность использовать дебагер,
    # запустим uvicorn сервер через python
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
    )
