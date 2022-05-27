#FINISHED

from functools import reduce

def average(lst):
    return reduce(lambda a, b: a + b, lst) / len(lst)
    
def maxValue(lst):
    return reduce(lambda a, b: a if a > b else b, lst)
    
def reduceLists(col):
    return reduce(lambda a, b: a + b, col)
    
def calcDistance(vec1, vec2):
    return reduce(lambda a, b: a + abs((b[0] - b[1])), zip(vec1,vec2) , 0)
    


def main():
    
    testList     =   [1,2,3,4,5]
    testList1    =   [-9,-8,-7,-6,-5]
    testList2    =   [11,12,13,14,15]
    collection   =   [testList,testList1,testList2]
    vector1      =   [100,47]
    vector2      =   [-65, 32]
    
    print("Średnia z listy:",average(testList),)
    
    print("\nNajwiększa wartość listy:",maxValue(testList))
    
    print("\nZłączona lista:",reduceLists(collection))
    
    print("\nOdległość między wektorami współrzędnych:", calcDistance(vector1,vector2))
    
if __name__ == "__main__":
    main()
