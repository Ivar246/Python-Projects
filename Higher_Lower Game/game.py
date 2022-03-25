import random
from tkinter import Y
from data import data
from art import logo
from os import system
from replit import clear


def choose_people():
    people = random.choice(data)

    return people


# compare the follower of poeple 
def compare(user_input, A, B):
    if user_input == 'A':
        if A['follower_count']  > B['follower_count']:
            return True
        return False
    elif user_input == 'B':
        if B['follower_count'] > A['follower_count']:
            return True
        return False


def play():
    dict_A = choose_people()
    dict_B = choose_people()
    if dict_A == dict_B:
        dict_B = choose_people()
        
    correct = True
    score = 0
    print(logo)
    
    while correct:
        print(f"compare A: {dict_A['name']}, {dict_A['description']}, {dict_A['country']}")
        print('\n    VS    \n')
        print(f"against B: {dict_B['name']}, {dict_B['description']}, {dict_B['country']}")
        
        choice = input("What is your choice?(A or B) : ").upper()
        
        if compare(choice, dict_A, dict_B) == True:
            score += 1
            dict_A = dict_B
            dict_B = choose_people()
            system('clear')
            print('Correct!')  
            print(f'current_score:{score}')       
        else:
            clear()
            print(f'Your choice is wrong..\nfinal score: {score}')
            user_input = input('Do you want to play again?(Y or N): ').upper()
            if user_input == 'Y':
                system('clear')
                play()
            else:
                correct = False

       
play()         
                