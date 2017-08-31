# alpine-aws-python-lambda
Lightweight docker image for running and packaging python-lambda code.

This is based on the super useful python-lambda library:

<https://github.com/nficano/python-lambda/>

# Usage

An example of a usable project can be found in the <example/> directory.  This example lambda function
takes a JSON input file like event.json and returns an ASCII-art version of the text.

```$ cd example/
```

The Dockerfile in the example directory loads the current workspace into the image and installs
dependencies from the requirements.txt file:

```FROM kilna/alpine-aws-python-lambda
COPY . /workspace
RUN pip install -r requirements.txt
```

To build a docker image called 'example-lambda-image' with the lambda function in it, run:

```$ docker build --tag example-lambda-image .
```

If you want to execute the lambda function against an event.json input file:

```$ docker run example-lambda-image lambda invoke
  _  _         _   _                                    _      _   _
 | || |  ___  | | | |  ___        __ __ __  ___   _ _  | |  __| | | |
 | __ | / -_) | | | | / _ \  _    \ V  V / / _ \ | '_| | | / _` | |_|
 |_||_| \___| |_| |_| \___/ ( )    \_/\_/  \___/ |_|   |_| \__,_| (_)
                            |/

```

If you would like to see if your lambda function builds properly, run:

```$ docker run example-lambda-image lambda build
```

If you would like to get a ZIP file of the lambda function suitable for uploading to Amazon:

```$ docker run example-lambda-image sh -c 'rm -rf dist* && lambda build 2&>1 >/dev/null && tar -c dist/*.zip' | tar -x -v
dist/2017-08-31-212523-example-lambda.zip
```


