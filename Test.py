
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


skapa en dictionary för en produkt
produkt ={"namn: " Laptoop", "pris": 10000, "lager":50}

produkt = {"namn": "Laptop", "pris": 10000, "lager": 50}
print(f"Produktens namn: {produkt['namn']}")
produkt["kategori"] = "Elektronik"
print(f"Ny kategori tillagd: {produkt['kategori']}")
produkt["lager"] = 40
print(f"Uppdaterat lager: {produkt['lager']}")
print("Uppdaterad produktinformation:", produkt)