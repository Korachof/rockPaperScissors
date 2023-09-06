import rps
import random


def main():
    print("Hello. Welcome to Rock, Paper, Scissors, FIGHT. My name is Frank. I do not mean to scare you, but " \
          "I am a Rock, Paper, Scissors champion. I believe I can beat you more than 50% of the time. Would " \
          "you like to challenge me?")

    opening_answer = input("Please type YES if you would like to challenge me. Otherwise, please type NO. \n")

    if opening_answer.upper() == "YES":
        user_name = input("Fantastic! I'm not going to go easy on you, though. First, what is your name? \n")

        user = rps.Player(user_name)

        print("Nice to meet you, " + user.get_player_name())

        print("Now that we are done with pleasantries, " + user.get_player_name() +
              ", it's time to attack me! What is your weapon of choice? \n")

        def make_moves():
            user_move = input("Please type ROCK if you would like to wield rock, PAPER if you would like to wield "
                              "paper, or SCISSORS if you would like to wield scissors \n")

            franks_move = random.choice(["ROCK", "PAPER", "SCISSORS"])

            user.results_data(user_name.lower(), user.battle_time(user_move.upper(), franks_move))

            replay = input("Would you like to try again? Type YES if you would like to continue. Type NO if not. \n")
            return replay

        play_time = make_moves()

        while play_time.upper() != "NO" and play_time.upper() != "YES":
            input("Would you like to try again? Type YES if you would like to continue."
                  " Type NO if not. \n")

        if play_time.upper() == "NO":
            exit()

        while play_time.upper() == "YES":
            play_time = make_moves()


main()
