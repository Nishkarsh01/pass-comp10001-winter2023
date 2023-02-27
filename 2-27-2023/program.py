import random

# Define the options for the game
option1 = "rock"
option2 = "paper"
option3 = "scissors"

# Define a function to play the game
def play_game():
    # Ask the user for their choice
    user_choice = input("Enter 'rock', 'paper', or 'scissors': ")
    # Make sure the user's choice is valid
    while user_choice != option1 and user_choice != option2 and user_choice != option3:
        user_choice = input("Invalid choice. Enter 'rock', 'paper', or 'scissors': ")
    # Generate a random choice for the computer
    computer_choice = random.choice((option1, option2, option3))
    # Determine the winner
    if user_choice == computer_choice:
        result = 'tie'
    elif (user_choice == option1 and computer_choice == option3) or (user_choice == option2 and computer_choice == option1) or (user_choice == option3 and computer_choice == option2):
        result = 'win'
    else:
        result = 'lose'
    # Display the results
    print(f"You chose {user_choice}. The computer chose {computer_choice}. You {result}!")

# Call the play_game function to play the game
play_game()
