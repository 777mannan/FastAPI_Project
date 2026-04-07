from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator 
from app.api import routes_auth,routes_predcit
from app.middleware.login_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers

app = FastAPI(title='Car Price Prediction API')

app.add_middleware(LoggingMiddleware)

app.include_router(routes_auth,tags=['Auth'])

app.include_router(routes_predcit,tags=['Prrediction'])

Instrumentator().instrument(app).expose(app)

register_exception_handlers(app)