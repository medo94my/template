import smtplib
import codecs

from contextlib import contextmanager
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from timeit import default_timer as timer
import re

@contextmanager
def logined(sender, password, smtp_host='smtp.gmail.com', smtp_port=587):
    start = timer()
    smtp_serv = smtplib.SMTP(smtp_host, smtp_port, timeout=10)
    try:
        # make smtp server and login
        smtp_serv.ehlo_or_helo_if_needed()
        smtp_serv.starttls()
        smtp_serv.ehlo()
        print('\nsmtp setup took (%.2f seconds passed)' % (timer() - start,))
        start = timer()
        smtp_serv.login(sender, password)
        print('login took %.2f seconds' % (timer() - start,))
        start = timer()
        yield smtp_serv

    finally:
        print('\nOperations with smtp_serv took %.2f seconds' % (timer() - start,))
        start = timer()
        smtp_serv.quit()
        print('Quiting took %.2f seconds' % (timer() - start,))
        print("\n")


smtp_host = 'smtp.gmail.com'
gmail_user, gmail_pwd = "tawfik@kidocode.com", "mad@tec980326"

kido_frm = "Ahmed"


def send_blast(email_list, subject, template, count):
    with logined(gmail_user, gmail_pwd, smtp_host) as smtp_serv:
        template = MIMEText(template, 'html')
        c = count
        for i in email_list:
            try:
                if i:
                    msg = MIMEMultipart('alternative')
                    msg['Subject'] = subject
                    msg['From'] = kido_frm
                    msg['To'] = i

                    msg.attach(template)
                    print(c, "Sent:", i, smtp_serv.sendmail(msg['From'], msg['To'], msg.as_string()))
                    c += 1
            except Exception as e:
                print(e.args)


_email_list = ["nasrin@kidocode.com"]
def replace_template_value(template,values):
    for key in values:
        template=re.sub(key,values[key],template)
    return template

values={
    "{{student_name}}":"Ahmed Test",
    "{{parent_name}}":"Tawfik Test",
    "{student.name}":"Ahmed Test",
    "{his/her}":"his",
    "{weekly/monthly}":"monthly",
    "{{Weekly/Monthly}}":"Monthly"
}
with open('./progress-report-template.html','r+', encoding='utf-8') as f:
    html=f.read()
    html=replace_template_value(html,values)

send_blast(_email_list, "last changes", html, 0)
