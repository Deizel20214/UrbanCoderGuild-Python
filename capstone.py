import random

def welcome_message():
    print("="*30) 
    print("Welcome to the Grade calculator") 
    print("="*30)


# Function to run the multiplication guessing game
def multiplication_function(max_attempts=3):
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    
    correct_answer = num1 * num2
    
    # Print "What times what gives you the answer?"
    print(f"What times what gives you {correct_answer}?")
    
    # Make attempt = 0
    attempts = 0

    # Allow the user to guess for 3 number of attempts
    while attempts < max_attempts:
        # Ask the user for their guess number
        guess_1 = int(input("jamal come up here and solve this division😏: "))


# Function to run the multiplication guessing game
def multiplication_function(max_attempts=3):
    # Generate a random number for the left side of the problem
    num1 = random.randint(1, 10)
    
    # Generate the correct answer by multiplying num1 by another random number
    num2 = random.randint(1, 10)
    correct_answer = num1 * num2
    
    # Print the structure of the equation
    print(f"What times {num1} gives you {correct_answer}?")
    
    # Initialize attempts to 0
    attempts = 0

    # Allow the user to guess for a limited number of attempts
    while attempts < max_attempts:
        # Ask the user to guess the second number (num2)
        guess = int(input(" somone else go answer  the second equation: "))
        attempts += 1
        
        # Check if the guess is correct
        if guess == num2:
            print(f"great job jamal!!😁 {num1} * {num2} is {correct_answer}.")
            break
        else:
            print(f"wrong answer you have failed get out of my class room right now!!!😡 {max_attempts - attempts} attempts left.")
    
    # If statement for whe user runs out of attempts
    if attempts == max_attempts and guess != num2:
        print(f"you are out of attepts stop skipping school!!!!!💀{num2}.")

# Call and run the game
multiplication_function(max_attempts=3)

  