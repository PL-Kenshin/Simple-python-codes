#FIXED AND FINISHED
import random 

print("Witaj w grze 'Zgadnij liczbę'!")
print("\nMam na myśli pewną liczbę z zakresu od 1 do 10")
print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.")

chances = 3
number = random.randint(1, 10)

while chances > 0:
    guess = int(input("Podaj liczbę: "))
    chances = chances - 1
    if guess == number:
        print("Wygrałeś, ta liczba to: " + str(number))
        break
    elif guess > number:
        if chances > 0:
            print("Za duża")
    else:
        if chances > 0:
            print("Za mała")
else:
    print("Przegrałeś, ta liczba to: " + str(number))
