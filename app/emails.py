from flask import render_template
from flask.ext.mail import Message
from app import mail
from decorators import async
from config import LOGIN, PASSWORD
from config import ADMINS
import requests

@async
def send_email(subject, sender, recipients, text_body, html_body):
    smtp = SMTP("smtp.mailgun.org", 587)
    smtp.login(LOGIN, PASSWORD)
    smtp.sendmail("liblog.team@gmail.com", ADMINS[0], text_body)
    smtp.quit()

    
def follower_notification(followed, follower):
    send_email("[liblogger] %s is now following you!" % follower.nickname,
        ADMINS[0],
        [followed.email],
        render_template("follower_email.txt", 
            user=followed, follower=follower),
        render_template("follower_email.html", 
            user=followed, follower=follower))
        