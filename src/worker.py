
from time import sleep

from celery import current_task

from src.celery_app import celery_app


@celery_app.task(acks_late=True, queue="test-queue")
def test_celery(word: str) -> str:
    print("Task started")
    for i in range(1, 11):
        sleep(1)
        current_task.update_state(state='PROGRESS',
                                  meta={'process_percent': i*10})
    return {
        "message": word
    }


@celery_app.task(acks_late=True, queue="test-queue")
def scheduled_task() -> str:
    print("Task started")
    for i in range(1, 11):
        sleep(1)
        current_task.update_state(state='PROGRESS',
                                  meta={'process_percent': i*10})
    return {
        "message": "Hello world!!!"
    }
