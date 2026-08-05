import random

def play_rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'quit' whenever you are satisfied and want to exit the game.\n")
    score = {
        'user_wins': 0,
        'computer_wins': 0,
        'ties': 0,
    }

    #options for the game
    choices=['rock','paper','scissors']
    while True:
        user_choice=input("Write your choice : ").lower()

        # Check if the user wants to quit
        if user_choice == 'quit':
            print("Thanks for playing! Have a great day.")
            break

        # Ensure the user entered a valid choice
        if user_choice not in choices:
            print("That doesn't look like a valid choice. and unfortunately my love asked me to not take other choices...\n")
            continue

        computer_choice=random.choice(choices)
        print('You chose : ', user_choice)
        print('Computer chose : ', computer_choice)

        if user_choice == computer_choice:
            print("It's a tie!\n")
            score['ties'] += 1
        elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!\n")
            score['user_wins'] += 1
        else:
            print("Computer wins!\n")
            score['computer_wins'] += 1

    print("Final score:")
    print("  Your wins:", score['user_wins'])
    print("  Computer wins:", score['computer_wins'])
    print("  Ties:", score['ties'])

if __name__ == "__main__":
    play_rock_paper_scissors()