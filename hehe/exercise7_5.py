# iterates the "cities" list, count & sum letter "a" in each city name
cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai",
          "Mexico City", "São Paulo", "Hyderabad"]
search_letter = "a"
total = 0

for city_name in cities:
    total += city_name.lower().count(search_letter)

print("The total # of \"" + search_letter + "\" found in the list is", total)
