import time as t

# OPTIMIZATION GOALS
# Design a hash table size ad hash function to use space efficiently.
# Design your hash function to distribute keys evenly across the hash table buckets.
listSize = 15013

mTKeyP = [[0]] * listSize
mTKeyG = [[0]] * listSize
mQKeyP = [[0]] * listSize
mQKeyG = [[0]] * listSize
best = [[0]] * listSize

wastedSpace = 0
collisions = 0

# 2 Linked List Hash Table with Title as Key
# Poor Hash Function
def poorLinkHFunc(title, info):
    global mTKeyP
    global listSize
    hVal = len(title) % listSize
    if mTKeyP[hVal][0] != 0:
        #newList = mTKeyP[hVal][0:len(mTKeyP[hVal])]
        # If doesnt work switch back to newList
        mTKeyP.append([title, info])
        #mTKeyP[hVal] = newList
        global collisions 
        collisions += 1
    else:
        mTKeyP[hVal] = [[title, info]]

# Good Hash Function
def goodLinkHFunc(title, info):
    global mTKeyG
    global listSize
    hVal = 0
    for i in title:
        hVal += ord(i)
    hVal = (hVal * 17431) % listSize
    if mTKeyG[hVal][0] != 0:
        #newList = mTKeyG[hVal][0:len(mTKeyG[hVal])]
        mTKeyG.append([title, info])
        #mTKeyG[hVal] = newList
        global collisions 
        collisions += 1
    else:
        mTKeyG[hVal] = [[title, info]]
# 2 Linear Probing Hash Table Quote as Key
# Poor Hash Function
def poorLinearHFunc(quote, info):
    global mQKeyP
    global collisions
    global listSize
    hVal = len(quote) % listSize
    # For some reason puts the collided item in from the beginning i think has to do with lProbeSpot
    curVal = mQKeyP[hVal][0]
    #print(f"hVal = {hVal},Quote = {quote}, Quote at hVal = {curVal}")
    if mQKeyP[hVal][0] != 0:
        for i in range(len(mQKeyP[hVal + 1:len(mQKeyP)])):
            if(mQKeyP[hVal + i][0] == 0):
                # This always returns the first index of the list
                lProbeSpot = (hVal + i) % listSize
                mQKeyP[lProbeSpot] = [quote, info]
                break
        if([quote, info] not in mQKeyP):
            for k in range(len(mQKeyP[0:hVal])):
                # Probably shouldn't have hVal + i since I want to go throught he first part of the list
                if(mQKeyP[k][0] == 0):
                    lProbeSpot = (k) % listSize
                    mQKeyP[lProbeSpot] = [quote, info]
                    break
        collisions += 1
    else:
        mQKeyP[hVal] = [quote,info]
# Good Hash Function

# Best of the 4 with more optimization

def main():
    global wastedSpace
    global mTKeyP
    global mTKeyG
    global mQKeyP
    time = t.time()
    with open("MOCK_DATA.csv", "r") as f:
        fLines = f.readlines()
        for line in fLines:
            lList = line.split(",")
            quote = lList[len(lList) - 1]
            info = lList[0:len(lList) - 1]
            poorLinearHFunc(quote, info)
    time = t.time() - time
    for i in mQKeyP:
        if i[0] == 0:
            wastedSpace += 1
    print(f"Time: {time:.2f}\nCollisons: {collisions}\nWasted Space: {wastedSpace}")

main()