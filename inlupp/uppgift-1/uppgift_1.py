'''
# Uppgift 1
# Skapa en funktion is_odd(x) som returnerar True om x är udda och False om x är jämnt.
# def funktions_namn(variabel_namn: datatyp) -> returtyp:
# Exempel: def is_odd(x: int) -> bool:
# Förklaring: Funktionens namn är is_odd och tar en parameter x av datatypen int. Funktionen returnerar en bool.

def is_odd(x: int) -> bool:
    """
    Skriv beskrivning här.
    """
    return x % 2 != 0

print (is_odd (10))
'''


my_list = [20, 30, 40, 50]
result = sum_list(my_list)
print(result) 
