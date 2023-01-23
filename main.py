from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional

#Database
from config.database import Session, engine, Base
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder

#Middlewares
from middlewares.error_handler import ErrorHandler
#Router
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
app.title = 'Mi primera aplicacion con FastAPi'
app.version = '0.0.1'

#Manejo de errores en general
app.add_middleware(ErrorHandler)
#Router
app.include_router(movie_router)
app.include_router(user_router)
#Motor
Base.metadata.create_all(bind=engine)


#Endpoint
@app.get('/', tags = ['Home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')


