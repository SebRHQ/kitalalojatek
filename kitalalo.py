from random import randint
from time import sleep

helyesTalalat = 0
helytelenTalalat = 0
probalkozasok = 0
nyelvHelyesseg = False
ujra = True
print("[1] Hungarian")
print("[2] English")
print("[3] German")
nyelv = input("[❓] Please choose your language! (1/2/3): ")

while not nyelvHelyesseg:
    if nyelv == "1":
        nyelvHelyesseg = True
    elif nyelv == "2":
        nyelvHelyesseg = True
    elif nyelv == "3":
        nyelvHelyesseg = True
    else:
        print("[❌] Incorrect input!")
        nyelv = input("[❓] Please enter a number between 1 and 3: ")
nyelv = int(nyelv)
if nyelv == 1:
    print("[👋] Üdv!")

    while ujra:

        gondoltSzam = randint(1, 5)
        probalkozasok += 1
        print('[ℹ️] ', probalkozasok, '. Próbálkozás', sep='')
        print('[🤔] Gondoltam egy számra 1 és 5 között. Ki tudja találni? Sok sikert!\n')
        megadottSzam = int(input('[🔢] A gondolt számom: '))
        while not 1 <= megadottSzam <= 5:
            print("[❌] Hibás bevitel!")
            megadottSzam = int(input("[🔢] Kérem adjon meg egy számot 1 és 5 között: "))
        if megadottSzam == gondoltSzam:
            print('[🥳] Sikerült! Kitalálta! A gondolt szám tényleg', gondoltSzam, 'volt!')
            helyesTalalat += 1
        else:
            if gondoltSzam < megadottSzam:
                print('[😢] A gondolt számom kisebb mint a megadott száma volt! Az én számom', gondoltSzam, 'volt!')
                helytelenTalalat += 1
            else:
                print('[😭] A gondolt számom nagyobb mint a megadott száma volt! Az számom', gondoltSzam, 'volt!')
                helytelenTalalat += 1
        hibas = True
        while hibas:
            kerdes = input('[😊] Szeretné újra megpróbálni? (I/N): ')
            if kerdes.lower() == 'n':
                ujra = False
                hibas = False
            elif kerdes.lower() == 'i':
                hibas = False
            else:
                print('[❌] Hibás bevitel! Kérem használja a megadott formátumot.')
                sleep(1)
    print('[ℹ️] Statisztikák:')
    print('  ', probalkozasok, 'próbálkozás')
    print('   Sikeres találatok:', helyesTalalat)
    print('   Hibás találatok:', helytelenTalalat, '\n')
    print('   Össz pontszám:', helyesTalalat-helytelenTalalat, '\n')
    print('[👋] Viszlát!')
    sleep(10)
elif nyelv == 2:
    print("[👋] Welcome!")

    while ujra:
        gondoltSzam = randint(1, 5)
        probalkozasok += 1
        print('[ℹ️] Attempt', probalkozasok)
        print('[🤔] I thought of a number between 1 and 5. Can guess it? Good luck!\n')
        megadottSzam = int(input('[🔢] My guess: '))
        while not 1 <= megadottSzam <= 5:
            print("[❌] Incorrect input!")
            megadottSzam = int(input("[🔢] Please enter a number between 1 and 5: "))
        if megadottSzam == gondoltSzam:
            print('[🥳] You guessed it! The thought number really was', gondoltSzam, '!')
            helyesTalalat += 1
        else:
            if gondoltSzam < megadottSzam:
                print('[😢] The thought number was smaller than the given number! My number is', gondoltSzam, '!')
                helytelenTalalat += 1
            else:
                print('[😭] The thought number was bigger than the given number! My number is', gondoltSzam, '!')
                helytelenTalalat += 1
        hibas = True
        while hibas:
            kerdes = input('[😊] Would you like to try it again? (Y/N): ')
            if kerdes.lower() == 'n':
                ujra = False
                hibas = False
            elif kerdes.lower() == 'y':
                hibas = False
            else:
                print('[❌] Incorrect input! Please use the format provided.')
                sleep(1)
    print('[ℹ️] Statistics:')
    print('  ', probalkozasok, 'attempt')
    print('   Correct guesses:', helyesTalalat)
    print('   Inorrect guesses:', helytelenTalalat, '\n')
    print('   Overall score:', helyesTalalat-helytelenTalalat, '\n')
    print('[👋] Bye!')
    sleep(10)
else:
    print("[👋] Willkommen!")

    while ujra:
        gondoltSzam = randint(1, 5)
        probalkozasok += 1
        print('[ℹ️] Versuchen', probalkozasok)
        print('[🤔] Ich dachte an eine Zahl zwischen 1 und 5. Kannst du sie erraten? Viel Glück!\n')
        megadottSzam = int(input('[🔢] Meine Vermutung: '))
        while not 1 <= megadottSzam <= 5:
            print("[❌] Falsche Eingabe!")
            megadottSzam = int(input("[🔢] Bitte geben Sie eine Zahl zwischen 1 und 5 ein: "))
        if megadottSzam == gondoltSzam:
            print('[🥳] Du hast es erraten! Die Gedankenzahl war wirklich', gondoltSzam, '!')
            helyesTalalat += 1
        else:
            if gondoltSzam < megadottSzam:
                print('[😢] Die gedachte Zahl war kleiner als die angegebene Zahl! Meine Nummer ist', gondoltSzam, '!')
                helytelenTalalat += 1
            else:
                print('[😭] Die gedachte Zahl war größer als die angegebene Zahl! Meine Nummer ist', gondoltSzam, '!')
                helytelenTalalat += 1
        hibas = True
        while hibas:
            kerdes = input('[😊] Möchten Sie es noch einmal versuchen? (J/N): ')
            if kerdes.lower() == 'n':
                ujra = False
                hibas = False
            elif kerdes.lower() == 'j':
                hibas = False
            else:
                print('[❌] Falsche Eingabe! Bitte verwenden Sie das bereitgestellte Format.')
                sleep(1)
    print('[ℹ️] Statistiken:')
    print('   Alle Versuche:', probalkozasok)
    print('   Richtige Vermutungen:', helyesTalalat)
    print('   Falsche Vermutungen:', helytelenTalalat, '\n')
    print('   Gesamtpunktzahl:', helyesTalalat-helytelenTalalat, '\n')
    print('[👋] Tschüss!')
    sleep(10)
