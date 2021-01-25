#!/bin/sh

celery -A src.celery_app worker -l info -Q test-queue -c 1 -E