pokemon_char = {
    "Pikachu": 50,
    "Charmander": 55,
    "Bulbasaur": 60,
    "Squirtle": 58,
    "Jigglypuff": 45,
    "Eevee": 52,
    "Snorlax": 80,
    "Gengar": 70,
    "Machamp": 75,
    "Mewtwo": 90 
}

# Sort the dictionary by value in descending order
sorted_pokemon = sorted(pokemon_char.items(), key=lambda item: item[1], reverse=True)

# Print the sorted dictionary
print("pokemon_char = {")
for pokemon, value in sorted_pokemon:
    print(f"\"{pokemon}\": {value},")
print("}")