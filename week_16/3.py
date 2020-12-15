def getMinimumIndex(list):
    orderedList = []
    for index in range(len(list)):
        index = list.index(min(list))
        result = min(list)
        list.pop(index)
        list.insert(index,max(list))
        orderedList.append(result)
    return orderedList

initalList = eval(input())
print(getMinimumIndex(initalList))
