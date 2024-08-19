import random

# Define Pokémon characters and their base powers
pokemon_char = {
    "Pikachu": 50,
    "Charmander": 55,
    "Bulbasaur": 60,
    "Squirtle": 58,
    "Jigglypuff": 45,
    "Eevee": 52,
    "Snorlax": 80,
    "Gengar": 70,
    "Machamp": 75,
    "Mewtwo": 90 
}

class Game:
    def __init__(self):
        self.user_power = 0
        self.battle_number = 0

    def display_intro(self):
        print("Welcome to the Pokémon Battle Simulator!")
        print("You will battle against a computer-generated Pokémon.")
        print("Choose your Pokémon wisely and see if you can win the battle!")
        print("Type 'x' to exit, 'c' to continue with the same Pokémon, or 'n' to choose a new Pokémon.")
        print()

    def choose_pokemon(self):
        print("Choose your Pokémon:")
        count = 0
        for key in pokemon_char:
            count += 1
            print(f"[{count}] {key}")
        print()
        
        try:
            user_choice = int(input("Your Pokémon (choose a number): "))
            if 1 <= user_choice <= len(pokemon_char):
                pokemon_list = list(pokemon_char.keys())
                selected_pokemon = pokemon_list[user_choice - 1]
                return selected_pokemon
            else:
                print("Invalid choice. Please select a valid number.")
                return self.choose_pokemon()
        except ValueError:
            print("Invalid input. Please enter a number.")
            return self.choose_pokemon()

    def computer_pokemon(self):
        pokemon_list = list(pokemon_char.keys())
        return random.choice(pokemon_list)
    
    def calculate_power(self, base_power):
        return base_power + random.randint(1, 100)
    
    def battle(self, user_pokemon, computer_pokemon):
        user_base_power = pokemon_char[user_pokemon]
        computer_base_power = pokemon_char[computer_pokemon]
        
        user_final_power = self.calculate_power(user_base_power)
        computer_final_power = self.calculate_power(computer_base_power)
        
        print(f"Battle {self.battle_number}:")
        print(f"User's Pokémon: {user_pokemon} - Power: {user_final_power}")
        print(f"Computer's Pokémon: {computer_pokemon} - Power: {computer_final_power}")
        
        if user_final_power > computer_final_power:
            self.user_power += computer_final_power
            print(f"Result: User Wins!")
        elif user_final_power < computer_final_power:
            print(f"Result: Computer Wins!")
        else:
            print(f"Result: Tie!")
        
        print(f"Updated User Power: {self.user_power}")
        print()

    def run(self):
        self.display_intro()
        continue_game = True

        while continue_game:
            if self.user_power == 0 or input("Would you like to select a new Pokémon? (n/c): ").lower() == 'n':
                user_pokemon = self.choose_pokemon()
            else:
                user_pokemon = self.user_pokemon
            
            computer_pokemon = self.computer_pokemon()
            self.battle(user_pokemon, computer_pokemon)
            self.user_pokemon = user_pokemon
            self.battle_number += 1
            
            user_input = input("Do you want to continue battling, choose a new Pokémon, or exit? (c/n/x): ").lower()
            if user_input == 'x':
                continue_game = False
                print("Thanks for playing! Goodbye!")
            elif user_input == 'n':
                continue
            elif user_input != 'c':
                print("Invalid input. Exiting the game.")
                continue_game = False

# Main program execution
if __name__ == "__main__":
    game_instance = Game()
    game_instance.run()
