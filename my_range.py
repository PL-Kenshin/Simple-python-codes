#FINISHED

def my_range(a, b=None, k=None):
    a = float(a)
    if b == None:
        b = a + 0.0
        a = 0.0
    if k == None:
        k = 1.0

    count = 0
    list = []
    while True:
        temp = float(a + count * k)
        if k > 0 and temp >= b:
            break
        elif k < 0 and temp <= b:
            break
        list.append(temp)
        count += 1
    return list

test = my_range(1.1,2.2,0.5)
print(test)

test = my_range(1.1,2.1,0.5)
print(test)

test = my_range(1.1,2.2)
print(test)

test = my_range(2.2)
print(test)

test = my_range(2.2,1.1,-0.5)
print(test)
