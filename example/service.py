#!/usr/bin/env python
import subprocess
def handler(event, context):
  return subprocess.check_output( ['pyfiglet', '-f', event.get('font', 'small'), event.get('text', '') ] ).decode('ascii')
