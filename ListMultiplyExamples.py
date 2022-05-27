#FINISHED

from functools import partial
from operator import mul

def multiply1(numbersList):
    return list(map(lambda x: x*len(numbersList), numbersList))
    
def multiply2(numbersList):
    return list(map(partial(mul, len(numbersList)), numbersList))
    
def multiply3(numbersList):
    return list(map(multiplyMethod(len(numbersList)), numbersList))
    
def multiplyMethod(a):
    def multiplyBy(b):
        return a*b
    return multiplyBy
    
    
def main():
    
    testList = [1,3,5]
    
    print(multiply1(testList))
    
    print(multiply2(testList))
    
    print(multiply3(testList))
    
    
    
if __name__ == "__main__":
    main()
