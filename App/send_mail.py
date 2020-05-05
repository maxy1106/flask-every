from threading import Thread

from flask_mail import Message
from App.ext import mail
from flask import render_template

def send_msg(to, title, template, **kwargs):
    msg = Message(title, sender='小猫游园<m15600352552@163.com>', recipients=to)
    msg.body = render_template(template+'.txt', **kwargs)
    msg.html = render_template(template+'.html', **kwargs)
    # thr = Thread(target=send_sync_msg, args=[app, msg])
    # thr.start()
    # return thr


def send_sync_msg(app, msg):
    with app.app_context():
        mail.send(msg)