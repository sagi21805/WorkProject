similar  = [1, 1.3]

circleDict = {

    1: 2,
    1.1 : 2,
    1.3 : 3


}

list = [circleDict.pop(key) for key in similar]
print(list)
print(circleDict)

