import random
import os


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
        self.battle_no = 0
        self.user_final_power = 0
        self.current_pokemon = []
        self.battle_results = []

        self.computer_final_power = 0

    # Working ✅
    def calculate_final_power(self, base_power):
        randVar = random.randint(1, 10) # mag bigay ng random num sa base_power ng pokemon
        calculated_power = base_power + randVar 
        return calculated_power, randVar

    
    # Working ✅
    def pokedex(self):
        os.system('cls') # Taga linis ng terminal
        print("----- Pokedex ----------")
        print("")
        print(f"Pokemon\t\t Base power")
        for count, (key, value) in enumerate(pokemon_char.items(), start=1):
            print(f"[{count}] {key}\t:   {value}")

        print("\n\nPress any key to return")
        print("")
        print("-------------------------")


    # Working ✅
    def computer_pokemon(self): # pokemon ng bot kalaban
        pokemon_list = list(pokemon_char.keys())
        computer_pokemon = random.choice(pokemon_list)

        computer_current_pokemon = computer_pokemon
        computer_final_power, randVar = self.calculate_final_power(pokemon_char[computer_pokemon])


        print(f"Computer choose: {computer_pokemon}")

        computer_pokemon_base_power = pokemon_char[computer_pokemon]
        print(f"\n\nComputer power: {computer_pokemon} base power + {randVar} blessings")
        print(f"Computer Final power: {computer_final_power}")
        
        self.battle(self.user_final_power, computer_final_power, computer_current_pokemon)
        return computer_final_power, computer_current_pokemon, computer_pokemon_base_power
        
    

    # Working ✅
    def select_user_pokemon(self):
        os.system('cls') # Taga linis ng terminal
        print("----- Pokemon Selection ----------")
        print("")
        print("Choose your pokemon\n")

        for count, key in enumerate(pokemon_char.keys(), start=1):
            print(f"[{count}]\t {key}")

        print("")
        print("-------------------------")
        
        # Papiliin user to choose pokemon of choice
        try:
            user_choice = int(input("\nYour Pokemon: ")) 

            # Working ✅
            if 1 <= user_choice <= len(pokemon_char):
                pokemon_list = list(pokemon_char.keys())
                user = pokemon_list[user_choice - 1] # return equivalent num na pinili ng user as pokemon
                print(f"\nYou choose: {user}")

                user_pokemon = pokemon_char[user]  
                self.current_pokemon = user


                user_final_power, randVar = self.calculate_final_power(user_pokemon)
                self.user_final_power = user_final_power

                print(f"\nYour power: {user_pokemon} base power + {randVar} blessings")
                print(f"Your Final power: {user_final_power}\n")

                self.computer_pokemon()

                return user_pokemon, user_final_power

            # Working ✅
            else:
                os.system('cls') # Taga linis ng terminal
                print("\nNo pokemon found.\n") # pag wala sa pamimilian na int pinili ng user
                return self.select_user_pokemon()

        # Working ✅    
        except ValueError:
            os.system('cls') # Taga linis ng terminal
            print("\nInvalid input. Please enter a number.") # balik mula simula pag input mali hindi int
            return self.select_user_pokemon()
        
        



    # Working ✅
    def battle(self, user_final_power, computer_final_power, computer_current_pokemon):
        self.battle_no += 1

        

    
        
        print(f"------------------- Battle {self.battle_no}  -------------------")
        print("User\t\t\tComputer")
        print(f"self.current_pokemon \tvs\t{computer_current_pokemon}")

        if self.user_final_power >= 100 or self.battle_no >= 5: # PANG PA BALANCEEEEEEEEEE
            computer_final_power += self.user_final_power // 4
        elif self.user_final_power >= 500 and self.battle_no >= 5: # PANG PA BALANCEEEEEEEEEE
            computer_final_power += self.user_final_power //2


        print(f"{user_final_power}\t\t{computer_final_power}")

        
        


        # SINO PANALO EWAN
        if user_final_power > computer_final_power:  # User wins
            result = "User"
            print(f"\t\t      You win!\n")
            print("--------------------------------------------------")
            print("")
            print(f"Your pokemon gained {computer_final_power} power")
            print(f"Current final power: {user_final_power + computer_final_power}\n")
            print("")
            print("--------------------------------------------------")
            user_final_power += computer_final_power
            self.user_final_power = user_final_power

        elif user_final_power < computer_final_power:  # User loses
            result = "CPU"
            print(f"\t\t   You Lose.\n")
            print("--------------------------------------------------")
            print("")
            print(f"Your pokemon lost {user_final_power} power")
            print(f"Computer current final power: {computer_final_power}\n")
            print("")
            print("--------------------------------------------------")
            self.user_final_power = 0
            computer_final_power += user_final_power

        else:  # Tie
            result = "-"
            print(f"\t\t\tIt's a Tie.\n")  # It's a tie
            print("--------------------------------------------------")
            print("")
            print(f"Your power remains")
            print("")
            print("--------------------------------------------------")

        # Record the battle result (using the original values before updates)
        self.battle_results.append((self.battle_no, user_final_power, computer_final_power, result))
        self.run()

     # Working ✅
    def battle_records(self):
        os.system('cls')  # Clear the terminal
        print("----- Battle records ----------")
        print("")
        print("")

        if not self.battle_results:
            print("You don't have any battle records.")

        else:
            print("Battle\tUser Power   Computer Power\tWinner")

            for result in self.battle_results:
                print(f" [{str(result[0])}] \t    {str(result[1])}\t\t   {str(result[2])} \t\t {result[3]}")
        print("")
        print("-------------------------")

    # Working ✅    
    def intro(self):
        print("\t\tWelcome to pokemon battle!\n\nA terminal based battle system made by Sherwin P. Limosnero from J2S.\n")
        print("For new players, choose a button to input then press enter.")

        self.run()

    # Working ✅
    def status(self):
        os.system('cls') # Taga linis ng terminal

        if not self.current_pokemon:
            self.current_pokemon = None
        else:
            pass
        
        print(f"""
----- Player Status ----------
              
    Battle \t\t:  {self.battle_no}
    Current Pokemon\t:  {self.current_pokemon}
    Current Power\t:  {self.user_final_power}
    
              
-------------------------

    Press any key to return

""")


    # Working ✅    
    def run(self):
        print("""
----- Buttons ----------
    
    [C] Continue    
    [N] New Pokemon
                        
    [P] Pokedex
    [S] Status    
    [B] Battle Records
                           
    [X] Exit
              
-------------------------
""")
        while True:
            user_input = input().lower()

            if user_input == "c":
                if self.current_pokemon:
                    computer_final_power, computer_current_pokemon = self.computer_pokemon()
                    self.battle(self.user_final_power, computer_final_power, computer_current_pokemon)
                else:
                    print("\nPlease choose your pokemon first.\n")
            
            elif user_input == "n":
                self.select_user_pokemon()
            
            elif user_input == "p":
                self.pokedex()

            elif user_input == "s":
                self.status()
                
            elif user_input == "b":
                self.battle_records()

            elif user_input == "x":
                print("Thank you for playing")
                break
            else:
                print("\nInvalid input.")
                os.system('cls') # Taga linis ng terminal
                self.run()
                


        







    
        

if __name__ == "__main__":
    _Game = Game()

    os.system('cls') # Taga linis ng terminal
    _Game.intro()