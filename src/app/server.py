from api import router
from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware
import logging


def init_routers(app_: FastAPI) -> None:    
    app_.include_router(router)


def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
            expose_headers=["*"]
        )
    ]
    return middleware

def create_app() -> FastAPI:
    app_ = FastAPI(
        title="PB case",
        description="API to suport the Linear Regression Model requests",
        version="1.0.0",
        docs_url= "/docs",                
        middleware=make_middleware(),
    )    
    init_routers(app_=app_)
    return app_

logging.basicConfig(filename='api_log.log', filemode='a', level=logging.INFO)
app = create_app()