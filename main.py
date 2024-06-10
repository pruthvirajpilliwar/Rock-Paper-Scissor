import random


def main():
    print("Welcome to Rock Paper Scissor Game\n")
    print("Please choose one of the following choice: ")
    print("""1. Rock
2. Paper
3. Scissor"""
    )
    user_choice = input("Enter your choice: ")

    choices = ["Rock", "Paper", "Scissor"]
    if user_choice not in choices:
        print("Please enter a valid choice")
        exit()

    print()
    comp_choice = random.choice(choices)

    if user_choice == comp_choice:
        print("Draw!")
    elif user_choice == "Rock" and comp_choice == "Paper":
        print("Computer Wins!")
    elif user_choice == "Rock" and comp_choice == "Scissor":
        print("User Wins!")
    elif user_choice == "Paper" and comp_choice == "Scissor":
        print("Computer Wins!")
    elif user_choice == "Paper" and comp_choice == "Rock":
        print("User Wins!")
    elif user_choice == "Scissor" and comp_choice == "Rock":
        print("Computer Wins!")
    elif user_choice == "Scissor" and comp_choice == "Paper":
        print("User Wins!")

    print(f"User: {user_choice} | Computer: {comp_choice}")


if __name__ == "__main__":
    main()
