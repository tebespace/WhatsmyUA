import requests
from bs4 import BeautifulSoup as bs

r = requests.get('http://whatsmyuseragent.org')
print
print('menuju: '+r.url)
print('response code: '+str(r.status_code))
print
b = bs(r.text,"html.parser")
for ua in b.find_all('p',class_="intro-text"):
     print(ua.text)

print
#<div class='user-agent'

#print(dir(ua))
