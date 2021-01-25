# FastAPI + Celery with result backend example

Run example step by step:
1. Run redis with docker-compose:
```sh
docker-compose up -d
```

2. Run application:
```sh
./run_app.sh
```

3. Run celery worker:
```sh
./run_celery.sh
```

4. Open API doc: [http://127.0.0.1:8000](http://127.0.0.1:8000)
5. Open Flower: [http://127.0.0.1:5555/flower](http://127.0.0.1:5555/flower)
