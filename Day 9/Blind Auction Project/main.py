# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)
bids = {}
bidder = True

while bidder:
    name = input("Whats is your name? \n")
    price = input("What is your bid? \n")
    bids[name] = price
    play = input("Are there any other bidders? Type 'yes' or 'no' \n")
    if play == 'yes':
        print("\n" * 80)
    elif play == 'no':
        bidder = False
    else:
        print('Please type a valid response')

win_bid = 0
winner = ''
for bid in bids:
    if int(bids[bid]) > win_bid:
        win_bid = int(bids[bid])
        winner = bid
print(f"The winner is {winner} with a bid of ${win_bid}")


