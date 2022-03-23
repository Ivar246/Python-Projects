import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words) # randomly chooses word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word


def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word) #represent all the letter of the word in set 
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what user has guessed
    Total_life = 6
    #getting user input
    while len(word_letters) > 0 and Total_life >0:
        #letter used
        #' '.join(['a', 'b', 'c']) --> 'a b c'
        print(f'total_life = {Total_life}') 
        print('you have used these letters: ', ' '.join(used_letters))
        
        # W-RD format
        word_list = [letter if letter in used_letters else'-' for letter in word]
        print('current_word : ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)  
            else:
                Total_life -= 1
                print('letter is not in the word')
        elif user_letter in used_letters:
            print('You have already used that character, please try again..')
        else:
            print('invalid character. Please try again')
        print('\n')
         
    if Total_life == 0:
        print('Sorry, You die')
        print(word)
    else: 
        print('Congratulation, You won the game.')
        print(word)
       
   
        
hangman()

    
