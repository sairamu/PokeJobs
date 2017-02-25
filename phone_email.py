import nltk
import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


f = open('aks.txt').read()
re_phone = re.findall(('(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?'),f)
phone = str(re_phone)[1:-1] #converts list object to str

re_email = re.findall(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-z A-Z]{1,4}',f)
#email = str(re_email).strip('[]') #converts list object to str
email = re_email[0]

msg = MIMEMultipart()
msg['From'] = "pythonmailtesting@gmail.com"
msg['To'] = email
msg['Subject'] = "Welcome to PokeJobs"

body = '''Hi ,

Welcome to PokeJobs
 '''

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
#Next, log in to the server
server.login("pythonmailtesting@gmail.com", "asdf123456789")
text = msg.as_string()
#Send the mail
server.sendmail("pythonmailtesting@gmail.com", email, text)
server.close()