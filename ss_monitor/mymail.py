#!/usr/bin/python
# coding=UTF-8
import email
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
  
class SendEmail(object):
 def __init__(self):
  self.host = 'smtp.office365.com' #smtp域名，用的outlook
  self.port = '587' 				#smtp端口
  self.sender = 'XXXXX@XXXX.com' #发件人账号
  self.password = 'XXXXX'		 #发件人密码
  
 def send_email(self, receiver, subject='', body=''):
  message = MIMEText(body, 'plain', 'utf-8')
  message['From'] = self.sender
  message['To'] = receiver
  message['Subject'] = subject
  
  try:
   email_clint = smtplib.SMTP(self.host, self.port)
   email_clint.starttls()
   print 'success get SSL'
   login_result = email_clint.login(self.sender, self.password)
   print 'login in'
   if login_result[0] == 235:
    print 'success'
    email_clint.sendmail(self.sender, receiver, message.as_string())
    print 'sendmail success'
   else:
    print 'fail'
  except Exception as e:
   print('myerror', e)
#mymail = SendEmail()
#mymail.send_email('guarantee2u@qq.com','你好鸭',"各位， 今天天气可以哦")
