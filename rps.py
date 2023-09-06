from datetime import date


class Player:
    def __init__(self, player_name):
        self._player_name = player_name

    def get_player_name(self):
        """
        Get name for user
        :param None
        :return: self._player_name
        """
        return self._player_name

    def get_game_options(self):
        """
        Get game options hash
        :return: hash
        """
        return {"ROCK": "SCISSORS", "SCISSORS": "PAPER", "PAPER": "ROCK"}

    def battle_time(self, player_choice, computer_choice):
        """
        Takes in player_choice and computer_choice and compares them to find a winner
        :param player_choice: String
        :param computer_choice: String
        :return: Binary: String (win/lose)
        """
        print("Your weapon of choice was " + player_choice.upper())
        print("My weapon of choice was " + computer_choice)

        # player wins
        if self.get_game_options()[player_choice] == computer_choice:
            print("Wow! You beat me! You win!")
            return "Player Win"

        # computer wins
        elif self.get_game_options()[computer_choice] == player_choice:
            print("Just as expected. Thanks for trying, but I'm just that good.")
            return "Computer Win"

        # game is tied
        print("Ah. I see I have a worthy opponent. Looks like we have a stalemate on our hands.")
        return "Tie"

    def results_data(self, user, result):
        """
        Takes in the user's name and the result of the rps match and appends the result to a
            text file
        :param user: String (user name)
        :param result: String (Player Win, Computer Win, or Tie)
        :return: None
        """
        today = date.today()
        with open(user + "_" + "rps_results.txt", "a") as f:
            f.write(str(today.month) + "/" + str(today.day) + "/" + str(today.year) + ": " + result + "\n")









