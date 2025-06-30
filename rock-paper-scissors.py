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

# Play 3 rounds
for i in range(1,4):
    print(f"Round {i}")
    print("Choose the number next to your choice")
    print("1: Rock")
    print("2: Paper")
    print("3: Scissors")
    while True:
	user_input = input("Select your choice: ")
	try:
	    user_choice = int(user_input)
	    if user_choice in [1,2,3]:
		break
	    else:
		print{"Invalid choice. Please enter a number between 1 and 3.")
	except ValueError: 
	    print("Invalid input. Please enter a valid number.")

    # Use the random number generator to have the computer randomly select a number between 1 and 3 (inclusive)
    computer_choice = randint(1,3)
    if computer_choice == 1:
        print("The computer chose rock")
    elif computer_choice == 2:
        print("The computer chose paper")
    else:
        print("The computer chose scissors")    	    
    winner = ""
    # 1 beats 3, 2 beats 1, 3 beats 2
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print("You win this round!")
        user_score = inc_score(user_score)
    else:
        print("The computer wins this round!")
        computer_score = inc_score(computer_score)
        
    print("\nScore")
    print("------")
    print(f"You: {user_score} \nComputer: {computer_score}\n")

if computer_score > user_score:
    print("Tough luck, the computer wins the game")
elif computer_score < user_score:
    print(f"{name} wins the game!")
else:
    print("It's a tie game!")
