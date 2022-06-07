#FINISHED

def varRec(ls, length, lsSum = 0):
    if(len(ls) > 0):
        avg, variance = varRec(ls[1:], length, ls[0] + lsSum)
        variance = variance + (ls[0] - avg)**2
        
        if(len(ls) == length):
            variance = 1/(length-1) * variance
            
        return avg, variance
        
    else:
        return lsSum / length, 0
 
def main():
    
    testList1 = [3,3,3,3]
    testList2 = [5,6,7,8,9]
    
    test1 = varRec(testList1,4)
    test2 = varRec(testList2,5)
    
    print("Pierwsza lista\nŚrednia: ", test1[0], "Wariancja:", test1[1])
    print("Druga lista\nŚrednia: ", test2[0], "Wariancja:", test2[1])

if __name__ == "__main__":
    main()
