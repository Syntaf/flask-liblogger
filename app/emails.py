from flask import render_template
from flask.ext.mail import Message
from app import mail
from decorators import async
from config import KEY, SANDBOX
from config import ADMINS
import requests

def send_email(subject, sender, recipients, text_body, html_body):
    request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(SANDBOX)
    request = requests.post(request_url, auth=('api', KEY), data={
        'from': 'lith@example.com',
        'to': ADMINS[0],
        'subject': subject,
        'text': text_body
    })

    
def follower_notification(followed, follower):
    send_email("[liblogger] %s is now following you!" % follower.nickname,
        ADMINS[0],
        [followed.email],
        render_template("follower_email.txt", 
            user=followed, follower=follower),
        render_template("follower_email.html", 
            user=followed, follower=follower))
        