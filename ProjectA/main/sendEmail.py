import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib.sessions.models import Session
from .models import Setting

class GmailAccount:
    def __init__(self):
        self.isActive=False
        self.account = ""
        self.passowrd = ""
        
        gmailAccount = Setting.objects.get_or_create(name="gmailAccount")[0]
        if (gmailAccount.c1!='' and gmailAccount.c2!='' and gmailAccount.isActive):
            self.account = gmailAccount.c1
            self.passowrd = gmailAccount.c2
            self.isActive = True
            
        

def sendGmailSmtp(strRecipient,strSubject,strContent):
    gmail = GmailAccount
    if not gmail.isActive:
        return False
    strGmailUser = gmail.account
    strGmailPassword = gmail.passowrd
    
    try:
        strMessage = MIMEMultipart()
        strMessage['From'] = strGmailUser
        strMessage['To'] = strRecipient
        strMessage['Subject'] = strSubject
        strMessage.attach(MIMEText(strContent))
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(strGmailUser, strGmailPassword)
        mailServer.sendmail(strGmailUser, strRecipient, strMessage.as_string())
        mailServer.close()
        return True
    except Exception as e:
        print(e)
        return False