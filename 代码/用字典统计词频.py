freqDict = eval(input())
a = input().split()
if a == []:
    print(freqDict)
else:
    for i in a:
        if i in freqDict:
            freqDict[i]+= 1
        else:
            freqDict[i] = 1
    print(freqDict)