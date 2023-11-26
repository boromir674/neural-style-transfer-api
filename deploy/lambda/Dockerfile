FROM public.ecr.aws/lambda/python:3.8

# Copy requirements.txt
# COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the specified packages
# RUN pip install -r requirements.txt

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}
# LAMBDA_TASK_ROOT is ie /var/task

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