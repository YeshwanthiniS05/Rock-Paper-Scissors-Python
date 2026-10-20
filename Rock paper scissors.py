import random


def play_game():
    # Choices available in the game
    choices = ["rock", "paper", "scissors"]

    # Initializing scores
    user_score = 0
    computer_score = 0
    target_score = 10

    print("=============================================")
    print("Welcome to Rock, Paper, Scissors!")
    print(f"First player to reach {target_score} points wins the game!")
    print("=============================================")

    # Main game loop
    while user_score < target_score and computer_score < target_score:
        print(
            f"\nCurrent Score -> You: {user_score} | Computer: {computer_score}"
        )

        # Get and validate user input
        user_choice = (
            input("Enter your choice (rock, paper, scissors): ")
            .strip()
            .lower()
        )

        if user_choice not in choices:
            print("❌ Invalid input! Please type 'rock', 'paper', or 'scissors'.")
            continue

        # Get computer choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner of the round
        if user_choice == computer_choice:
            print("👔 It's a tie!")

        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "paper" and computer_choice == "rock")
            or (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("🎉 You win this round!")
            user_score += 1

        else:
            print("🤖 Computer wins this round!")
            computer_score += 1

    # Announce the final match winner
    print("\n=============================================")
    print("GAME OVER")
    print(f"Final Score -> You: {user_score} | Computer: {computer_score}")

    if user_score == target_score:
        print("🏆 Congratulations! You beat the computer and won the match!")
    else:
        print("💻 The computer wins the match! Better luck next time.")
    print("=============================================")


if __name__ == "__main__":
    play_game()
