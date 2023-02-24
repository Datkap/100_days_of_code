from day_9.secret_auction_extras import logo
from replit import clear

bidders = {}
more_bidders = True

while more_bidders:
    clear()
    current_bidder = input("What's your name?")
    current_bid = input("What's your bid?")
    bidders[current_bidder] = current_bid
    if input("Are there more bidders?").lower() == "no":
        more_bidders = False


print(f"Highest bidder is {max(bidders, key=bidders.get)} with the value of {max(bidders.values())}.")