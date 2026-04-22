travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visited": 12
    }, 
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Munich"],
        "total_visited": 5
    }
]

def add_new_country (country, cities_visited, total_visited):
    new_country = {}
    new_country["country"] = country
    new_country["cities_visited"] = cities_visited
    new_country["total_visited"] = total_visited
    travel_log.append(new_country)

add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)
print(travel_log)