import numpy as np
import sys

# Add all numbers
def add_all(*args):
    return np.sum(args)

#print(add_all(1,2,3))

if len(sys.argv) >= 2:
    numbers_to_add = [int(x) for x in sys.argv[1:]]
    print(add_all(numbers_to_add))

else :
    print("Enter the numbers to add please, thank you!! xoxo")