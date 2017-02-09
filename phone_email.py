import nltk
import os
import re
f = open('aks.txt').read()
re_phone = re.findall(('(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?'),f) 
print ('phone',re_phone)

re_email = re.findall(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-z A-Z]{1,4}',f)
print ('email',re_email)

