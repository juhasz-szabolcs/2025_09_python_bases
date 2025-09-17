"""
4️ Három szám közül a legnagyobb
Kérj be három egész számot, és írd ki, melyik a legnagyobb.
"""

elso = int(input("Kérlek add meg az első számot! "))
masodik = int(input("Kérlek add meg a második számot! "))
harmadik = int(input("Kérlek add meg a harmadik számot! "))

if elso > masodik and elso > harmadik:
    print(f"Legnagyobb szam az első szám: {elso}")
elif masodik > elso and masodik > harmadik:
    print(f"Legnagyobb szam a második szám: {masodik}")
elif harmadik > elso and harmadik > masodik:
    print(f"Legnagyobb szam a harmadik szám: {harmadik}")