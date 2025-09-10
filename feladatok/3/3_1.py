"""
1. Feladat
Thonny fejlesztői környezetben készíts egy rövid programot, amely
kommentként tartalmazza a program funkciójának leírását,
konstansként tárolja PI értékét,
egy másik változóban tárolja egy kör sugarának nagyságát 
(cm-ben megadva),
kiszámolja és a képernyőre kiírja a kör kerületét és területét!
"""

# Program a kör kerületének és területének kiszámítására
# szorzás *
PI = 3.14
radius = 5  # cm
circumference = 2 * PI * radius
area = PI * radius * radius

print(f'Kör kerülete: {circumference} cm')
print(f'Kör területe: {area} cm²')
# print(f'Kör területe: {PI * radius ** 2} cm²')