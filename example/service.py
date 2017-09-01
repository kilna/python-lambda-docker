#!/usr/bin/env python
import subprocess
def handler(event, context):
  return subprocess.check_output( ['xart', '-f', event.get('font', 'Small'), event.get('text', '') ] )
