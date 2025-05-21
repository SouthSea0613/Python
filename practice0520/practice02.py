from urllib.request import urlopen

print(urlopen('http://www.example.com').read(500).decode('utf-8'))