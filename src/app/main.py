import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi import status
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

from database.db import Base, engine

from routers import admin, blog

Base.metadata.create_all(bind=engine)

origins = ["localhost:8080"]

app = FastAPI()

app.include_router(admin.router)
app.include_router(blog.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", status_code=status.HTTP_200_OK, tags=["API Check"])
def check():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run(app)
