import random

#user guess number 
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Enter your guess >"))
        if guess < random_number:
            print('sorry, try again, too low..')
        elif guess > random_number:
            print('sorry, try again, too high')
    else:
        print('congrats, you won...')


#computer guess number
def computer_guess(x):
    low =  1
    high = x 
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess}, too high(H), too low(L), or correct(C) ").lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess+1
    else: 
        print('Hurrah!, The computer guess your number')      
    
  
computer_guess(10)     