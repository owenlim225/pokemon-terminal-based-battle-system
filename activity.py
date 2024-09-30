#Limosnero, Sherwin P.
# J2S
# Machine Problem #1M

import os

class Mechanics:
    def __init__(self):
        self.player1 = []
        self.player2 = []
        
        # Pokémon names, health, power, poison and potions
        self.pokemons = [
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
    
    # Print out all the names of the Pokémon 
    def pokemon_list_display(self):
        for count, pokemon in enumerate(self.pokemons):
            # Print Pokémon name with appropriate formatting
            print(f"[{count}] {pokemon[0]}", end="\t\t" if (count % 2 == 0) else "\n")
        # Ensure a newline after the last row if the number of Pokémon is odd
        if len(self.pokemons) % 2 != 0:
            print()
    
    # Choose three Pokémon
    def Choose_Pokemon(self, player_num):
        chosen_pokemons = []
        
        # Player [num] Choose Pokémon
        while len(chosen_pokemons) < 3:
            print(f"\tPlayer {player_num}\n")
            self.pokemon_list_display()
            
            # User choices
            choices = list(map(int, input("Choose 3 Pokémon: ").split()))
            
            if len(choices) > 3:
                print("Please choose up to 3 Pokémon.")
                continue
            
            if all(0 <= choice < len(self.pokemons) for choice in choices):
                chosen_pokemons = choices
                print(f"\nPlayer {player_num} has chosen: {', '.join(self.pokemons[i][0] for i in chosen_pokemons)}\n")
                
                # Add chosen Pokémon to the player list
                if player_num == 1:
                    self.player1.extend(self.pokemons[i] for i in chosen_pokemons)
                elif player_num == 2:
                    self.player2.extend(self.pokemons[i] for i in chosen_pokemons)
                
                # Remove chosen Pokémon from the list
                self.pokemons = [pokemon for index, pokemon in enumerate(self.pokemons) if index not in chosen_pokemons]
                return chosen_pokemons  # Return the chosen Pokémon
            else:
                print("Invalid choices. Please choose indices from the list.")
        

class Display(Mechanics):
    def __init__(self) -> None:
        super().__init__()
    
    def run(self):
        self.Choose_Pokemon(1)  # No need to assign the return value
        self.Choose_Pokemon(2)  # No need to assign the return value

if __name__ == "__main__":
    os.system('cls')  # Clean terminal
    
    # Classes
    Game = Display()
    Game.run()
    
    print("Player 1 Pokémon:", Game.player1)
    print("Player 2 Pokémon:", Game.player2)
