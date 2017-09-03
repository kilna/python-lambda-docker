# python-lambda-docker

[![](https://images.microbadger.com/badges/image/kilna/python-lambda.svg)](https://microbadger.com/images/kilna/python-lambda)
[![](https://img.shields.io/docker/pulls/kilna/python-lambda.svg?style=plastic)](https://hub.docker.com/r/kilna/python-lambda/)
[![](https://img.shields.io/docker/stars/kilna/python-lambda.svg?style=plastic)](https://hub.docker.com/r/kilna/python-lambda/)
[![](https://img.shields.io/badge/docker_build-automated-blue.svg?style=plastic)](https://cloud.docker.com/swarm/kilna/repository/docker/kilna/python-lambda/builds)
[![](https://img.shields.io/badge/python-2.7,_3.3,_3.4,_3.5,_3.6-blue.svg?style=plastic)](https://github.com/kilna/python-lambda-docker/)

Lightweight docker image for running and packaging python-based AWS lambda code

## Links

* Docker: [python-lambda](https://hub.docker.com/r/kilna/python-lambda/)
* GitHub: [python-lambda-docker](https://github.com/kilna/python-lambda-docker)
* Based on the [python-lambda library](https://github.com/nficano/python-lambda/) by [nficano](https://github.com/nficano/)

## Purpose

I needed a Docker-based environment in which to host AWS python lambda functions for the purpose of testing and building them... python-lambda works well under virtualenv for development, but build and deployment automation require a clean and reproducible environment to operate in. Our CI system already supported Docker as a containerization system, so it was the obvious choice.

In order to use this, you will have your project derive its own Dockerfile based on a base python-lambda image corresponding to which version of Python you wish to run.

## Usage

An example of a usable project can be found in the [example/](./example/) directory.  The lambda function in [service.py](./example/service.py) takes a JSON input file like the one provided in [event.json](./example/event.json) and returns an ASCII-art version of the text described in it.  The [Dockerfile](./example/Dockerfile) derives from python-lambda as a base image, and loading the example directory contents into the image at the path _/lambda_, then installs dependencies from the [requirements.txt](./example/requirements.txt) file.  

### Building a Derived Docker Image

To build a docker image from the provided [exmaple/](./exmaple) called _example-lambda-image_ with the ASCII-art lambda function in it, run:

```
$ cd example/
$ docker build --tag example-lambda-image .
```

Any time you make changes to the example project, you'll need to re-run the `docker build` command above, or you can investigate using docker volumes to sync local filesystem changes into the container. 

#### Switching Python Versions

The example [Dockerfile](./example/Dockerfile) uses a _:latest_ docker tag in the FROM line, which is currently the same as _:3.6_, but if you wish to use a different Python version you can change this. Supported Python versions are 2.7, 3.3, 3.4, 3.5, 3.6. To use Python version 2.7 change the first line of the example [Dockerfile](./example/Dockerfile) to:

```
FROM kilna/python-lambda:2.7
```

You will also need to change the following line in [config.yaml](./example/config.yaml)

```
runtime: python2.7
```

### Executing the Lambda Function

If you want to execute the lambda function against the [event.json](./example/event.json) input file:

```
$ docker run example-lambda-image lambda invoke
 _  _     _ _                        _    _ _
| || |___| | |___    __ __ _____ _ _| |__| | |
| __ / -_) | / _ \_  \ V  V / _ \ '_| / _` |_|
|_||_\___|_|_\___( )  \_/\_/\___/_| |_\__,_(_)
                 |/
```

### Building and Testing the Lambda Function

If you would like to builf the lambda function (which will package the function and all its dependencies), run:

```
$ docker run example-lambda-image lambda build
```

The result will be a zip file created in the /lambda/dist directory inside the container.

If you would like to build and _test_ the lambda function and gather up the results, you can run:

```
$ docker run example-lambda-image lambda_build_tar | tar -x -v
build.log
test.log
dist/
dist/2017-09-01-003647-example-lambda.zip
```

Behind the scenes, what this does is:

* Removes any log and dist files from prior runs
* Executes 'lambda build' and stores the log in _/lambda/build.log_ in the container
* If present and executable, runs _/lambda/run_tests_ and stores the log in /lambda/test.log in the container
* Tars the log files, and the contents of the dist directory in /lambda on the container and pipes it to standard output
* Untars the contents bundled up within the container, and extracts them into your current directory

### Deploying the Lambda Function

You can deploy your lambda function to Amazon's infrastructure...  you'll need to add AWS credentials into the [config.yaml](./example/config.yaml) file. Alternately you can credentials into your container by configuring them through the Dockerfile, for example by adding a `COPY .aws /root/.aws` line, where example/.aws/ is a copy of your ~/.aws/ directory. Once AWS is working within your container, you can then run the following to deploy your function to Amazon:

```
$ docker run example-lambda-image lambda deploy
```

