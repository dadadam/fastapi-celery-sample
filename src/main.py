from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.worker import test_celery


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/{word}")
async def root(word: str):
    task = test_celery.delay(word)

    # Wait until task is ready, and return its result.
    # more by link: https://docs.celeryproject.org/en/stable/reference/celery.result.html
    print(task.get())

    return {"message": "Word received"}
