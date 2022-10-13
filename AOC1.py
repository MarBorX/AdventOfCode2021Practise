import matplotlib.pyplot as plt

print('---Day 1: Sonar Sweep')

'''
Objective: count the number of times a depth measurement increases
'''

def openFile(fileName):
    # Opens up string file name
    # Forces input to string
    # Returns an array of ints
    with open(str(fileName)) as txt:
        arrayOfInts = [int(line) for line in txt]

    return arrayOfInts

def iterateThroughDepthsAndCountIncrease(arrayOfInts):
    increaseCounter = 0
    for num in range(len(arrayOfInts)-1):
        if(arrayOfInts[num+1] > arrayOfInts[num]):
            increaseCounter += 1

    print(f"Increase in depths: {increaseCounter}")
    return increaseCounter

def iterateThroughDepths_3_SlidingWindow(arrayOfInts):
    arrayOf3Sum = []
    for iter in range(2,len(arrayOfInts)):
        arrayOf3Sum.append(arrayOfInts[iter-2] + arrayOfInts[iter-1] + arrayOfInts[iter])
    
    print('---Part II---')
    iterateThroughDepthsAndCountIncrease(arrayOf3Sum)
    return arrayOf3Sum

def plotData(data):
    # Bonus: Ploting depths over time taken
    t = [element for element in range(1,len(data)+1)] # length == 2000, +1 because not started at 0
    
    plt.plot(t,data, '*')
    plt.xlim(0,2000)
    plt.ylim(0,8000)
    plt.title('t [s] vs. depth [m]')
    plt.xlabel('t [seconds]')
    plt.ylabel('depth [metres]')
    plt.grid()
    plt.show()


# SOLUTION Part I
depths = openFile('AOC1.txt') # Array of ints
numberOfDepthIncreases = iterateThroughDepthsAndCountIncrease(depths) # Int

# SOLUTION Part II
iterateThroughDepths_3_SlidingWindow(depths)

# BONUS
# plotData(depths)