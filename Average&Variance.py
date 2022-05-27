#FINISHED

def varianceFunction(table):
    avg = variance = squareAvg = 0
    numberOfElements = len(table)
    avg = sum(table)/len(table)
    
    for x in table:
        squareAvg += (x-avg)**2
    variance = squareAvg/len(table)
    return avg, variance
    
    
tab = []

x = 1
while x != 0:
    x = int(input("Wprowadź liczbę do tablicy: "))
    if x == 0: 
        break
    tab.append(x)


result = varianceFunction(tab)
print("\nŚrednia:", result[0], "\nWariancja:",result[1])

tab.clear()
tab = [3,3,3,3]

result = varianceFunction(tab)
print("\nTablica: \"3,3,3,3\" \nŚrednia:", result[0], "\nWariancja:",result[1])

tab.clear()
tab = [5,6,7,8,9]

result = varianceFunction(tab)
print("\nTablica: \"5,6,7,8,9\" \nŚrednia:", result[0], "\nWariancja:",result[1])
