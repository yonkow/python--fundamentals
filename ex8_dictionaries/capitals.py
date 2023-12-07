countries = input().split(', ')
capitals = input().split(', ')

# capitals_by_countries = dict(zip(countries, capitals))
capitals_by_countries = {countries[index]: capitals[index] for index in range(len(countries))}
for country, capital in capitals_by_countries.items():
    print(f"{country} -> {capital}")
