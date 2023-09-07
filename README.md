# rockPaperScissors
A simple rock paper scissors game that allows a player to play against a computer opponent. 

Built using Python Object-Oriented Programming. 

Features:

- Offers dialogue from a computer opponent named Frank. 

- Allows the user to choose between the three traditional options in rock, paper, scissors, 
and compares them to Frank's, which are determined by random choice(). 

- Determines a winner by using a dictionary (hash) to compare key/value pairs. 

- Appends the outcome information to a user specific text document to record scores, which
is named using the user name. 

- Multiple players can play and have separate recorded results, assuming they have different
usernames

- Offers the player a game play loop to retry the game and play Frank again without
going through initial dialogue.

Possible Future Features: 

- Add a conditional to check if a text document already exists with the user's name. If
so, prompt them to either continue or create a new username. 

- Add the choice to play a more complex rock paper scissors with more options. 

- Give Frank more functionality than just "random." Could take the user's last result (or
more) and use that history to determine future moves. 
