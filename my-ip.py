import requests, json
me="https://www.whatismyip-address.com/?check"
res=requests.get(me).json
print(res)
