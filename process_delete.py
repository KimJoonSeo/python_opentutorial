#!python

import cgi, os
form = cgi.FieldStorage()
pageId = form['pageId'].value
files = os.listdir('data')

if pageId in files:
    os.remove('data/'+pageId)

#Redirection
print("Location: index.py")
print()