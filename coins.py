#FINISHED

arr = [2, 5, 10]
m = len(arr)
n = 100

table = [0 for k in range(n+1)]
table[0] = 1

for i in range(0,m):
    for j in range(arr[i],n+1):
        table[j] += table[j-arr[i]]
  
print("Liczba możliwych kombinacji: ",table[n])
