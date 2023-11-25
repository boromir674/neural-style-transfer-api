#!/usr/bin/env sh

set -e

##### Run the Application Server in dev mode #####

# Our Application Server, is written in Python,
# and is an implmentation of ASGI (Asynchronous Server Gateway Interface),
# since the code leverage coroutines to handle concurrent requests.

# Uvicorn is our specific ASGI implmentation.



python -m uvicorn --host 0.0.0.0 --reload-dir src/neural_style_transfer_api --reload neural_style_transfer_api.app_instance:app

# python -m uvicorn neural_style_transfer_api.main:app --host --reload --reload-dir src/neural_style_transfer_api




# #!/usr/bin/env bash

# set -e

# if [ -n "${RUN_API}" ]; then
#     #             TIMEOUT is undefined
#     gunicorn -w 16 -t 0 -b 0.0.0.0:8080 -k uvicorn.workers.UvicornWorker app.api.main:app
# elif [ -n "${RUN_WORKER}" ]; then
#     celery -A app.job_runner.celery.worker worker -Ofair --concurrency=16
# elif [ -n "${RUN_MIGRATIONS}" ]; then
#     alembic upgrade head
# elif [ -n "${RUN_SCHEDULER}" ]; then
#     PYTHONPATH=$PWD python app/scheduler/main.py
# else
#     # shellcheck disable=SC2016
#     echo 'ERROR: Neither $RUN_API nor $RUN_WORKER nor $RUN_MIGRATIONS is not set'
#     exit 127
# fi
