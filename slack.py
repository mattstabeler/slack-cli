
# take user input like:
# slack [teamname] {#channel|@user} message
# and post it to the logged in slack

# Store team tokens in a config file ~/.slack-cli/teams.json
import urllib
import urllib2
import json


webhookurl = "https://hooks.slack.com/services/"


message = "Your message here."
channel = "#general"

request = {
    "username": "CLI Bot",
    # "icon_url": "https://slack.com/img/icons/app-57.png",
    "icon_emoji": ":ghost:",
    "text" : message,
    "channel" : channel

}

json_payload =  json.dumps(request)

print json_payload

# data = urllib.urlencode(json_payload)
req = urllib2.Request(webhookurl, json_payload)
response = urllib2.urlopen(req)
the_page = response.read()

print the_page