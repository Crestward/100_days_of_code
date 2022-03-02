
print("Welcome to the silent auction")

bidders = {}

def highest_bid(amount):
    amt = 0
    winner = ""
    for i in amount:
        bid_amount = amount[i]
        if bid_amount > amt:
            amt = bid_amount
            winner = i
    print(f"The winner is {winner} with a bid of ${amt}")

end_of_bid = False

while not end_of_bid:
    name = input("What is your name: ").lower()
    bids = int(input("What is your bid: $"))
    bidders[name] = bids
    other_bid = input("Are there any other bidders: Yes or No: ").lower()

    if other_bid == 'no':
        end_of_bid = True 
        highest_bid(amount=bidders)




