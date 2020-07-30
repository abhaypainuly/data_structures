def sumOddEven(lst):
    sumEven = 0
    sumOdd = 0
    for val in lst:
        if val%2==0:
            sumEven = 2*sumEven+1
            sumOdd *= 2
        else:
            sumEven,sumOdd =sumEven+sumOdd,sumEven+sumOdd+1
    print(sumEven,sumOdd)


#BOTTOM UP APPROACH
def sumOddEven(lst):
    countEven = [0]*(len(lst)+1)
    countOdd = [0]*(len(lst)+1)
    for i in range(1,len(lst)+1):
        if lst[i-1]%2==0:
            countEven[i] = countEven[i-1] + countEven[i-1]+1
            countOdd[i] = countOdd[i-1] + countOdd[i-1]
        else:
            countEven[i],countOdd[i] = countEven[i-1]+countOdd[i-1],countEven[i-1]+countOdd[i-1]+1
    return countEven[len(lst)],countOdd[len(lst)]
    