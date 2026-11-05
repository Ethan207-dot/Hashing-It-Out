import time as t

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

main()