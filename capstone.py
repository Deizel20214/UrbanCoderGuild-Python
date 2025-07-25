import random

def welcome_message():
    print("="*30) 
    print("Welcome to the Grade calculator") 
    print("="*30)

import random

def welcome_message():
    print("="*30)
    print("Welcome to the Grade calculator")
    print("="*30)

welcome_message()

# Function to run the multiplication guessing game
def multiplication_function(max_attempts=3):
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    correct_answer = num1 * num2
    
    # Print the structure of the equation
    print(f"What times {num1} gives you {correct_answer}?")
    
    # Initialize attempts to 0
    attempts = 0

    # Allow the user to guess for a limited number of attempts
    while attempts < max_attempts:
        # Ask the user to guess the second number (num2)
        guess = int(input("Jamal, come up here and solve this division 😏: "))
        attempts += 1
        
        # Check if the guess is correct
        if guess == num2:
            print(f"Great job Jamal!! 😁 {num1} * {num2} is {correct_answer}.")
            break
        else:
            print(f"Wrong answer! You have failed. Get out of my classroom right now!!! 😡 {max_attempts - attempts} attempts left.")
    
    # If the user runs out of attempts
    if attempts == max_attempts and guess != num2:
        print(f"You are out of attempts! Stop skipping school!!!!! 💀 The correct answer was {num2}.")

# Call and run the game
multiplication_function(max_attempts=3)
