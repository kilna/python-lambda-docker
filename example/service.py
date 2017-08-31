#!/usr/bin/env python

import subprocess
import json

def handler(event, context):
  font=event.get('font', 'Small')
  text=event.get('text', '')
  return subprocess.check_output( ['xart', '-f', font, text ] )
