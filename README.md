# alpine-aws-python-lambda
Lightweight [docker image](https://hub.docker.com/r/kilna/alpine-aws-python-lambda/) for running and packaging python-based AWS lambda code.  This is based on [nficano](https://github.com/nficano/)'s super useful [python-lambda library](https://github.com/nficano/python-lambda/)

# Usage

An example of a usable project can be found in the [example/](./example/) directory.  This lambda function takes a JSON input file like the provided [event.json](./example/event.json) and returns an ASCII-art version of the text described in it.  The provided [Dockerfile](./example/Dockerfile) derives from this image and loads the current workspace into the image, then installs dependencies from the [requirements.txt](./example/requirements.txt) file.

To build a docker image called _example-lambda-image_ with the example lambda function in it, run:

```
$ cd example/
$ docker build --tag example-lambda-image .
```

If you want to execute the lambda function against the [event.json](./example/event.json) input file:

```
$ docker run example-lambda-image lambda invoke
  _  _         _   _                                    _      _   _
 | || |  ___  | | | |  ___        __ __ __  ___   _ _  | |  __| | | |
 | __ | / -_) | | | | / _ \  _    \ V  V / / _ \ | '_| | | / _` | |_|
 |_||_| \___| |_| |_| \___/ ( )    \_/\_/  \___/ |_|   |_| \__,_| (_)
                            |/

```

If you would like to see if your lambda function builds properly, run:

```
$ docker run example-lambda-image lambda build
```

If you would like to get a ZIP file of the lambda function suitable for uploading to Amazon, and the build log in one command:

```
$ docker run example-lambda-image sh -c 'rm -rf build.log dist || true && lambda build &>build.log && tar -c build.log dist' | tar -x -v
build.log
dist/
dist/2017-09-01-003647-example-lambda.zip
```
