from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
import os

from routes.auth_route import auth_routes

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes, prefix="/api/auth")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=os.getenv(
        "PORT", default=5000), log_level="info")
