#FIXED AND FINISHED


class Figura:
    
    def __init__(self,name):
        self.__name = name
        
    def getName(self):
        return self.__name
    
class Kolo(Figura):
    
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        
    
    def obwod(self):
        return 2 * 3.14 * self.radius
    

class Prostokat(Figura):
    
    def __init__(self, name, a, b):
        super().__init__(name)
        self.a = a
        self.b = b
        
    def obwod(self):
        return 2*self.a+2*self.b


class Kwadrat(Prostokat):
    
    def __init__(self, name, a):
        super().__init__(name, a, a)


class Wielokat(Figura):
    
    def __init__(self, name, *sides):
        super().__init__(name)
        self.sides = sides
        
    def obwod(self):
        perimeter = 0
        for x in self.sides:
            perimeter +=x
        return perimeter
    
    
    
    
    
def main():
    
    myFigures = [Kolo("Koło r=4", 4), Prostokat("Prostokat 2x4", 2, 4), Kwadrat("Kwadrat 2x2", 2), Wielokat("Wielokat 1x2x3x4x5", 1,2,3,4,5)]
    
    for x in myFigures:
        print("Figura:", x.getName())
        print("Obwód figury:", x.obwod())
    
    
    
if __name__ == "__main__":
    main()
