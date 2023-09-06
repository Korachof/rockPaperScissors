import rps

def main():
    opening = "Hello. Welcome to Rock, Paper, Scissors, FIGHT. My name is Frank. I do not mean to scare you, but" \
                    "I am a Rock, Paper, Scissors champion. I believe I can beat you more than 50% of the time. Would" \
                    "you like to challenge me?"

    opening_answer = input("Please type YES if you would like to challenge me. Otherwise, please type NO. \n")

    if opening.upper() == "YES":
        user_name = input("Fantastic! I'm not going to go easy on you, though. First, what is your name? \n")

        rps.Player(user_name)

        "Nice to meet you, " + rps.Player.get_player_name()

        "Now that we are done with pleasantries, time to attack me! What is your weapon of choice?"

        user_move = input("Please type ROCK if you would like to wield rock, PAPER if you would like to wield paper, " \
                          "or SCISSORS if you would like to wield scissors")




        if user_move.upper() != "ROCK" or user_move.upper() != "PAPER" or user_move.upper() != "SCISSORS":




