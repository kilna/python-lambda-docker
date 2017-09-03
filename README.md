# python-lambda-docker

[![](https://images.microbadger.com/badges/image/kilna/python-lambda.svg)](https://microbadger.com/images/kilna/python-lambda)
[![](https://img.shields.io/docker/imagelayers/image-size/kilna/python-lambda.svg?style=plastic)](https://hub.docker.com/r/kilna/python-lambda/)
[![](https://img.shields.io/docker/imagelayers/layers/kilna/python-lambda.svg?style=plastic)](https://hub.docker.com/r/kilna/python-lambda/)
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

I needed a Docker-based environment in which to host AWS python lambda functions for the purpose of testing and building them... python-lambda works well under virtualenv for development, but build and deployment automation require a clean and reproducible environment to operate in. Our CI system already supported Docker as a containerization sytem, so it was the obvious choice.

In order to use this, you will have your project derive its own Dockerfile based on a base python-lambda image corresponding to which version of Python you wish to run.

## Usage

An example of a usable project can be found in the [example/](./example/) directory.  This lambda function in [service.py](./example/service.py) takes a JSON input file like the one provided in [event.json](./example/event.json) and returns an ASCII-art version of the text described in it.  The provided [Dockerfile](./example/Dockerfile) derives from this image and loads the current workspace into the image at the path _/lambda_, then installs dependencies from the [requirements.txt](./example/requirements.txt) file.  

To build a docker image called _example-lambda-image_ with the example lambda function in it, run:

```
$ cd example/
$ docker build --tag example-lambda-image .
```

If you want to execute the lambda function against the [event.json](./example/event.json) input file:

```
$ docker run example-lambda-image lambda invoke
 _  _     _ _                        _    _ _
| || |___| | |___    __ __ _____ _ _| |__| | |
| __ / -_) | / _ \_  \ V  V / _ \ '_| / _` |_|
|_||_\___|_|_\___( )  \_/\_/\___/_| |_\__,_(_)
                 |/
```

If you would like to see if your lambda function build (which will package the lambda and all dependencies within the container into a zip file), run:

```
$ docker run example-lambda-image lambda build
```

### Build and Test

If you would like to build and test the lambda function and gather up the results, you can run:

```
$ docker run example-lambda-image lambda_build_tar | tar -x -v
build.log
test.log
dist/
dist/2017-09-01-003647-example-lambda.zip
```

Behind the scenes, what this script does is:

* Removes any log and dist files from prior runs
* Runs 'lambda build' and stores the log in _/lambda/build.log_ in the container
* If present and executable, run _/lambda/run_tests_ and stores the log in /lambda/test.log in the container
* Tars the log files, and the contents of the dist directory in /lambda on the container and pipes it to standard output
* Untars the contents bundled up within the container, and extracts them into your current directory 

### Python Version

The example Dockerfile uses _:latest_ in the FROM line, which is currently the same as _:python-3.6_, but if you wish to use different python versions you can change this.

For instance, if you want to use Python version 2.7 change the first line of your Dockerfile from:

```
FROM kilna/python-lambda:latest
```

To:

```
FROM kilna/python-lambda:2.7
```

