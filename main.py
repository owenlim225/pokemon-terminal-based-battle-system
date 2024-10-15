
# ========Install module if not available============

# import packages
# packages.initialize_packages()

# ====================================================

from backend import Backend, GameData
from frontend import Frontend
import time
import os

class Gameplay:
    def __init__(self) -> None:
        # Initialize Backend and Frontend Managers
        self.backend = Backend()
        self.frontend = Frontend()
        self.game_data = GameData()

        # Flag to track if all Pokemons are used in battle
        self.all_pokemons_used = False



    def clear_screen(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')



    def pokemon_array_selection(self) -> None:
        count = 0
        while count != 2:
            try:
                # Get Pokémon info and display the table
                pokemon_info = self.backend.get_pokemon_info()
                self.frontend.display_pokemon_selection_table(pokemon_info)

                # Prompt player for selection input (ensure proper validation)
                user_input = input(f"Player {count + 1}, select a Pokémon by entering the index: ").strip()

                # Validate input is a digit
                if not user_input.isdigit():
                    print("Invalid Input. Please enter a valid number.")
                    time.sleep(1)
                    continue  # Re-prompt if the input is not valid

                selection = int(user_input)

                # Call backend method for selecting Pokémon
                selection_error = self.backend.pokemon_array_selection(count, selection)

                if selection_error:
                    print("Selection Error. Please try again.")
                    time.sleep(1)
                    continue  # Re-prompt if there was an error in selection

                count += 1  # Move to the next player after a successful selection
                time.sleep(1)

            except ValueError as e:
                print(f"An error occurred: {e}. Please Try Again!")
                time.sleep(1)

    def run(self) -> None:
        # Step 1: Show the layout and program info
        self.frontend.display_program_info()

        # Step 2: Select Pokémon for both players
        self.pokemon_array_selection()

        # Step 3: Start the battle loop
        while not self.all_pokemons_used:
            try:
                self.all_pokemons_used = self.battle_pokemon_selection()

                if self.all_pokemons_used:
                    self.clear_screen()

                player1 = self.game_data.players[1]
                player2 = self.game_data.players[2]

                self.battle_preparation()
                self.backend.main_battle()
                self.backend.post_battle_adjustments()

            except Exception as e:
                print(f"An error occurred: {e}")
                break

        self.backend.end_battle_program()
        print("Program Ended")
    
    def pokemon_array_selection(self) -> None:
        count = 0
        while count != 2:
            try:
                # Get Pokémon info and display the table in the layout's upper part
                pokemon_info = self.backend.get_pokemon_info()
                self.frontend.display_pokemon_selection_table(pokemon_info)

                # Prompt player for selection input (add clear instruction)
                user_input = input(f"Player {count + 1}, select a Pokémon by entering the index: ").strip()

                # Check if the input is a digit (valid number for selection)
                if not user_input.isdigit():
                    print("Invalid Input. Please enter a valid number.")
                    time.sleep(1)
                    continue  # Re-prompt if the input is not a valid number

                # Convert input to integer for selection processing
                selection = int(user_input)

                # Handle Pokémon selection for the current player
                selection_error = self.backend.pokemon_array_selection(count, selection)

                if selection_error:
                    print("Selection Error. Please try again.")
                    time.sleep(1)
                    continue  # Re-prompt if there was an error in selection

                # Increment count after successful selection
                count += 1
                time.sleep(1)

            except ValueError:
                print("Invalid Input. Please Try Again!")
                time.sleep(1)



    def battle_preparation(self) -> None:
        count = 0
        while count != 2:
            try:
                # Player 1 and Player 2 battle preparation
                player_battle_pokemon = self.game_data.players[count + 1].battle_pokemon
                self.frontend.poison_or_potion(player_battle_pokemon)

                # Handle battle preparation for each player
                selection_errors = self.backend.BattlePreparation(count)

                if selection_errors:
                    print("Battle Preparation Error. Please try again.")
                    time.sleep(1)
                    self.clear_screen()
                    continue

                count += 1
                self.clear_screen()

            except ValueError:
                print("Invalid Input. Please Try Again!")
                time.sleep(1)
                self.clear_screen()

        print("{:<15}{:>0}".format("", "🔥 Entering Battle Stage 🔥\n"))
        time.sleep(1)




    def battle_pokemon_selection(self) -> bool:
        pass





if __name__ == "__main__":
    game = Gameplay()
    game.run()  


