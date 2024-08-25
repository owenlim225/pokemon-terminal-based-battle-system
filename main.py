import random

pokemon_char = {
    "Mewtwo": 90,
    "Snorlax": 80,
    "Machamp": 75,
    "Gengar": 70,
    "Bulbasaur": 60,
    "Squirtle": 58,
    "Charmander": 55,
    "Eevee": 52,
    "Pikachu": 50,
    "Jigglypuff": 45,
}

class Game:
    def __init__(self):
        self.user_power = 0
        self.battle = 0
        self.pokemon = []
    
    def intro(self):
        print("Pokemon Battle\n")
        self.user_pokemon()

    
    def user_pokemon(self):

        # Display mga pokemon for user to choose one to battle
        count = 0
        for key in pokemon_char:
            count += 1
            print(f"[{count}] {key}", end="\n" if count % 2 == 0 else "\t     ") # organize display sa terminal
        print()

        # Papiliin user to choose pokemon of choice
        try:
            user_choice = int(input("Your Pokemon: ")) 

            if 1 <= user_choice <= len(pokemon_char):
                pokemon_list = list(pokemon_char.keys())
                return pokemon_list[user_choice - 1] # return equivalent num na pinili ng user as pokemon

            else:
                print("No pokemon found.") # pag wala sa pamimilian na int pinili ng user
                return self.user_pokemon()
            
        except ValueError:
            print("Invalid input. Please enter a number.") # balik mula simula pag input mali hindi int
            return self.user_pokemon()
        
    
    def bot_pokemon(self): # pokemon ng bot kalaban
        pokemon_list = list(pokemon_char.keys())
        return random.choice(pokemon_list) # mag return ng kahit anong pokemon mula sa pokemon char dict    


    def calculate_power(self, base_power):
        return base_power + random.randint(1, 100) # mag bigay ng random num sa base_power ng pokemon
    
    def battle(self, user_pokemon, bot_pokemon):
        user_base_power = pokemon_char[user_pokemon]
        bot_base_power = pokemon_char[bot_pokemon]

        # inherited value mula sa dalawang func
        user_final_power = self.calculate_power(user_base_power) 
        bot_final_power = self.calculate_power(bot_base_power)







    def run(self):
        self.intro()
        in_game = True
        
        while in_game:
            if self.user_power == 0 or input("Would you like to select a new Pokémon? (n/c): ").lower() == 'n':
                user_pokemon = self.user_pokemon()
            else:
                user_pokemon = self.user_pokemon
                
            bot_pokemon = self.bot_pokemon()
            self.battle(user_pokemon, bot_pokemon)
            self.user_pokemon = user_pokemon
            self.battle_number += 1
            








# Execute yung main program
if __name__ == "__main__":
    game_instance = Game()
    game_instance.run()




