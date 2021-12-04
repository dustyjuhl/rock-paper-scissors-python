from random import randint

# Iterate the user's score by one
def inc_score(score):
    score += 1
    return score

# Get the user's name
name = input("What's your name? ")
print("Let's start your game, "+name + "\n")

# Set each player's starting score
user_score = 0
computer_score = 0

# Use the For Loop to play for 3 rounds
for i in range(1,4):
    print("Choose the number next to your choice")
    print("1: Rock")
    print("2: Paper")
    print("3: Scissors")
    user_input = input("Select your choice: ")
    user_input = int(user_input)

# Use the random number generator to have the computer randomly select a number between 1 and 3 (inclusive)
computer_choice = randint(1,3)
winner = "";
# Use and if-elif block to make a decision about who the winner of the round inc_score
if computer_choice == 1:
	print("The computer chose rock")
	if user_input == 1:
		winner = "none"
	elif user_input == 2:
		winner = name
	elif user_input == 3:
		winner = "computer"	
elif computer_choice == 2:
	print("The computer chose paper")
	if user_input == 1:
		winner = name
	elif user_input == 2:
		winner = "none"
	elif user_input == 3:
		winner = "computer"
elif computer_choice == 3:
	print("The computer chose scissors")
	if user_input == 1:
		winner = name
	elif user_input == 2:
		winner = "computer"
	elif user_input == 3:
		winner = "none"
# Check if both players chose the same thing
if winner == "none":	
	print("It's a draw!")
	#Student will be able to call a function 
	user_score = inc_score(user_score)
	computer_score = inc_score(computer_score)
# Update the scores
elif winner == name:
	print("You win this round!")
	user_score = inc_score(user_score)
elif winner == "computer":
	print("The computer wins this round!")
	computer_score = inc_score(computer_score)
# Print out the current score for that round
	print("\nScore")
	print("------")
	print("You: " , user_score, "\nComputer: ",computer_score)
	print("\n")
if computer_score > user_score:
	print("Tough luck, the computer wins")
elif computer_score < user_score:
	print(name + " wins!")
elif computer_score == user_score:
	print("It's a tie!")
