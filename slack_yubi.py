#!/usr/bin/python
import sys
import time
import yaml
from slackclient import SlackClient

with open('config.yml','r') as ymlfile:
  cfg = yaml.load(ymlfile)
yubistring = cfg["yubikey"]["yubistring"]
token = cfg["slack"]["apitoken"] 
sc = SlackClient(token)
if sc.rtm_connect():
  while True:
    new_evts =  sc.rtm_read()
    for evt in new_evts:
        if "type" in evt:
          if evt["type"] == "message" and "text" in evt:
            message=evt["text"]
            pline=""
            if yubistring in message and len(message) == 44:
              pline="Hi yubi!"
              chan = sc.server.channels.find(evt["channel"])
              if chan:
                chan.send_message(pline)
  time.sleep(1)
else:
  print "Connection Failed, invalid token?"
