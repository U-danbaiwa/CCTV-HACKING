import requests, json
me="https://www.whatismyip-address.com/json"
res=requests.get(me).json
print(res["Decimal"])
print(res["Organization"])
