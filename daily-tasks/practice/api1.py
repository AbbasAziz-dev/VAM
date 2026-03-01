user = {
    "id": 1,
    "name": "Abbas",
    "address": {
        "city": "Hyderabad",
        "geo": {
            "lat": "17.3850",
            "lng": "78.4867"
        }
    }
}



city = user.get("address",{}).get("geo",{})

print(city)