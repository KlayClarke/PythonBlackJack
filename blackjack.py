import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def check_for_ace():
    for card in user_hand:
        if card == 11:
            print(sum(user_hand))
            if sum(user_hand) < 21:
                print('\nYou\'ve been dealt an ace! \n')
                ace_choice = int(input('\nWould you like this ace to count as 1 or 11? Please type either "1" or "11" to continue. \n' ))
                if ace_choice == 1:
                    card_index = user_hand.index(card)
                    user_hand[card_index] = 1
                    user_score = sum(user_hand)
                    print(f'\nYour cards: {user_hand}, your score: {user_score}')
                elif ace_choice == 11:
                    card_index = user_hand.index(card)
                    user_hand[card_index] = 11
                    user_score = sum(user_hand)
                    print(f'\nYour cards: {user_hand}, your score: {user_score}')
            elif sum(user_hand) > 21:
                print(f'\nYour hand: {user_hand}, your score: {user_score}\n')
                print(f'\nDealer\'s hand: {dealer_hand}, dealer\'s score: {dealer_score}\n')
                print('\nDealer Wins\n')
##def soft_17():
##    if dealer_score >= 17 or dealer_score == 21:
##        end_of_game = True
##    else:
##        while dealer_score < 17:
##            dealer_hand.append(random.choice(cards))
##            dealer_score = sum(dealer_hand)
def show_score():
    print(f'\nYour hand: {user_hand}, your score: {user_score}\n')
    print(f'\nDealer\'s hand: {dealer_hand}, dealer\'s score: {dealer_score}\n')

print(logo)

end_of_game = False
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_hand = []
dealer_hand = []

user_hand.append(random.choice(cards))
dealer_hand.append(random.choice(cards))
dealer_hand.append(random.choice(cards))

while not end_of_game:

    user_hand.append(random.choice(cards))

    user_score = sum(user_hand)

    print(f'\nYour cards: {user_hand}, current score: {user_score}\n')
                  
    check_for_ace()

    dealer_score = sum(dealer_hand)

    print(f'\nDealer\'s first card: {dealer_hand[0]}\n')

    if user_score >= 21 or dealer_score >= 21:
        end_of_game = True
    else:
        user_hit = input('\nType "y" to get another card, type "n" to pass: \n').lower()
        if user_hit == 'y':
            end_of_game = False  

        elif user_hit == 'n':
            if dealer_score < 17:
                while dealer_score < 17:                
                    dealer_hand.append(random.choice(cards))
                    dealer_score = sum(dealer_hand)
                    show_score()
                end_of_game = True
        
if end_of_game == True:
    if dealer_score > 21 and user_score > 21:
        show_score()
        print('\nNo true winner. Both the dealer and the user busted.\n')
    elif dealer_score > 21 or user_score == 21 or (user_score < 21 and user_score > dealer_score):
        show_score()
        print('\nYou Win\n')
    elif user_score > 21 or dealer_score == 21 or (dealer_score < 21 and dealer_score > user_score):
        show_score()
        print('\nYou Lose\n')
    elif user_score == dealer_score:
        show_score()
        print('\nGame ended in a tie\n')
    else:
        show_score()
        print('\nExtraneous result that I had not accounted for.\n')
