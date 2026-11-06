import time as t
# Name: Ethan Smith
# Date: 11/05/2026

# OPTIMIZATION GOALS
# Design a hash table size ad hash function to use space efficiently.
# Design your hash function to distribute keys evenly across the hash table buckets.

listSize = 15013

mTKeyP = [[0]] * listSize
mTKeyG = [[0]] * listSize
mQKeyP = [[0]] * listSize
mQKeyG = [[0]] * listSize
mBest = [[0]] * listSize

wastedSpace = 0
collisions = 0

# 2 Linked List Hash Table with Title as Key

# Poor Hash Function
#  Uses the length of the title and modulos to generate a hash value and then inserts
# the key and value and when there is something already there it creates a list at that location
# of the whatever is there with what you were adding
def poorLinkHFunc(title, info):
    global mTKeyP
    global listSize
    hVal = len(title) % listSize
    if mTKeyP[hVal][0] != 0:
        # If doesnt work switch back to newList
        mTKeyP.append([title, info])
        global collisions 
        collisions += 1
    else:
        mTKeyP[hVal] = [[title, info]]

# Good Hash Function
#   Uses the sum of the ascii values of the title * a big prime % the size of the list to make the
# hash value and then inserts the key and value but if there is something there we add it to the list
# of things that are already there
def goodLinkHFunc(title, info):
    global mTKeyG
    global listSize
    hVal = 0
    for i in title:
        hVal += ord(i)
    hVal = (hVal * 17431) % listSize
    if mTKeyG[hVal][0] != 0:
        mTKeyG.append([title, info])
        global collisions 
        collisions += 1
    else:
        mTKeyG[hVal] = [[title, info]]

# 2 Linear Probing Hash Table Quote as Key

# Poor Hash Function
#   Uses the length of the quote % the list size to make a hash value and then inserts it but if
# something is already there it searches for the next open spot to put it
def poorLinearHFunc(quote, info):
    global mQKeyP
    global collisions
    global listSize
    hVal = len(quote) % listSize
    if mQKeyP[hVal][0] != 0:
        for i in range(len(mQKeyP)):
            if(mQKeyP[(hVal + (i + 1)) % listSize][0] == 0):
                lProbeSpot = (hVal + (i + 1)) % listSize
                mQKeyP[lProbeSpot] = [quote, info]
                break
        collisions += 1
    else:
        mQKeyP[hVal] = [quote,info]

# Good Hash Function
#   Uses the sum of the ascii of the quote * a big prime % the list size to make a hash value 
# and then inserts it but if something is already there it searches for the next open spot to 
# put it
def goodLinearHFunc(quote, info):
    global mQKeyG
    global collisions
    global listSize
    hVal = 0
    for i in quote:
        hVal += ord(i)
    hVal = (hVal * 17431) % listSize
    if mQKeyG[hVal][0] != 0:
        for i in range(len(mQKeyG)):
            if(mQKeyG[(hVal + (i+1)) % listSize][0] == 0):
                lProbeSpot = (hVal + (i + 1)) % listSize
                mQKeyG[lProbeSpot] = [quote, info]
                break
        collisions += 1
    else:
        mQKeyG[hVal] = [quote,info]

# Best of the 4 with more optimization

#   Uses the sum of the ascii of the quote % 499 * a big prime % the list size to make a hash value 
# and then inserts it but if something is already there it searches for the next open spot to 
# put it
def best(quote, info):
    global mBest
    global collisions
    global listSize
    hVal = 0
    for i in quote:
        hVal += ord(i)
    hVal = (hVal % 499) * 17431 % listSize
    if mBest[hVal][0] != 0:
        for i in range(len(mBest)):
            if(mBest[(hVal + (i+1)) % listSize][0] == 0):
                lProbeSpot = (hVal + (i + 1)) % listSize
                mBest[lProbeSpot] = [quote, info]
                break
        collisions += 1
    else:
        mBest[hVal] = [quote,info]

# The function that runs it all
def main():
    global wastedSpace
    global mTKeyP
    global mTKeyG
    global mQKeyP
    global mQKeyG
    global mBest
    time = t.time()
    with open("MOCK_DATA.csv", "r") as f:
        fLines = f.readlines()
        for line in fLines:
            lList = line.split(",")
            quote = lList[len(lList) - 1]
            info = lList[0:len(lList) - 1]
            best(quote, info)
    time = t.time() - time
    for i in range(len(mBest)):
        if mBest[i][0] == 0:
            wastedSpace += 1
    print(f"Time: {time:.2f}\nCollisons: {collisions}\nWasted Space: {wastedSpace}")
# Calling the function that runs it all
main()