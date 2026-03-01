import json 
data={
    "name":"Abbbas",
    "age":21,
    "education":True
    }

with open("user.json","w") as file:
    json.dump(data,file, indent=5)

  