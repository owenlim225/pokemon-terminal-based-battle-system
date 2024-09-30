#Limosnero, Sherwin P.
# J2S
# Machine Problem #1M



# Pokémon names, health, power, poison and potions
pokemons = [
    ["Pikachu", 35, 55, 12, 2],
    ["Bulbasaur", 45, 49, 15, 3],
    ["Charmander", 39, 52, 8, 1],
    ["Squirtle", 44, 48, 10, 2],
    ["Jigglypuff", 115, 45, 20, 4],
    ["Gengar", 60, 65, 25, 5],
    ["Machamp", 90, 130, 14, 3],
    ["Lapras", 130, 85, 6, 4],
    ["Psyduck", 50, 52, 9, 2],
    ["Snorlax", 160, 110, 5, 4],
]




class Mechanics:
    def __init__(self) -> None:
        self.player1 = []
        self.player2 = []
    
    
    # Print out all the names of the pokemon 
    def pokemon_list_display() -> None:
        for count, pokemon in enumerate(pokemons, start=1):
            print(f"[{count}]{pokemon[0]}", end="\t\t" if (count) % 2 else "\n")

    
    
    
    # Choose three pokemon
    def Choose_Pokemon(self, player1, player2) -> list:
        while player1 < 3:
            self.pokemon_list_display()
            player1 = list(map(int, input("Choose 3 pokemon: ").split()))
            


class Display(Mechanics):
    def __init__(self) -> None:
        super().__init__()
        pass
    
    

            
    

if __name__ == "__main__":
    pass
