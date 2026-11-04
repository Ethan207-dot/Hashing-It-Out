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
    hVal = len(title) % listSize
    if mTKeyP[hVal][0] != 0:
        newList = mTKeyP[hVal][0:len(mTKeyP[hVal])]
        newList.append([title, info])
        mTKeyP[hVal] = newList
        global collisions 
        collisions += 1
    else:
        mTKeyP[hVal] = [[title, info]]

# Good Hash Function

# 2 Linear Probing Hash Table Quote as Key
# Poor Hash Function

# Good Hash Function

# Best of the 4 with more optimization

def main():
    global wastedSpace
    global mTKeyP
    time = t.time()
    with open("MOCK_DATA.csv", "r") as f:
        fLines = f.readlines()
        for line in fLines:
            lList = line.split(",")
            title = lList[0]
            info = lList[1:len(lList)]
            poorLinkHFunc(title, info)
    time = t.time() - time
    for i in mTKeyP:
        if i[0] == 0:
            wastedSpace += 1
    print(f"Time: {time:.2f}\nCollisons: {collisions}\nWasted Space: {wastedSpace}")

main()