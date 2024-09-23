import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_total = {}



def player_choice(amount):
    return random.sample(cards, amount)
def dealer_chocie(amount):
    return random.sample(cards, amount)

deal = True

def blackjack_coinditions(player_total_hand_play, dealer_total_hand_play, next_card):
    if player_total_hand_play > dealer_total_hand_play and player_total_hand_play <= 21:
        print(f"Your final hand: {game_total['player_picks']}, current score: {game_total['user_hand']}")
        print(f"Computer's final hand: {game_total['dealer_picks']}, current score: {game_total['dealer_hand']}")
        print("You win")
        return not pick_card
    elif player_total_hand_play == dealer_total_hand_play and next_card == 'n':
        print(f"Your final hand: {game_total['player_picks']}, current score: {game_total['user_hand']}")
        print(f"Computer's final hand: {game_total['dealer_picks']}, current score: {game_total['dealer_hand']}")
        print("It's a draw")
        return not pick_card
    elif player_total_hand_play > 21:
        print(f"Your cards: {game_total['player_picks']}, current score: {game_total['user_hand']}")
        print(f"Computer's first card: {game_total['dealer_picks'][0]}")
        print(f"Your final hand: {game_total['player_picks']}, current score: {game_total['user_hand']}")
        print(f"Computer's final hand: {game_total['dealer_picks']}, current score: {game_total['dealer_hand']}")
        print("You went over. You lose")
        return not pick_card
    elif dealer_total_hand_play > 21:
        print(f"Your cards: {game_total['player_picks']}, current score: {game_total['user_hand']}")
        print(f"Computer's first card: {game_total['dealer_picks'][0]}")
        print(f"Your final hand: {game_total['player_picks']}, current score: {game_total['user_hand']}")
        print(f"Computer's final hand: {game_total['dealer_picks']}, current score: {game_total['dealer_hand']}")
        print("Dealer went over. You win")
        return not pick_card
    else:
        print(f"Your final hand: {game_total['player_picks']}, current score: {game_total['user_hand']}")
        print(f"Computer's final hand: {game_total['dealer_picks']}, current score: {game_total['dealer_hand']}")
        print("You lose")
        return not pick_card

def hand(play, next_card, pick_card):
    total_player_score = 0
    total_dealer_score = 0
    for player_value in game_total['player_picks']:
        total_player_score += player_value
    for dealer_value in game_total['dealer_picks']:
        total_dealer_score += dealer_value
    game_total["user_hand"] = total_player_score
    game_total["dealer_hand"] = total_dealer_score

    print(f"Your cards: {game_total['player_picks']}, current score: {game_total['user_hand']}")
    print(f"Computer's first card: {game_total['dealer_picks'][0]}")

    player_total_hand_play = 0
    dealer_total_hand_play = 0
    for player_picks in game_total['player_picks']:
        player_total_hand_play += player_picks
    for dealer_picks in game_total['dealer_picks']:
        dealer_total_hand_play += dealer_picks

    if play == 'n' or next_card == 'y':
        blackjack_coinditions(player_total_hand_play, dealer_total_hand_play, next_card)
    if next_card == 'n':
        blackjack_coinditions(player_total_hand_play, dealer_total_hand_play, next_card)


player = []
dealer = []
next_card = ''
pick_card = True
while deal:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    pick_card = True
    game_total = {}
    dealer_total_hand = 0
    if play == 'n':
        player += player_choice(2)
        dealer += dealer_chocie(2)
        game_total['player_picks'] = player
        game_total['dealer_picks'] = dealer
        for hands in game_total['dealer_picks']:
            dealer_total_hand += hands
        if dealer_total_hand < 17:
            dealer += dealer_chocie(1)
            game_total['dealer_picks'] = dealer
        pick_card = hand(play, next_card, pick_card)
    if play == 'y':
        player = []
        dealer = []
        player += player_choice(2)
        dealer += dealer_chocie(2)
        game_total['player_picks'] = player
        game_total['dealer_picks'] = dealer
        hand(play, next_card, pick_card)
        while pick_card:
            next_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if next_card == 'n':
                hand_return = hand(play, next_card, pick_card)
                pick_card = hand
            elif next_card == 'y':
                accum_value = 0
                player += player_choice(1)
                for player_value in game_total['player_picks']:
                    accum_value += player_value
                for hands in game_total['dealer_picks']:
                    dealer_total_hand += hands
                if dealer_total_hand < 17:
                    dealer += dealer_chocie(1)
                    game_total['dealer_picks'] = dealer
                pick_card = hand(play, next_card, pick_card)