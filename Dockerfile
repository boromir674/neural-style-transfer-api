FROM python:3.8.12-slim-bullseye as base

# Determine where to install poetry
ENV POETRY_HOME=/opt/poetry

# Install Poetry
# RUN pip install poetry
RUN python -c 'from urllib.request import urlopen; print(urlopen("https://install.python-poetry.org").read().decode())' | python
# RUN curl -sSL https://install.python-poetry.org | python

# Generate requirements.txt from poetry format
COPY poetry.lock pyproject.toml ./
RUN "$POETRY_HOME/bin/poetry" export -f requirements.txt -E lambda > requirements.txt
# RUN poetry export -f requirements.txt -E lambda > requirements.txt

FROM public.ecr.aws/lambda/python:3.8 as install
# LAMBDA_TASK_ROOT : /var/task

# Copy requirements.txt
COPY --from=base requirements.txt ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install -r ${LAMBDA_TASK_ROOT}/requirements.txt

COPY --from=base pyproject.toml .
COPY --from=base poetry.lock .
COPY src src
COPY README.md README.md
RUN pip install .

COPY deploy/lambda/lambda_function.py ${LAMBDA_TASK_ROOT}
CMD [ "lambda_function.handler" ]

# test:
# curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"resource": "/", "path": "/api/v1/test/", "httpMethod": "GET", "requestContext": {}, "multiValueQueryStringParameters": null}'


# Copy function code
# COPY deploy/lambda/app.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
# CMD [ "app.handler" ]



## How to Build
# docker build --platform linux/amd64 -t docker-image:test .

# run a shell (ie bash) in container
# docker run -it --rm -p 9000:8080 --entrypoint bash docker-image:test

## How to Test
# docker run -it --rm -p 9000:8080 docker-image:test

# curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
# curl "http://localhost:8001/2015-03-31/functions/function/invocations"
# curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}'