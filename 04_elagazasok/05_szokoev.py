"""
5️ Szökőév ellenőrző
Kérj be egy évet, és írd ki, hogy szökőév-e.
    (Szökőév, ha osztható 4-gyel, de nem 100-zal, kivéve ha 400-zal is osztható.)
"""

year = int(input("Kérlek adj meg egy évet! "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Szökőév")
else:
    print("Nem szökőév")