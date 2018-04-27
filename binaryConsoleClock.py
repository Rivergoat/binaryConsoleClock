import time

def getXthPowerOfTwo(x):
    if x is 0:
        return 1

    output = 2
    for i in range(x - 1):
        output = output * 2

    return output

def intToBinary(number, lenght = 8):
    binary = []
    number+= 1
    for i in range(1, lenght+1):
        if number > getXthPowerOfTwo(lenght - i):
            number = number - getXthPowerOfTwo(lenght - i)
            binary.append(1)
        else:
            binary.append(0)

    return binary

def printArray(array):
    for i in range(len(array)):
        print(array[i])
