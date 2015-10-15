#!/usr/bin/python
import sys
import time
import yaml
import random
from slackclient import SlackClient

# Get the config file
with open('config.yml','r') as ymlfile:
  cfg = yaml.load(ymlfile)

# Set some variables from the config file
yubistring = cfg["yubikey"]["yubistring"]
token = cfg["slack"]["api_token"]
yubisays = cfg["yubisays"]
sc = SlackClient(token)

# Chomp yubistring to first 6 chars
if len(yubistring) > 6:
   yubistring = yubistring[:6]

if sc.rtm_connect():
  while True:
    new_evts =  sc.rtm_read()
    for evt in new_evts:
        if "type" in evt:
          if evt["type"] == "message" and "text" in evt:
            message=evt["text"]
            pline=""
            if yubistring in message and len(message) == 44:
              pline=random.choice (yubisays)
              chan = sc.server.channels.find(evt["channel"])
              if chan:
                chan.send_message(pline)
  time.sleep(1)
else:
  print "Connection Failed, invalid token?"
