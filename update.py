#!python
print("Content-Type: text/html; charset=utf-8")
print()
import cgi, os
files = os.listdir('data')
form = cgi.FieldStorage()

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
  <h2>Update {title}</h2>
  <form action="process_update.py" method="post">
    <input type="hidden" name="pageId" value={form_default_title} />
    <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></p>
    <p><input type="submit" /></p>
  </form>
</body>
</html>
'''.format(title=pageId, desc=pageBody, form_default_title=pageId, form_default_description=pageBody))
