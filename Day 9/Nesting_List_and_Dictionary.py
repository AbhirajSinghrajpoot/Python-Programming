travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visited": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Munich"], "total_visited": 5}
}

# Nesting Dictionary in a List

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visited":12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Munich"],
        "total_visited": 5
    },
]

print(travel_log)