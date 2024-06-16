from fastapi import FastAPI, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from auth import validate_iap_jwt
from api import user, test

app = FastAPI(
    # すべてのエンドポイントでIAPから渡されるJWTトークンを必須化する
    dependencies=[Depends(validate_iap_jwt)]
)

# MIDDLEWARE: CORS
origins = [
    # "http://localhost",
    # "http://localhost:5173"
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"]
)

app.include_router(user.router, prefix="/api")
app.include_router(test.router, prefix="/api")

app.mount("/", StaticFiles(directory="dist", html=True), name="dist")