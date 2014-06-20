from flask import render_template
from flask.ext.mail import Message
from app import mail
from decorators import async
from config import ADMINS
import requests

@async
def send_email(subject, sender, recipients, text_body, html_body):
    return requests.post(
        "https://api.mailgun.net/v2/sandbox817101cca3eb41cca8651824d52d350c.mailgun.org/messages",
        auth=("api", "key-1rksvcw43bl7h4rbdpjg0gqpc969-z41"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox817101cca3eb41cca8651824d52d350c.mailgun.org>",
        "to": recipients,
        "subject: ": subject,
        "text": text_body})

    
def follower_notification(followed, follower):
    send_email("[liblogger] %s is now following you!" % follower.nickname,
        ADMINS[0],
        [followed.email],
        render_template("follower_email.txt", 
            user=followed, follower=follower),
        render_template("follower_email.html", 
            user=followed, follower=follower))
        