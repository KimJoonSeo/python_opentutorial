#!python
print("Content-Type: text/html; charset=utf-8")
print()
import cgi, os
files = os.listdir('data')
listStr = ''
for item in files:
  listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
# pageId = form["id"].value
# pageId = "javascript" if "id" not in form else form["id"].value
if 'id' in form:
  pageId = form['id'].value
  pageBody = open('data/' + pageId, 'r').read()
  update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
else :
  pageId = 'welcome'
  pageBody = 'thank you'
  update_link = ''
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {ls}
  </ol>
  <a href="create.py">create</a>
  {update_link}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=pageBody, ls=listStr, update_link=update_link))
