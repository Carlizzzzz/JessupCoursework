aList = [1,7,3,4]


def get_products_of_all_ints_except_at_index(aList):
    newList = []
    for i in range(0, len(aList)):
        for j in range(i+1, len(aList)):
            for k in range(j+1, len(aList)):
                newList.append(aList[i]*aList[j]*aList[k])
    return newList



print(get_products_of_all_ints_except_at_index(aList))