##edit code to allow for accurate blackjack step where dealer deals own card until soft 17
##make sure the if end_of_game conditional is specific enough
##overall good job

import random

def check_for_ace():
    for card in user_hand:
        if card == 11:
            if sum(user_hand) < 21:
                print('You\'ve been dealt an ace! \n')
                ace_choice = int(input('\nWould you like this ace to count as 1 or 11? Please type either "1" or "11" to continue. \n' ))
                if ace_choice == 1:
                    card_index = user_hand.index(card)
                    user_hand[card_index] = 1
                    user_score = sum(user_hand)
                    print(f'\nYour cards: {user_hand}, current score: {user_score}')
                elif ace_choice == 11:
                    card_index = user_hand.index(card)
                    user_hand[card_index] = 11
                    user_score = sum(user_hand)
                    print(f'\nYour cards: {user_hand}, current score: {user_score}')
            elif sum(user_hand) > 21:
                print(f'\nYour final hand: {user_hand}, final score: {user_score}\n')
                print(f'\nDealer\'s final hand: {dealer_hand}, final score: {dealer_score}\n')
                print('\nDealer Wins\n')
            else:
                continue

##def soft_17():
##    if dealer_score >= 17 or dealer_score == 21:
##        end_of_game = True
##    else:
##        while dealer_score < 17:
##            dealer_hand.append(random.choice(cards))
##            dealer_score = sum(dealer_hand)
def show_score():
    print(f'\nYour final hand: {user_hand}, final score: {user_score}\n')
    print(f'\nDealer\'s final hand: {dealer_hand}, final score: {dealer_score}\n')
    
end_of_game = False
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_hand = []
dealer_hand = []
user_score = 0
dealer_score = 0

user_hand.append(random.choice(cards))
dealer_hand.append(random.choice(cards))

while not end_of_game:

    user_hand.append(random.choice(cards))
    user_score = sum(user_hand)

    print(f'\nYour cards: {user_hand}, current score: {user_score}\n')
                  
    check_for_ace()
    
    dealer_hand.append(random.choice(cards))
    dealer_score = sum(dealer_hand)

    print(f'\nDealer\'s first card: {dealer_hand[0]}\n')

    if user_score >= 21:
        end_of_game = True
    else:
        user_hit = input('\nType "y" to get another card, type "n" to pass: \n').lower()
        if user_hit == 'y':
            end_of_game = False  

        elif user_hit == 'n':
            #try to account for soft 17 rule of dealers... once dealer soft 17, then compare hands and reveal winner
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
