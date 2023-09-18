from random import randint
from time import sleep

helyesInput = False
helyesTalalat = 0
helytelenTalalat = 0
probalkozasok = 0
nyelvHelyesseg = False
ujra = True

print("[1] Hungarian")
print("[2] English")
print("[3] German")

nyelv = input("[❓] Please choose your language! (1/2/3): ")

while not helyesInput:
    if nyelv.isdigit():
        nyelv = int(nyelv)
        if 1 <= nyelv <= 3:
            helyesInput = True
        else:
            print("[❌] Incorrect input!")
            nyelv = input("[❓] Please enter a number between 1 and 3: ")
    else:
        print("[❌] Incorrect input!")
        nyelv = input("[❓] Please enter a number between 1 and 3: ")

if nyelv == 1:
    print("[👋] Üdv!")

    while ujra:
        gondoltSzam = randint(1, 5)
        probalkozasok += 1
        print('[ℹ️] ', probalkozasok, '. Próbálkozás', sep='')
        print('[🤔] Gondoltam egy számra 1 és 5 között. Ki tudja találni? Sok sikert!\n')
        megadottSzam = input('[🔢] A gondolt számom: ')
        helyesInput = False
        while not helyesInput:
            if megadottSzam.isdigit():
                megadottSzam = int(megadottSzam)
                if 1 <= megadottSzam <= 5:
                    helyesInput = True
                else:
                    print("[❌] Hibás bevitel!")
                    megadottSzam = input('[🔢] Kérem adjon meg egy számot 1 és 5 között: ')
            else:
                print("[❌] Hibás bevitel!")
                megadottSzam = input('[🔢] Kérem adjon meg egy számot 1 és 5 között: ')

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
        helyesInput = False
        while not helyesInput:
            kerdes = input('[😊] Szeretné újra megpróbálni? (I/N): ')
            if kerdes.lower() == 'n':
                ujra = False
                helyesInput = True
            elif kerdes.lower() == 'i':
                helyesInput = True
            else:
                print('[❌] Hibás bevitel! Kérem használja a megadott formátumot.')
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
        megadottSzam = input('[🔢] My guess: ')
        helyesInput = False
        while not helyesInput:
            if megadottSzam.isdigit():
                megadottSzam = int(megadottSzam)
                if 1 <= megadottSzam <= 5:
                    helyesInput = True
                else:
                    print("[❌] Incorrect input!")
                    megadottSzam = input("[🔢] Please enter a number between 1 and 5: ")
            else:
                print("[❌] Incorrect input!")
                megadottSzam = input("[🔢] Please enter a number between 1 and 5: ")

        if megadottSzam == gondoltSzam:
            print('[🥳] [🥳] You guessed it! The thought number really was', gondoltSzam, '!')
            helyesTalalat += 1
        else:
            if gondoltSzam < megadottSzam:
                print('[😢] The thought number was smaller than the given number! My number is', gondoltSzam, '!')
                helytelenTalalat += 1
            else:
                print('[😭] The thought number was bigger than the given number! My number is', gondoltSzam, '!')
                helytelenTalalat += 1
        helyesInput = False
        while not helyesInput:
            kerdes = input('[😊] Would you like to try it again? (Y/N): ')
            if kerdes.lower() == 'n':
                ujra = False
                helyesInput = True
            elif kerdes.lower() == 'y':
                helyesInput = True
            else:
                print('[❌] Incorrect input! Please use the format provided.')
    print('[ℹ️] Statistics:')
    print('  ', probalkozasok, 'attempt')
    print('   Correct guesses:', helyesTalalat)
    print('   Inorrect guesses:', helytelenTalalat, '\n')
    print('   Overall score:', helyesTalalat-helytelenTalalat, '\n')
    print('[👋] Bye!')
    sleep(10)
elif nyelv == 3:
    print("[👋] Willkommen!")

    while ujra:
        gondoltSzam = randint(1, 5)
        probalkozasok += 1
        print('[ℹ️] Versuchen', probalkozasok)
        print('[🤔] Ich dachte an eine Zahl zwischen 1 und 5. Kannst du sie erraten? Viel Glück!\n')
        megadottSzam = input('[🔢] Meine Vermutung: ')
        helyesInput = False
        while not helyesInput:
            if megadottSzam.isdigit():
                megadottSzam = int(megadottSzam)
                if 1 <= megadottSzam <= 5:
                    helyesInput = True
                else:
                    print("[❌] Falsche Eingabe!")
                    megadottSzam = input('[🔢] Meine Vermutung: ')
            else:
                print("[❌] Falsche Eingabe!")
                megadottSzam = input('[🔢] Meine Vermutung: ')

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
        helyesInput = False
        while not helyesInput:
            kerdes = input('[😊] Möchten Sie es noch einmal versuchen? (J/N): ')
            if kerdes.lower() == 'n':
                ujra = False
                helyesInput = True
            elif kerdes.lower() == 'j':
                helyesInput = True
            else:
                print('[❌] Falsche Eingabe! Bitte verwenden Sie das bereitgestellte Format.')
    print('[ℹ️] Statistiken:')
    print('   Alle Versuche:', probalkozasok)
    print('   Richtige Vermutungen:', helyesTalalat)
    print('   Falsche Vermutungen:', helytelenTalalat, '\n')
    print('   Gesamtpunktzahl:', helyesTalalat-helytelenTalalat, '\n')
    print('[👋] Tschüss!')
    sleep(10)
