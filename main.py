from replit import clear
from art import logo

continue_prompt = True
all_bids = {}
winning_amt = 0
winning_bid = {}
while continue_prompt:
  print(logo)
  name = input("What's your name?: ")
  bid = int(input(f"{name}, what's your bid?: $")) 
  all_bids[name] = bid
  more_users = input("More people bidding?: y / n ")
  if more_users == "n":
    continue_prompt = False
    clear()
    for key in all_bids:
      if all_bids[key] > winning_amt:
        winning_amt = all_bids[key]
        winning_bid = {key : all_bids[key]}
    print(winning_bid)
  else:
    clear()
