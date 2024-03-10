def ToList(num):
    li = []
    for i in num:     
        li.append(int(i))
    return li

def toTen(number,testLi):
    toTen = 0
    for j in range(len(testLi)):
        temp = number**(len(testLi)-1-j)*testLi[j]
        toTen += temp

    return toTen

def testTwo(li):
    resultLi = []
    for i in range(len(li)):
        testLi = li.copy()
        if testLi[i] == 0:
            testLi[i] = 1
        elif testLi[i] == 1:
            testLi[i] = 0

        resultLi.append(toTen(2,testLi))
    
    return resultLi

def testThree(li):
    resultLi = []
    for i in range(len(li)):
        testLi = li.copy()
        if testLi[i] == 0:
            testLi[i] = 1
            resultLi.append(toTen(3,testLi))
            testLi[i] = 2
            resultLi.append(toTen(3,testLi))
        elif testLi[i] == 1:
            testLi[i] = 2
            resultLi.append(toTen(3,testLi))
            testLi[i] = 0
            resultLi.append(toTen(3,testLi))
        elif testLi[i] == 2:
            testLi[i] = 1
            resultLi.append(toTen(3,testLi))
            testLi[i] = 0
            resultLi.append(toTen(3,testLi))
    
    return resultLi

def findSame(l1,l2):
    s1 = set(l1)
    s2 = set(l2)
    common = s1 & s2
    return list(common)[0]



n1 = input()
n2 = input()

list1 = ToList(n1)
list2 = ToList(n2)

test1 = testTwo(list1)
test2 = testThree(list2)

print(findSame(test1,test2))