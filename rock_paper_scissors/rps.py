#!/usr/bin/python

import sys

def rock_paper_scissors (n):
    plays = [['rock'], ['paper'], ['scissors']]
    
    # can't go back in time!
    if n < 0:
        return "Impossible"
    
    # Zero plays is boring
    elif n == 0:
        return [[]]
    
    # Stll boring
    elif n == 1: 
        return plays
    
    else:
        ans = []
        for play in plays:
            for simpler_part in rock_paper_scissors(n-1):
                ans.append(play + simpler_part)
        return ans





if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')