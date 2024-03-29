import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi import status
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

from database.db import Base, engine
from database.models.measurement_images import MeasurementImage  # noqa: F401

from routers import (
    admin,
    blog,
    measurement,
    material,
    category,
    sub_category,
    product,
    carousel_item,
    collection,
    instagram,
)

Base.metadata.create_all(bind=engine)

origins = ["http://localhost:8080", "https://fashion-o-phile.netlify.app"]

app = FastAPI()

app.include_router(admin.router)
app.include_router(blog.router)
app.include_router(measurement.router)
app.include_router(material.router)
app.include_router(category.router)
app.include_router(sub_category.router)
app.include_router(product.router)
app.include_router(carousel_item.router)
app.include_router(collection.router)
app.include_router(instagram.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origin_regex="^https://deploy-preview-[0-9]+--client-boutique.netlify.app$",  # noqa: E501
)


@app.get("/", status_code=status.HTTP_200_OK, tags=["API Check"])
def check():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run(app)
