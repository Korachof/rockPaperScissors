
class Player:
    def __init__(self, player_name):
        self._player_name = player_name
        gameOptionsHash = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}

    def get_player_name(self):
        """
        Get name for user
        :param None
        :return: self._player_name
        """

        return self._player_name

    def player_move(self, rps_choice):
        """
        Takes in the legal player move
        :param rps_choice: string
        :return: rps_choice
        """

        if rps_choice in gameOptionsHash.keys():
            return rps_choice

        #if player choice is not a legal move, ask again
        ask_again = input("Please type ROCK if you would like to wield rock, PAPER if you would like to wield paper, " \
                          "or SCISSORS if you would like to wield scissors \n")

        self.player_move(ask_again)

    def battle_time(self, player_choice, computer_choice):
        """
        Takes in player_choice and computer_choice and compares them to find a winner
        :param player_choice: String
        :param computer_choice: String
        :return: Binary: String (win/lose)
        """
        print("Your weapon of choice was " + player_choice)
        print("My weapon of choice was" + computer_choice)

        # player wins
        if self.gameOptionsHash[player_choice] == computer_choice:
            print("Wow! You beat me! You win!")
            return "Player Win"

        # computer wins
        elif self.gameOptionsHash[computer_choice] == player_choice:
            print("Just as expected. Thanks for trying, but I'm just that good.")
            return "Computer Win"

        # game is tied
        print("Ah. I see I have a worthy opponent. Looks like we have a stalemate on our hands.")
        return "Tie"









