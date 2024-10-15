
# ========Install module if not available============

import packages
packages.initialize_packages()

# ====================================================

import backend as BE
from backend import GameData
import frontend as FE
import time
import os

class Gameplay:
    def __init__(self) -> None:
        # Initialize Backend and Frontend Managers
        self.backend = BE.Backend()
        self.frontend = FE.Frontend()
        self.game_data = GameData()

        # Flag to track if all Pokemons are used in battle
        self.all_pokemons_used = False



    def clear_screen(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')



    def run(self) -> None:
        # Select pokemon for the two players
        self.pokemon_array_selection()

        # Battle loop
        while not self.all_pokemons_used:
            try:
                # Select and battle until all Pokemons are used
                self.all_pokemons_used = self.battle_pokemon_selection()

                if self.all_pokemons_used:
                    self.clear_screen()

                # Battle function sequence
                player1 = self.game_data.players[1]
                player2 = self.game_data.players[2]
                
                self.battle_preparation()
                self.backend.main_battle()
                self.backend.post_battle_adjustments(player1, player2)

            except Exception as e:
                print(f"An error occurred: {e}")    
                break

        self.backend.end_battle_program()
        print("Program Ended")




    # Select pokemon array for the two players
    def pokemon_array_selection(self) -> None:
        self.frontend.display_program_info()
        count = 0

        while count != 2:
            try: 
                # Call the method to get the Pokemon info
                self.frontend.display_pokemon_selection_table(self.backend.get_pokemon_info())
                
                # Handle Pokemon selection for the current player
                selection_error = self.backend.pokemon_array_selection(count)

                # Add delay if there's a selection error
                if selection_error: 
                    time.sleep(1)
                    self.clear_screen()
                    continue

                # Increment count and clear screen after successful selection
                count += 1
                self.clear_screen()

            except ValueError:
                print("Invalid Input. Please Try Again!")
                time.sleep(1)
                self.clear_screen()


    def battle_preparation(self) -> None:
        # ==================================
        # Battle Preparation where the players
        # can decide whether they can use
        # poison or postion
        # ==================================
        count = 0
        while count != 2:
            try:
                # Access players' battle_pokemon based on count
                if count == 0:
                    player_battle_pokemon = self.game_data.players[1].battle_pokemon  # Player 1's battle Pokémon
                    self.frontend.poison_or_potion(player_battle_pokemon)
                elif count == 1:
                    player_battle_pokemon = self.game_data.players[2].battle_pokemon  # Player 2's battle Pokémon
                    self.frontend.poison_or_potion(player_battle_pokemon)

                # Handle battle preparation for each player
                selection_Errors = self.game_Manager.BattlePreparation(count)
                
                # Check IndexError for user input selections
                if selection_Errors: 
                    time.sleep(1)
                    self.clear_screen()
                    continue    
                count += 1
                
                self.clear_screen()
                
            except ValueError:
                print("Invald Input. Please Try Again!")
                time.sleep(1)
                self.clear_screen()
                continue
        else:
            print("{:<15}{:>0}".format(
                "",
                "🔥 Entering Battle Stage 🔥\n"
            ))
            time.sleep(1)





    def battle_pokemon_selection(self) -> bool:
        pass





if __name__ == "__main__":
    game = Gameplay()
    game.run()  


