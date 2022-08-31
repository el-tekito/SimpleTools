from logging import exception
from sys import exc_info
from pyfiglet import figlet_format
from smtplib import SMTP
print(figlet_format("El tekito\nmail sender", font="cybermedium"))
try:
    #fakeMail =input("el_tekito@MailSender [Fake Mail] -> ")
    targetMail =input("el_tekito@MailSender [Target Mail] -> ")
    youMail =input("el_tekito@MailSender [You Mail] -> ")
    youPasswd =input("el_tekito@MailSender [You Password] -> ")
    smtpcon =input("el_tekito@MailSender [SMTP] -> ")
    subject =input("el_tekito@MailSender [Subject] -> ")
    messages =input("el_tekito@MailSender [Message] -> ")
    mail = SMTP(smtpcon,587)
    mail.ehlo()
    mail.starttls()
    mail.login(youMail,youPasswd)
    mail.sendmail(youMail,targetMail,subject,messages)
except exception as e:
    print("error"+e)
