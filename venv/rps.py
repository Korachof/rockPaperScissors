import randint

class Player:
    def __init__(self, player_name):
        self._player_name = player_name
        gameOptionsHash = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}


    def get_player_name(self):
        return self._player_name

    def player_move(self, rps_choice):
        if rps_choice in gameOptionsHash.keys():
            return rps_choice

        #if player choice is not a legal move, ask again
        ask_again = input("Please type ROCK if you would like to wield rock, PAPER if you would like to wield paper, " \
                          "or SCISSORS if you would like to wield scissors \n")

        self.player_move(ask_again)






# hashmap for player options and their corresponding


