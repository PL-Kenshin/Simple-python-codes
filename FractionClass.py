#FIXED AND FINISHED

from decimal import Decimal

class Fraction:
    __counter = 0
    # default constructor
    def __init__(self, num, denom):
        Fraction.__counter += 1
        self.num = num
        self.denom = denom
            
    @classmethod
    def fromDecimal(cls, num):
        num = Decimal(num*100)
        denom = 100
        common = cls.__gcd(cls, num, denom)
        num = num // common
        denom = denom // common
        return cls(num, denom)
        
    # toString method
    def __str__(self):
        return str(self.num) + '/' + str(self.denom)
        
    # greatest common divisor method
    def __gcd(self, m, n):
        while m%n != 0:
            m, n = n, m%n
        return n
        
    # adding method
    def __add__(self, other): 
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom
        common = self.__gcd(new_num, new_denom)
        return Fraction(new_num//common, new_denom//common)

    # substitute method
    def __sub__(self, other): 
        new_num = self.num * other.denom - other.num * self.denom
        new_denom = self.denom * other.denom
        common = self.__gcd(new_num, new_denom)
        return Fraction(new_num//common, new_denom//common)

    # multiply method
    def __mul__(self, other): 
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        common = self.__gcd(new_num, new_denom)
        return Fraction(new_num//common, new_denom//common)

    # divide method
    def __truediv__(self, other): 
        new_num = self.num * other.denom
        new_denom = self.denom * other.num
        common = self.__gcd(new_num, new_denom)
        return Fraction(new_num//common, new_denom//common)
        
    # deleting (calling destructor)
    def __del__(self):
        Fraction.__counter -= 1
        
    @staticmethod
    def getCounter():
        return Fraction.__counter
   
   
def main():
    f1 = Fraction.fromDecimal(1.5)
    
    f2 = Fraction(4,3)
    
    print("Ilość obiektów tym momencie:", Fraction.getCounter())
    print("\nPierwszy ulamek:", f1)
    print("Drugi ulamek:", f2)
    print("\nWynik dodawania:", f1 + f2)
    print("Wynik odejmowania:", f1 - f2)
    print("Wynik mnożenia:", f1 * f2)
    print("Wynik dzielenia:", f1 / f2)
    
    del f1
    print("\nTestowanie czy obiekt został usunięty: ", end="")
    try:
       f1
    except NameError:
        print("Obiekt nie istnieje")
    else:
        print("Obiekt istnieje")
        
    print("Ilość obiektów tym momencie:",Fraction.getCounter())
       
if __name__ == "__main__":
    main()
