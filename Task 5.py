import random

def determine_winner(player, comp):
    if player == comp: return "🤝 It's a tie!"
    elif (player == "rock" and comp == "scissors") or \
         (player == "scissors" and comp == "paper") or \
         (player == "paper" and comp == "rock"):
        return "🏆 You win!"
    else:
        return "💻 Computer wins!"

def play_game():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user = input("Choose rock/paper/scissors: ").lower()
        if user not in choices:
            print("Invalid move.")
            continue
        comp = random.choice(choices)
        print(f"Computer chose: {comp}")
        print(determine_winner(user, comp))
        again = input("Play again? (yes/no): ").lower()
        if again != 'yes':
            print("Thanks for playing!")
            break

play_game()
