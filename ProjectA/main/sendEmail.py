import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings
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
            if self.account!="" and self.passowrd!="":
                self.isActive = True
            else:
                self.isActive = False
        

class SMTP:
    def __init__(self):
        gmail = GmailAccount()
        self.account=gmail.account
        self.account=gmail.passowrd
        self.isActive = gmail.isActive


    def send(self, strRecipient,strSubject,html,text):
        strGmailUser = self.account
        strGmailPassword = self.passowrd
        strSubject="["+ settings.SITE_NAME +"] " + strSubject
        try:
            strMessage = MIMEMultipart()
            strMessage['From'] = strGmailUser
            strMessage['To'] = strRecipient
            strMessage['Subject'] = strSubject
            #strMessage.preamble = 'This is a multi-part message in MIME format.'
            
            # Encapsulate the plain and HTML versions of the message body in an
            # 'alternative' part, so message agents can decide which they want to display.
            msgAlternative = MIMEMultipart('alternative')
            strMessage.attach(msgAlternative)
            msgText = MIMEText(text)
            msgAlternative.attach(msgText)
            msgText = MIMEText(html, 'html')
            msgAlternative.attach(msgText)
            
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
    
def sendGmailSmtp2(strRecipient,strSubject):
    gmail = GmailAccount()
    if not gmail.isActive:
        return False
    strGmailUser = gmail.account
    strGmailPassword = gmail.passowrd
    
    try:
        strMessage = MIMEMultipart()
        strMessage['From'] = strGmailUser
        strMessage['To'] = strRecipient
        strMessage['Subject'] = strSubject
        strMessage.preamble = 'This is a multi-part message in MIME format.'
        
        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        strMessage.attach(msgAlternative)
        
        msgText = MIMEText('This is the alternative plain text message.')
        msgAlternative.attach(msgText)
        
        # We reference the image in the IMG SRC attribute by the ID we give it below
        msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!', 'html')
        msgAlternative.attach(msgText)
        
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