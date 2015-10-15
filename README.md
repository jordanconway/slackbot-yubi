#slackbot-yubi
A basic slack bot that responds to accidental yubikey touches.

Requirements
-----
1. You need [python-slackclient](https://github.com/slackhq/python-slackclient) and [PyYAML](http://pyyaml.org/) installed.

2. A working Slack [bot user](https://api.slack.com/bot-users)

Usage
-----
1. Copy config.yml.sample to config.yml and fill in your values.
  * **yubistring:** is the first 6 digits of your yubikey otp code (they should always be the same)
  * **api_token:** is your slackbot api token

2. run slack_yubi.py - I should probably figure out how to daemonize this or something...
