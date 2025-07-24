from hangman_helpers import *
import pygame

# CREATE GAME WINDOW/SCREEN
# HINT: use a function from the list
screen = setup_game()

# NAME THE GAME save Jesus😇!
game_title = "Hangman"

# LOAD GAME PICTURES
# HINT: use a function from the list

image = load_images()
# CREATE LIST OF AT LEAST 10 WORDS

words = ["apple", "DragonFruit", "Plum" , "Phone", "Headphones" ]
# PICK A RANDOM WORD
# HINT: use a function from the list
word = pick_word(words)

# KEEP TRACK OF GAME
# What are two variables we can use to keep track of our progress in the game
mistakes = 0
letters = []

# PLAY UNTIL WE TELL IT TO STOP
playing = True

while playing == True:
    # WHAT DO WE SEE ON THE SCREEN
    # HINT: use a function from the list
    draw_game(screen, game_title, image, mistakes, word, letters)
    for event in pygame.event.get():
        # CLOSE THE GAME
        # IF WINDOW IS CLOSED
        if event.type == pygame.QUIT:
            # STOP PLAYING
            playing = False

        # DETECT KEY
        if event.type == pygame.KEYDOWN:
            key = event.unicode.lower() # Grab unicode of pressed key

            # IF THE KEY PRESSED HAS NOT BEEN TRIED BEFORE  

            if key not in letters:
                # ADD IT TO THE LIST OF GUESSED KEYS
                
                #IF THAT KEY WAS WRONG
                letters.append(key)
                    # INCREASE THE COUNT ON THE AMOUNT OF MISTAKES
                if key not in word:
                    mistakes += 1

        #check for win
        win = check_win(word, letters)

        # IF WE WON: 
        if win == True:
        # CELEBRATION MESSAGE (HINT: use a function from the list) 
            show_result(screen, "you win!!!", "blue")
        
        # STOP PLAYING
            playing = False

    # IF WE DID NOT WIN AND WE RAN OUT OF GUESSES (We only have 6)
        if mistakes >= 6 and win == False:
        # TELL PLAYER THEY LOST (HINT: use a function from the list)
         show_result(screen, "You Lost :( ", "red")
        # STOP PLAYING


pygame.quit()
