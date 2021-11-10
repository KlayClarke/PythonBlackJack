##edit code to allow for accurate blackjack step where dealer deals own card until soft 17
##make sure the if end_of_game conditional is specific enough
##overall good job

import random

end_of_game = False

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user_hand = [random.choice(cards), random.choice(cards)]

user_score = sum(user_hand)

print(f'Your cards: {user_hand}, current score: {user_score}')

def ace_select():
    for card in user_hand:
        if card == 11:
            ace_choice = int(input('Would you like this ace to count as 1 or 11? Please type either "1" or "11" to continue.' ))
            if ace_choice == 1:
                card = 1
            elif ace_choice == 11:
                card = 11
                
ace_select()

dealer_hand = [random.choice(cards), random.choice(cards)]
dealer_score = sum(dealer_hand)

print(f'Dealer\'s first card: {dealer_hand[0]}')

user_hit = input('Type "y" to get another card, type "n" to pass: ').lower()

if user_hit == 'y':
    user_hand.append(random.choice(cards))
    user_score = sum(user_hand)
    ace_select()
    print(f'Your cards: {user_hand}, current score: {user_score}')
    dealer_hand.append(random.choice(cards))
    dealer_score = sum(dealer_hand)
    print(f'Dealer\'s first card: {dealer_hand[0]}')
    if user_score >= 21 or dealer_score >= 21:
        end_of_game = True
    else:
        print(f'Your cards: {user_hand}, current score: {user_score}')
        print(f'Dealer\'s first card: {dealer_hand[0]}')
        user_hit = input('Type "y" to get another card, type "n" to pass: ').lower()   
elif user_hit == 'n':
    end_of_game = True
if end_of_game:
    if user_score == 21 or dealer_score > 21 or user_score < 21 and user_score > dealer_score:
        print(f'Your final hand: {user_hand}, final score: {user_score}')
        print(f'Dealer\'s final hand: {dealer_hand}, final score: {dealer_score}')
        print('You Win')
    elif dealer_score == 21 or user_score > 21 or dealer_score < 21 and dealer_score > user_score:
        print(f'Your final hand: {user_hand}, final score: {user_score}')
        print(f'Dealer\'s final hand: {dealer_hand}, final score: {dealer_score}')
        print('Dealer Wins')
        
