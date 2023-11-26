FROM public.ecr.aws/lambda/python:3.8 as base

# Determine where to install poetry
ENV POETRY_HOME=/opt/poetry

# Install Poetry
RUN python -c 'from urllib.request import urlopen; print(urlopen("https://install.python-poetry.org").read().decode())' | python

# Generate requirements.txt from poetry format
COPY poetry.lock pyproject.toml ./
RUN "$POETRY_HOME/bin/poetry" export -f requirements.txt  -E lambda > /tmp/requirements.txt


FROM public.ecr.aws/lambda/python:3.8 as install
# LAMBDA_TASK_ROOT : /var/task

COPY --from=base /tmp/requirements.txt /tmp/requirements.txt

# Copy requirements.txt
COPY /tmp/requirements.txt ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install -r /tmp/requirements.txt

# Copy function code
COPY deploy/lambda/app.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]


## How to Build
# docker build --platform linux/amd64 -t docker-image:test .

# run a shell (ie bash) in container
# docker run -it --rm -p 9000:8080 --entrypoint bash docker-image:test

## How to Test
# docker run -it --rm -p 9000:8080 docker-image:test

# curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'

# curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}'