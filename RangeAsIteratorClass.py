#FINISHED

class MyRange:

    def __init__(self, a=None, b=None, k=None, *error):
        if error:
            raise ValueError("Metoda przyjmuje od 1 do 3 parametrów")
            
        if a==None:
            raise ValueError("Metoda przyjmuje od 1 do 3 parametrów")
        else:
            self.a = float(a)

        if b == None:
            self.b = self.a + 0.0
            self.a = 0.0
        else:
            self.b = float(b)
            
        if k == None:
            self.k = 1.0
        else:
            if k == 0:
                raise ValueError("krok nie może wynosić 0")
            else:
                self.k = float(k)

    def __iter__(self):
        return self

    def __next__(self):
        if self.a < self.b:
            result = self.a
            self.a += self.k
            return result
        elif self.a > self.b:
            result = self.a
            self.a -= self.k
            return result
        else:
            raise StopIteration


for i in MyRange(5):
    print(i, end=", ")
    
print("\n")

for i in MyRange(1,7):
    print(i, end=", ")
    
print("\n")
for i in MyRange(1,10,0.5):
    print(i, end=", ")
    
print("\n")
for i in MyRange(10,0,1):
    print(i, end=", ")
    
print("\n")
try:
    for i in MyRange():
        print(i, end=", ")
except ValueError as e:
    print(e)
    pass
    
print("\n")
try:
    for i in MyRange(10,0,1,1):
        print(i, end=", ")
except ValueError as e:
    print(e)
    pass
    
