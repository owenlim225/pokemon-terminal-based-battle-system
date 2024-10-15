
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


     
    def main(self) -> None:
        # Select pokemon for the two players
        self.pokemon_array_selection()
        
        # Battle loop
        while not self.all_pokemons_used:
            self.all_pokemons_used = self.battle_pokemon_selection()

            if self.all_pokemons_used:
                os.system('cls') # Clear terminal
                
            # Battle function sequence
            self.backend.battle_preparation()
            self.backend.main_battle()
            self.backend.post_battle_adjustments()
        
        self.backend.end_battle_program()
        print("Program Ended")


    # Select pokemon array for the two players
    def pokemon_array_selection(self) -> None:
        self.frontend.display_program_info()
        









if __name__ == "__main__":
    game = Gameplay()
    game.main()  


