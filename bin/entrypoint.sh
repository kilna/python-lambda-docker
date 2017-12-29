#!/bin/bash

pip install -r requirements.txt
sed -i 's/runtime: .*$/runtime: '"${python_runtime}"'/' config.yaml
cat config.yaml
if [[ -d .aws ]]; then
  pushd .
  cd ~ && ln -s /lambda/.aws
  popd
fi

exec "$@"

