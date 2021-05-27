# File: mod4_binsearch.py
# CS 5010
# Module 4 Exercise: Binary Search (Python version: 3)
# Nicholas Keeley, ngk3pf

import math


## Define function.
def BinarySearch(item_list, target):
    
    # Boolean for found target or not.
    found = False
    
    # Create initial pointers.
    high_ind = int(len(item_list))-1 # Converts length of list into useful high index. CORRECT.
    low_ind = 0
    mid_ind = int((low_ind+high_ind)/2)

    # Loop until mid, low, and hi indeces all point to same index or you found the value.
    while(found == False):

        # If value != target, found = True. Should trigger closeout of loop. CORRECT.
        if (item_list[mid_ind] == target):
            found=True
            return found
        
        # If target less than mid value, mid becomes high.
        if(target < item_list[mid_ind]):
            high_ind = mid_ind - 1
            mid_ind = float((low_ind+high_ind)/2)
            mid_ind= math.floor(mid_ind)
        
        # If target greater than mid value, mid becomes low.
        if(target > item_list[mid_ind]):
            low_ind = mid_ind + 1
            temp = (low_ind+high_ind)/2
            mid_ind = math.floor(temp)

        # Exception case. All three indces point to same value.
        if(low_ind == high_ind & high_ind == mid_ind):
            if (item_list[mid_ind] == target):
                found=True
                return found
            else:
                return found

item_list = [1, 2, 50, 500, 10000, 500000, 50000001]    
print("Is 1 in " + str(item_list) + "? " +str(BinarySearch(item_list, 1)))
print("Is 50000001 in " + str(item_list) + "? " +str(BinarySearch(item_list, 50000001)))
print("Is 3 in " + str(item_list) + "? " +str(BinarySearch(item_list, 3)))