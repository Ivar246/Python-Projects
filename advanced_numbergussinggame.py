import random
from os import system

def play(attempts):
    number = random.randint(1, 100)
    guess = 0
    
    while guess != number and attempts != 0:
        print(f'You have {attempts} attempts left.')
        guess = int(input("Enter your guess: "))
        if number > guess:
            print('Too low...\nGuess again')
            attempts -=1
        elif number < guess:
            print('Too high... \nGuess again')
            attempts -=1
    if attempts == 0:
        print("You loose..")
        
        
    else:
        print('Hurrah! You won the game...')



def start_game():
    want_to_play = True    
    while want_to_play:
        user = input('Do you want to play Number_guessing game(Type Y or N):').upper()
        if user == 'Y':
            system("clear")
            print('''Welcome to Number Guessing Game..
                  Plz guess the number between 1 and hundered ''')
            level = input("which level do you prefer(Type 'Easy' or 'Hard'): ").title()
            if level == 'Hard':
                play(5)
            elif level == "Easy":
                play(10)
            else: 
                print('Invalid input...')
        elif user == 'N':
             want_to_play = False
        else:
             print("invalid command.\nPlease Enter the valid command to play the game")
             


start_game()