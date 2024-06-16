from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from api import user, test

app = FastAPI()

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
    allow_methods=["GET"],
    allow_headers=["*"]
)

app.include_router(user.router, prefix="/api")
app.include_router(test.router, prefix="/api")


app.mount("/", StaticFiles(directory="dist", html=True), name="dist")