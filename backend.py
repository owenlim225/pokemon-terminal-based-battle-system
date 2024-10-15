import time
import random

# =========== Player Data =========== 
class Player:
    def __init__(self):
        self.selected_pokemon = []
        self.battle_pokemon = []
        self.previous_power = None
        self.power_increase = []
        self.power_decrease = []
        self.previous_health = None
        self.unused_count = 0
# ====================================









# ====================================

class GameData:
    def __init__(self):
        # Store player data in a dictionary for easier access
        self.players = {
            1: Player(),  # Player 1
            2: Player()   # Player 2
        }

        # Other game-related variables
        self.battle_number = 0
        self.battle_winner = ""
        self.all_pokemon_is_selected = False
        self.pokemon_array = []

    # =======================================
    # Helper Methods for Setting Values
    # =======================================
    def set_selected_pokemons_to_null(self):
        """Reset selected Pokémon for both players."""
        for player in self.players.values():
            player.selected_pokemon = []

    def set_changed_pokemon_power_to_null(self):
        """Reset power increases and decreases for both players."""
        for player in self.players.values():
            player.power_increase = []
            player.power_decrease = []

    def reset_all_values(self):
        """Reset all values for a new battle."""
        self.battle_winner = ""
        self.all_pokemon_is_selected = False
        for player in self.players.values():
            player.unused_count = 0
            player.previous_health = None
            player.previous_power = None

    # ==================================
    # Methods for Accessing Player Data
    # ==================================
    def get_selected_pokemon(self, player_id: int) -> list:
        return self.players[player_id].selected_pokemon

    def get_battle_pokemon(self, player_id: int) -> list:
        return self.players[player_id].battle_pokemon

    def get_previous_power(self, player_id: int) -> int:
        return self.players[player_id].previous_power

    def get_power_increase(self, player_id: int) -> list:
        return self.players[player_id].power_increase

    def get_power_decrease(self, player_id: int) -> list:
        return self.players[player_id].power_decrease

    def get_unused_count(self, player_id: int) -> int:
        return self.players[player_id].unused_count

    def get_previous_health(self, player_id: int) -> int:
        return self.players[player_id].previous_health

    # ==================================
    # Battle-related Methods
    # ==================================
    @property
    def get_battle_number(self) -> int:
        return self.battle_number

    @get_battle_number.setter
    def set_battle_number(self, value: int) -> None:
        if value < 0:
            raise ValueError("Battle number cannot be negative.")
        self.battle_number = value

    @property
    def get_battle_winner(self) -> str:
        return self.battle_winner

    @property
    def is_all_pokemon_selected(self) -> bool:
        return self.all_pokemon_is_selected

# ===================================










# ====== All available pokemon players can choose from ====== 
class PokemonData:
    def __init__(self) -> None:
        self.pokemon_data = [
            # [Name, Health, Power, is_used]
            ["Pikachu",     100, 55, False],
            ["Charmander",  100, 60, False],
            ["Bulbasaur",   100, 50, False],
            ["Squirtle",    100, 65, False],
            ["Jigglypuff",  100, 45, False],
            ["Eevee",       100, 70, False],
            ["Snorlax",     100, 98, False],
            ["Gengar",      100, 75, False],
            ["Machamp",     100, 80, False],
            ["Mewtwo",      100, 99, False]
        ]

    def get_pokemon_array(self) -> list:
        return self.pokemon_data
# ============================================================










# ====== Status manager that handles battle data ======
class Status:
    def show_status_table(self) -> None:
        pass




# ==================================================









# ============== Collection of funcs that runs the game ==============
class Backend:
    def __init__(self) -> None:
        self.status = Status()
        self.pokemon_data = PokemonData()
        self.pokemon_array = self.pokemon_data.get_pokemon_array()

        


    def get_pokemon_info(self) -> None:
        return self.pokemon_array

    #===========Battle related funcs===========

    def poison_or_potion(self, user_input) -> None:
        # Display roulette effect (simulating a rolling effect)
        print("Roulette spinning...")
        time.sleep(3)  # Simulating delay for effect

        # Define possible outcomes
        outcomes = ["poison", "potion"]
        result = random.choice(outcomes)

        # Calculate the effect based on the outcome
        if result == "poison":
            effect_value = -random.randint(1, 5) * user_input
            print(f"Unlucky! You got poisoned. Your power is reduced by {abs(effect_value)}.")
        elif result == "potion":
            effect_value = random.randint(1, 5) * user_input
            print(f"Lucky! You got a potion. Your health is increased by {effect_value}.")

        # Return the effect value (if needed for further processing)
        return effect_value





    def main_battle(self) -> None:
        pass


    ## requirements
    def post_battle_adjustments(self) -> None:
        pass

    #===========================================

    # Show the battle scoreboard after the game
    def end_battle_program(self) -> None:
        self.status.show_status_table()






if __name__ == "__main__":
    Backend()