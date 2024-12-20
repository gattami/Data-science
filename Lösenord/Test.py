'''''
text = "   Python är roligt!   "
rensad_text = text.strip()
print(rensad_text)

text = "python är roligt!"
print(text.replace("roligt", "fantastiskt"))

text = "python är bäst"
print(text.replace("bäst", "sådär"))

namn = "Mila jackson"
ålder = "39"
print (f"hej mitt namn är {namn} jag är {ålder} år GAMMAL.")



produkt = {"namn": "Laptop", "pris": 10000, "lager": 50}
print(f"Produktens namn: {produkt['namn']}")
produkt["kategori"] = "Elektronik"
print(f"Ny kategori tillagd: {produkt['kategori']}")
produkt["lager"] = 40
print(f"Uppdaterat lager: {produkt['lager']}")
print("Uppdaterad produktinformation:", produkt)


age = int(input("Ange din ålder: " ))
if age > 18:
 print("GÅ UT, DU FÅR INTE VARA HÄR")


telefonnummer = input("Ange ditt telefonnummer: ")


telefonnummer = input("Ange ditt telefonnummer: ")

if len(telefonnummer) >= 10 and telefonnummer.isdigit():
    print(f"Ditt telefonnummer är: {telefonnummer}")
else:
    print("Telefonnumret måste vara minst 10 siffror och endast innehålla siffror!")


telefonnummer = input("Ange ditt telefonnummer: ")
if telefonnummer.isdigit() and len(telefonnummer) >= 10:
    print(f"Ditt telefonnummer är: {telefonnummer}")
else:
    print("Telefonnumret måste vara minst 10 siffror och endast innehålla siffror!")
print("Telefonnumret måste vara minst 10 siffror och endast innehålla siffror!")


password = ""
while password != "hemligt":   #startar loop, != betyder "inte lika med" i Python. Den används för att jämföra två värden och kontrollera om de inte är lika. Om värdena inte är lika, returnerar den True (sant), annars returnerar den False (falskt).
    password = input("Ange lösenord: ") 
    print("Rätt lösenord!") 
    if password != "hemligt": 
        print("Fel lösenord, försök igen!")
'''
password = ""
while password == "abc":
    password = input("Ange password: ")
    if password == "abc":
        print("Fel password! Försök igen!")
print("Inloggad")   
'''



