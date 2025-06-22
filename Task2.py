import random

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    secret = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1
            if guess < secret:
                print("🔻 Too low!")
            elif guess > secret:
                print("🔺 Too high!")
            else:
                print(f"✅ Correct! You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

number_guessing_game()
