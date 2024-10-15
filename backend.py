# ====== All available pokemon players can choose from ====== 
class PokemonData:
    def __init__(self) -> None:
        self.pokemon_data = [
            # [Name, Health, Power, is_used]
            ["Pikachu",     100, 55, 0, 0, False],
            ["Charmander",  100, 60, 0, 0, False],
            ["Bulbasaur",   100, 50, 0, 0, False],
            ["Squirtle",    100, 65, 0, 0, False],
            ["Jigglypuff",  100, 45, 0, 0, False],
            ["Eevee",       100, 70, 0, 0, False],
            ["Snorlax",     100, 98, 0, 0, False],
            ["Gengar",      100, 75, 0, 0, False],
            ["Machamp",     100, 80, 0, 0, False],
            ["Mewtwo",      100, 99, 0, 0, False]
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
        pass 

    #===========Battle related funcs===========

    def battle_preparation(self) -> None:
        pass


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