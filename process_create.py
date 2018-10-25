#!python

import cgi, os
form = cgi.FieldStorage()
title = form['title'].value
desc = form['description'].value
files = os.listdir('data')

if title in files:
    #Redirection
    print("Location: index.py")
    print()
else:
    opened_file = open('data/'+title, 'w')
    opened_file.write(desc)
    opened_file.close()
    #Redirection
    print("Location: index.py?id=" + title)
    print()