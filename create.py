#!python
print("Content-Type: text/html; charset=utf-8")
print()

print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <form action="process_create.py" method="post">
    <p><input type="text" name="title" placeholder="title" /></p>
    <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
    <p><input type="submit" /></p>
  </form>
</body>
</html>
''')
