import csv

with open("abbas.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"],row["age"])



user = [
    {"name": "Ali", "age": 25, "city": "Delhi"},
    {"name": "Zara", "age": 23, "city": "Mumbai"}
]

with open("exit.csv","w",newline="") as f:
    writer= csv.DictWriter(f,fieldnames=["name","age","city"],)
    writer.writeheader()
    writer.writerows(user)