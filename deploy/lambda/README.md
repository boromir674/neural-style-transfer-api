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
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}'
```

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