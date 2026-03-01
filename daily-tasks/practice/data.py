import json
with open("user.json","r") as file:
    data= json.load(file)

location= data.get("address",{}).get("city")

print(location)