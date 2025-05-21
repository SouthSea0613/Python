from urllib.request import urlopen
from urllib.parse import urlencode

url = 'https://127.0.0.1:8888/cgi-bin/script.py'
data = {
    'name' : '김남해',
    'email' : 'tksz0613@gmail.com',
    'url' : 'https://www.google.com',
}
encData = urlencode(data)
postData = encData.encode('ascii')

f = urlopen(url, postData)
print(f.read().decode('cp949'))