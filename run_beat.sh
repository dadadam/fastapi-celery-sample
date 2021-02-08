#!/bin/sh

celery -A src.celery_app beat -l info