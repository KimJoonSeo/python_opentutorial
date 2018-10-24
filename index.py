#!python
print("Content-Type: text/html; charset=utf-8")
print()
import cgi
form = cgi.FieldStorage()
# pageId = form["id"].value
pageId = "javascript" if "id" not in form else form["id"].value
if 'id' in form:
  pageId = form['id'].value
  pageBody = open('data/' + pageId, 'r').read()
else :
  pageId = 'welcome'
  pageBody = 'thank you'
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    <li><a href="index.py?id=html">HTML</a></li>
    <li><a href="index.py?id=CSS">CSS</a></li>
    <li><a href="index.py?id=javascript">JavaScript</a></li>
  </ol>
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=pageBody))
