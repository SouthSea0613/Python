import cgi

form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
url = form.getvalue('url')

print('Content-type: text/plain')
print()

print('Welcome CGI Scripts')
print('name :', name)
print('email :', email)
print('url :', url)