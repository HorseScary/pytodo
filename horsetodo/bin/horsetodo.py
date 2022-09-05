#!/usr/bin/env python

import horsetodo
import argparse

from horsetodo.horsetodo import showIndexed

file = "/home/horse/.horseTODO" #this is best practice 100% real!!!!!
# if your name isnt horse or you dont want it in your home directory just like change it idk thats not my problem

parser = argparse.ArgumentParser(description="A simple TODO script")
group = parser.add_mutually_exclusive_group(required=False)

group.add_argument('--add', '-a', type=str, default=None, nargs='?', help="Add an item to the TODO list")
group.add_argument('--remove', '-r', type=int, default=None, nargs='?', help="Remove an item from TODO list by index")

args = parser.parse_args()

if args.add != None:
    print(horsetodo.addItem(file, args.add))
elif args.remove != None:
    print(horsetodo.removeItem(file, args.remove))
else:
    showIndexed(file)