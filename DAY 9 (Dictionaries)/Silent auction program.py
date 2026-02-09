# TODO-1: Ask the user for input
# TODO-2: Save the data into dictionary {name:price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare the bids in the dictionary

import art
print(art.logo) 


# print(Bid_amount)
def find_highest_bidder(Bid_amount):
    winner=""
    highest_bid = 0
    for bid in Bid_amount:
        bid_price = Bid_amount[bid]
        if bid_price > highest_bid:
            highest_bid = bid_price
            winner=bid
    print(f"The winner is {winner} with the bid amount ${bid_price}")                                                                                                      

Bid_amount={}
# run = True
while True:
    Name = input("What is your name?: ")
    Bid = int(input("What's your bid? $"))
    
    Bid_amount[Name]=Bid

    another_person = input("Is there any other person? Type yes or no: ").lower()
    # print("\n"*20)
    if another_person == "no":
        
    #  run = False
        find_highest_bidder(Bid_amount)
        # for amount in
        #max(Bid_amount[Name])
        break 
    elif another_person == "yes":
        print("\n"*20)

