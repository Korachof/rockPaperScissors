import rps
from random import randint

def main():
    opening = "Hello. Welcome to Rock, Paper, Scissors, FIGHT. My name is Frank. I do not mean to scare you, but " \
                    "I am a Rock, Paper, Scissors champion. I believe I can beat you more than 50% of the time. Would " \
                    "you like to challenge me?"

    opening_answer = input("Please type YES if you would like to challenge me. Otherwise, please type NO. \n")

    if opening.upper() == "YES":
        user_name = input("Fantastic! I'm not going to go easy on you, though. First, what is your name? \n")

        user = rps.Player(user_name)

        "Nice to meet you, " + user.get_player_name()

        "Now that we are done with pleasantries, " + user.get_player_name() + \
            ", it's time to attack me! What is your weapon of choice?"

        user_move = input("Please type ROCK if you would like to wield rock, PAPER if you would like to wield paper, " \
                          "or SCISSORS if you would like to wield scissors")

        franks_move = user.gameOptionsHash[randint(0, 2)]

        user.battle_time(user_move, franks_move)




