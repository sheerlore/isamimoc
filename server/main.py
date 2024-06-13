from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import root, user

app = FastAPI()

# MIDDLEWARE: CORS
origins = [
    "http://localhost",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"]
)

app.include_router(root.router)
app.include_router(user.router)