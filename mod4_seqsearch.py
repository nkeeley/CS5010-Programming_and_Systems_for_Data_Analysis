# File: mod4_seqsearch.py
# CS 5010
# Module 4 Exercise: Sequential Serach (Python version: 3)
# Nicholas Keeley, ngk3pf


## Define function.
def linearSearch(target, my_list):
    
    # Creates local sentinel boolean to determine if needs to print and sentinel value.
    sentinel_out=True
    sentinel = -1
    
    # Iterate through list to find target.
    for i in range(len(my_list)):
        
        # If target found, print index, change sentinel to false, and break.
        if(my_list[i]==target):
            sentinel_out=False
            return i
            break
        
        # Sentinel conditional: last index, still no target. Works if target is last term too.
        if((i==(int(len(my_list)))-1) & sentinel_out==True):
            return sentinel

# Print the sentinel value if i reaches end of list without


zoo = ["lion", "tiger", "elephant", "zebra", "bear"]
print(linearSearch("tiger", zoo))
print(linearSearch("zebra", zoo))
print(linearSearch("bear", zoo)) # test case if bear is last term
print(linearSearch("panda", zoo))


