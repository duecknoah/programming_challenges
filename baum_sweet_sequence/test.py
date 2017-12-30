''''
b_n = 0 if the binary representation of n contains a block of consecutive 0s of odd length
'''

def integerToBinary(n):
    '''
    Takes in n: an integer 
    Returns back s: a string representing the binary version of n
    '''

    #generate sequence of binary digits up to n 
    i = 1
    binDigits = []
    while i <= n:
        binDigits.append(i)
        i *= 2
    binDigits.reverse()

    #converting to binary
    s = ""
    for digit in binDigits: 
        if (n-digit) >= 0:
            s += "1"
            n -= digit
        else:
            s += "0"
    return s


def baumSweet(n):
    '''
    Given an integer n, returns the baumSweet value (1 or 0)
    '''
    binaryNum = integerToBinary(n)
    i = 0
    while i < len(binaryNum):
        if binaryNum[i] == '0':
            runCount = 0
            while i < len(binaryNum) and binaryNum[i] == '0':
                runCount += 1
                i += 1

            i -= 1

            if runCount % 2 != 0:
                return 0

        i += 1

    return 1

upTo = int(input("Enter n: "))
answer = [baumSweet(elem) for elem in list(range(upTo+1))]
print("Baum sweet sequence is: " + str(answer))