antalMånadÅr = 10
antalÅr = 3
Bidrag = 1250

Pengar = antalMånadÅr * antalÅr * Bidrag

print("Är du född mellan juli och september? ja/nej")
FöddMånad = input(str())

if FöddMånad == "ja":
    Pengar = Pengar - (Bidrag // 2)
    print("Under 3 år får du " + (str(Pengar)) + "kr")
elif FöddMånad == "nej":
    print("Under 3 år får du " + (str(Pengar)) + "kr")
else:
    print("Skriv med små bokstäver")