from celery import Celery

# from src.worker import test_celery

celery_app = Celery("worker",
                    backend="redis://localhost:6379/3",
                    broker="redis://localhost:6379/2",
                    include=['src.worker'])

# celery_app.conf.task_routes = {"src.worker.test_celery": "test-queue"}

celery_app.conf.update(task_track_started=True)
