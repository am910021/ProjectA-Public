import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings
from .models import Setting

class SMTP:
    def __init__(self):
        gmailAccount = Setting.objects.get_or_create(name="gmailAccount")[0]
        self.account = gmailAccount.c1
        self.passowrd = gmailAccount.c2
        
        if self.account!="" and self.passowrd!="" and gmailAccount.isActive:
            self.isActive = True
        else:
            self.isActive = False


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
    