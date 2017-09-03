#!/usr/bin/env python

from pyfiglet import Figlet

def handler(event, context):
  f = Figlet( font=event.get('font', 'small') )
  return f.renderText( event.get('text', '') )

