#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):

  # can't take the solid gold full-scale elephant
  small_enough_items = [eye for eye in items if eye['size'] <= capacity]

  # extend the tuples by density = value/size

  # sort the tuples by size and density (smallest, highest first)
  # unclear which has priority

  the_goods = []

  remaining_capacity = capacity

  while remaining_capacity > 0:

    # filter for size-relevance
    while small_enough_items[0][size] > remaining_capacity: 
      small_enough_items.pop(0)

    next_thing = small_enough_items.pop(0) # add the next-densest item
    the_goods.append[next_thing]
    
    remaining_capacity -= next_thing['size']

  return the_goods


  # This is not perfect.  There can be a case where a dense but large item would
  # preclude a number of smaller, nearly identically dense items, that could be 
  # siezed, leaving room for the next valuable item.


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')