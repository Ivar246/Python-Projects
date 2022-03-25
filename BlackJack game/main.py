from card import deal_card
from os import system
import logo
from replit import clear
  
# def deal_card(): #for generating card
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
    
#     return card


def calculate_score(cards):  #take card and return score
    if sum(cards) == 21 and len(cards) ==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score ==0:
        return "lose, opponent has blackjack"
    elif user_score ==0:
        return "Congratulation you win the game..."
    elif user_score > 21:
        return "Your went over, Your lose"
    elif computer_score > 21:
        return "Opponent went over, You win."
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
    

def play_game():
    print(logo.logo)
   #dealig with computer and user card using deal_card()
    user_card = []
    computer_card = []
    is_game_over = False

    for _ in range(2):  # generating first hand card for computer and user 
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:  #dealing with user card
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f' Your cards: {user_card} \n current_score : {user_score}')
        print(f" computer_cards: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or  user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("type 'Y' to get another card, Type 'N' to pass: ").upper()
            if user_should_deal == 'Y':
                user_card.append(deal_card())
            elif user_should_deal == 'N':
                is_game_over= True
            else:
                print("Invaid Command..")
        
    while computer_score != 0 and computer_score < 17: #generatig card for computer
            computer_card.append(deal_card())
            computer_score = calculate_score(computer_card)
            
    print(f'your final hand: {user_card} \n your final_score: {user_score}')
    print(f'Computer final hand: {computer_card} \n computer final_score: {computer_score}')
    print(compare(user_score, computer_score))


while input('Do you want to play BlackJack game(Type Y or N):').upper() == 'Y':
    clear()
    play_game()
    