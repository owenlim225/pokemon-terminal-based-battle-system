
# ========Install module if not available============

import packages
packages.initialize_packages()

# ====================================================

import backend as BE
import frontend as FE
import time


class Gameplay:
    def __init__(self) -> None:
        # Initialize Backend and Frontend Managers
        self.backend = BE.Backend()
        self.frontend = FE.Frontend()
        
        # Flag to track if all Pokemons are used in battle
        self.all_pokemons_used = False
     
    def main(self):
        # Main gameplay logic
        pass

if __name__ == "__main__":
    game = Gameplay()
    game.main()  


