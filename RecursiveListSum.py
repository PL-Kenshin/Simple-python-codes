#FINISHED
def listSum(l):
    if len(l)==0:
        return 0
    else:
        return l[0] + listSum(l[1:])
        
def listSumTail(l, Sum=0):
    if len(l)==0:
        return Sum
    else:
        return listSumTail(l[1:], Sum + l[0])
    
    
    
def main():
    
    test = [1,2,3,4]
    test2 = []
    
    print(listSum(test))
    print(listSum(test2))
    
    print(listSumTail(test))
    print(listSumTail(test2))

if __name__ == "__main__":
    main()
