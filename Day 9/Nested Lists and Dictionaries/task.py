capitals = {
    "France": "Paris",
    "Germany": "Beline"
}

# Nested List in Dictionary

travel_vlog = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# print lille
print(travel_vlog["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2])
print(nested_list[2][1])


travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Stuttgart", "Berlin", "Berlin"],
        "total_visit": 5
    }
}

places = (travel_log["Germany"])
print(places["cities_visited"][2])
