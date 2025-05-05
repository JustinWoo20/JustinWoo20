# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
import random
print(art.logo)

print("Welcome to the silent auction!")

item = ["Playstation 5", "Wooden Chair", "Year's Supply of Coffee", "Trip to Hawaii",
        "80in flat screen TV", "2025 Lexus", "Wagyu Beef", "Free Voucher for a stay at the Ritz Carlton",
        "Bicycle", "Mona Lisa"]
bid_item = random.choice(item)
print(f"We are bidding for a {bid_item}.")


# Method 1 use a function to find the highest bidder. Method 2, use the max function to find the higehst bidder
bidding_finished = False

bidding_dictionary = {}

def bidding_results(bidding_dictionary):
    highest_bidder = ""
    highest_bid = 0

    for bidder in bidding_dictionary:
        current_bid = bidding_dictionary[bidder]
        if current_bid > highest_bid:
            highest_bid = current_bid
            highest_bidder = bidder
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}. Congratulations, you win a {bid_item}!")

while not bidding_finished:

    name = input("What is your name?\n")
    bid_amount = int(input("What is your bid amount?\n$ "))
    more_bids = input("Are there more participants?\n"
                      "Type \"yes\" to continue or \"no\" to tally the bids.\n").lower()
    print("\n" * 50)

    bidding_dictionary[name] = bid_amount


    if more_bids == "no":
        bidding_finished = True
        # bidding_results(bidding_dictionary)
        highest_bidder = max(bidding_dictionary, key=bidding_dictionary.get)
        print(f"The winner is {highest_bidder} with a bid of ${bidding_dictionary[highest_bidder]}. Congratulations, you get the {bid_item}.")
