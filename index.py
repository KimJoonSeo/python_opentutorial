#!python
print("Content-Type: text/html; charset=utf-8")
print()
import cgi, view



form = cgi.FieldStorage()
# pageId = form["id"].value
# pageId = "javascript" if "id" not in form else form["id"].value
if 'id' in form:
  pageId = form['id'].value
  pageBody = open('data/' + pageId, 'r').read()
  update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
  delete_action = '''
    <form action="process_delete.py" method="post">
      <input type="hidden" name="pageId" value="{}" />
      <input type="submit" value="delete" />
    </form>
  '''.format(pageId)
else :
  pageId = 'welcome'
  pageBody = 'thank you'
  update_link = ''
  delete_action = ''
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
  {delete_action}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=pageBody, ls=view.getList(), update_link=update_link, delete_action=delete_action))
