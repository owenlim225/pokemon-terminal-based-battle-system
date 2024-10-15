
# ========Install module if not available============

import packages
packages.initialize_packages()

# ====================================================

import backend as BE
import frontend as FE
import time
import os

class Gameplay:
    def __init__(self) -> None:
        # Initialize Backend and Frontend Managers
        self.backend = BE.Backend()
        self.frontend = FE.Frontend()
        
        # Flag to track if all Pokemons are used in battle
        self.all_pokemons_used = False

        # Start the program
        self.main()

    def clear_screen(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
     
    def main(self) -> None:
        # Select pokemon for the two players
        self.pokemon_array_selection()
        
        # Battle loop
        while not self.all_pokemons_used:
            self.all_pokemons_used = self.battle_pokemon_selection()

            if self.all_pokemons_used:
                self.clear_screen()
                
            # Battle function sequence
            self.backend.poison_or_potion()
            self.backend.main_battle()
            self.backend.post_battle_adjustments()
        
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



    def battle_pokemon_selection(self) -> bool:
        pass





if __name__ == "__main__":
    game = Gameplay()
    game.main()  


