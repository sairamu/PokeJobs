import nltk
import os
import re
f = open('aks.txt').read()
re_phone = re.findall(r'((?:\(?\+34\)?)?\d{12})',f) or (r'((?:\(?\+34\)?)?\d{10})',f)
print ('phone',re_phone)

re_email = re.findall(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-z A-Z]{1,4}',f)
print ('email',re_email)

