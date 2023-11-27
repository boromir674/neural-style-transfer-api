# Serverless with AWS Lambda

## Opt1: use an AWS-based Image

### Build
The [runtime interface client](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-ric) is already included in the image.  

We need to take care only of our code and its dependencies.

```shell
docker build --platform linux/amd64 -t docker-image:test .
```

### Test

The [runtime interface emulator](https://docs.aws.amazon.com/lambda/latest/dg/images-test.html)
is already built inside the image, so we don't need to prepare anything.

Spin-up Lambda locally:  `docker run -it --rm -p 9000:8080 docker-image:test`

```shell
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"resource": "/", "path": "/", "httpMethod": "GET", "requestContext": {}}'

curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"resource": "/", "path": "/test", "httpMethod": "GET", "requestContext": {}}'

curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"resource": "/", "path": "/nst-rest", "httpMethod": "POST", "requestContext": {}, "queryStringParameters": {"ratio": "0.6", "iterations": "12"}, "body": }'
```
?ratio=0.6&iterations=10
`curl -X POST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'`

curl -X 'POST' \
  'http://127.0.0.1:8001/nst-rest?ratio=0.6&iterations=10' \
  -H 'accept: image/png' \
  -H 'Content-Type: multipart/form-data' \
  -F 'content_image=@canoe_water_w300-h225.jpg;type=image/jpeg' \
  -F 'style_image=@blue-red_w300-h225.jpg;type=image/jpeg'

### Deploy
Upload to ECR and then deploy to Lambda.


## Opt2: use custom Image

### Build
The [runtime interface client](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-ric) is already included in the image.  

We need to take care only of our code and its dependencies.

```shell
docker build --platform linux/amd64 -t docker-image:test .
```

### Test

The [runtime interface emulator](https://docs.aws.amazon.com/lambda/latest/dg/images-test.html)
is NOT built inside the image, so we opt for installing it in the host (other option is to
bake it in the image.)



Spin-up Lambda locally:  `docker run -it --rm -p 9000:8080 docker-image:test`

```shell
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}'
```


We must include a [runtime interface client](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-ric)
