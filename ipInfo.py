import json
from urllib.request import urlopen
from pyfiglet import figlet_format
print(figlet_format("el tekito\nIp Info", "cybermedium"))

url = "https://ipinfo.io/json"
response = urlopen(url)
data = json.load(response)

print("\nel_tekito@IpInfo [Ip Adress] -> ", data["ip"])
print("\nel_tekito@IpInfo [Country]   -> ", data["country"])
print("\nel_tekito@IpInfo [City]      -> ", data["city"])
print("\nel_tekito@IpInfo [Location]  -> ", data["loc"])
print("\nel_tekito@IpInfo [Org]       -> ", data["org"],"\n")