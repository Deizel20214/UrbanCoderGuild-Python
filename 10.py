import random 
import math


def main():

    secret_number = round(random.random() * 9+1)
    guess = True
    attempts = 0
    max_attempts = 3

    print("I'm thiking of a number beteween 1 and 10")
    print(f"You have {max_attempts} attempts to guess the number")
    

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts+=1

        if guess < secret_number:
            print("your Guess is to low ")
        elif guess > secret_number:
            print("your Guess is to High") 
        else:
            print(f"you guessed corectly!! {secret_number} , it took you {attempts} attempts to getb it ")
            break
        
    if guess != secret_number:
        print(f"your out of attepts! The corect number was {secret_number}")
    print("game over!!")
    
    if __name__=="__main__":
        main()
