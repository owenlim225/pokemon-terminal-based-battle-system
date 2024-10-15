class Status:
    def show_status_table():
        pass




class Backend(Status):
    def __init__(self) -> None:
        self.status = Status()



    def battle_preparation(self) -> None:
        pass


    def main_battle(self) -> None:
        pass


    ## requirements
    def post_battle_adjustments(self) -> None:
        pass

    

    # Show the battle scoreboard after the game
    def end_battle_program(self) -> None:
        self.show_status_table()






if __name__ == "__main__":
    Backend()