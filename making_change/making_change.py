#!/usr/bin/python

import sys

def making_change(amount, denominations):
  
if amount < 0:
  return "Amount can't be negative."

cache = [0]*(amount + 1) # we want an entry for index = amount

# base case
cache[0] = 1

# iteratively build cache
# per denomination, per number of coins
for d in denominations:
  i = 1
  while (i * d) < amount:
    # do something
    i += 1

return  # value found in a single column cache
        # or some weird value that is the sum of values in different columms



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")