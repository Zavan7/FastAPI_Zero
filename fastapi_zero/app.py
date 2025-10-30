from http import HTTPStatus

from fastapi import FastAPI

from fastapi_zero.schemas import Message
from fastapi_zero.schemas import UserSchemas

app = FastAPI()


@app.get(
        '/',
        status_code=HTTPStatus.OK,
        response_model=Message
    )
def read_root():
    return {'message': 'Olá Mundo!'}

@app.post('/users/')
def create_user(user: UserSchemas):
    return user