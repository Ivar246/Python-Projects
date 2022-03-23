import random


def play():
    print('''Enter <r> rock.
Enter <s> for scissor.
Enter <p> for paper.''')
    user = input("What's your choice? ").lower()
    computer = random.choice(['r', 's', 'p'])
    if user == computer:
        return 'Tie'
    if is_win(user, computer):     
        return 'Hurrah, You won the game'
    return 'You lost'


def is_win(player, opponent): #comparing user choice and computer which return true when user win
    if ((player == 'r' and opponent == 's' ) or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r')):
        return True


print(play())