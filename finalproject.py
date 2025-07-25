import random

def welcome_message():
    print("="*30)
    print("Welcome to the Grade Calculator")
    print("="*30)

welcome_message()

# Function to run the multiplication guessing game
def multiplication_function():
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    correct_answer = num1 * num2
    
    # Print the structure of the equation
    print(f"\nWhat number multiplied by {num1} equals {correct_answer}?")
    
    # Keep asking until the user wants to quit or gets it right
    guess_correct = False
    while guess_correct == False:
        guess_input = input("Enter your guess: ")
        
        if guess_input.isdigit():
            guess = int(guess_input)
            
            if guess == num2:
                print(f"Great job! 🎉 {num1} * {num2} is indeed {correct_answer}.")
                guess_correct = True
            else:
                print("Oops! That's not correct. 😅 Try again.")
        else:
            print("Please enter a valid number!")

        if guess_correct == False:
            attempts = input("Do you want to try a new question? (yes to continue / no to quit): ").lower()
            if attempts == "no" or attempts == "n":
                return "quit"

# Main loop
keep_playing = "yes"
while keep_playing == "yes":
    result = multiplication_function()
    if result == "quit":
        print("\nThanks for playing! See you next time! 👋")
        keep_playing = "no"
