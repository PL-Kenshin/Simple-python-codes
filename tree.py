#FINISHED
import string

height = 0

while height != 7:
    print('Podaj wysokosc choinki: ', end='')
    height=int(input())
    if height %2 == 0:
        char='*'
    else:
        char='#'
        
    for i in range(1, height+1):
        print(' '*(height-i), end='')
        print(char*(2*i-1))
