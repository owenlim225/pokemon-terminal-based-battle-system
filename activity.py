#Limosnero, Sherwin P.
# J2S
# Machine Problem #1M

import os
import time

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
            print(f"[{count}] {pokemon[0]}", end="\t\t\t" if (count % 2 == 0) else "\n")
        # Ensure a newline after the last row if the number of Pokémon is odd
        if len(self.pokemons) % 2 != 0:
            print()
    
    
    
    
    # Choose three Pokémon
    def Choose_Pokemon(self, player_num):
        os.system('cls')  # Clean terminal
        
        chosen_pokemons = []
        
        # Maximum choices for both players
        max_choices = 4
        
        # Player [num] Choose Pokémon
        while True:
            print(f"\t\tPlayer {player_num}\n")
            self.pokemon_list_display()
            
            # If it's Player 1, prompt for their choices
            if player_num == 1:
                choices = list(map(int, input(f"\nChoose 1 to {max_choices} Pokémon: ").split()))
            else:
                # For Player 2, they must choose the same number as Player 1
                choices = list(map(int, input(f"\nYou must choose exactly {self.player1_choice_count} Pokémon: ").split()))
            
            # Validate the number of choices for Player 1
            if player_num == 1:
                if not (1 <= len(choices) <= max_choices):
                    print(f"Please choose between 1 and {max_choices} Pokémon.")
                    continue
            else:
                # Validate for Player 2 to ensure they pick the same number as Player 1
                if len(choices) != self.player1_choice_count:
                    print(f"Player 2 must choose exactly {self.player1_choice_count} Pokémon.")
                    continue
                
            if all(0 <= choice < len(self.pokemons) for choice in choices):
                chosen_pokemons = choices
                print(f"\nPlayer {player_num} has chosen: {', '.join(self.pokemons[i][0] for i in chosen_pokemons)}\n")
                
                # Add chosen Pokémon to the player list
                if player_num == 1:
                    self.player1.extend(self.pokemons[i] for i in chosen_pokemons)

                    # Store the number of Pokémon Player 1 has chosen for Player 2's turn
                    self.player1_choice_count = len(chosen_pokemons)
                    
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
        time.sleep(2)
        self.Choose_Pokemon(2)  # No need to assign the return value

if __name__ == "__main__":
    os.system('cls')  # Clean terminal
    
    # Classes
    Game = Display()
    Game.run()
    
    print("Player 1 Pokémon:", Game.player1)
    print("Player 2 Pokémon:", Game.player2)
