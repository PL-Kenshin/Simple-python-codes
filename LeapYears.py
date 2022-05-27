#FINISHED

print("Podaj przedzial lat do obliczenia lat przestępnych")
yearMin = int(input("Początek: "))
yearMax = int(input("Koniec: "))

leapYears = [x for x in range(yearMin, yearMax) if (x % 400 == 0) or (x % 4 ==0) and (x % 100 != 0)]

print("\nLata przestępne z podanego zakresu to:\n" + str(leapYears))
