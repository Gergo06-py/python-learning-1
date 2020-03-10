forras = open("EUcsatlakozas.txt", "r", encoding="latin2")

forras.readline()

matrix = [sor.strip().split(";") for sor in forras]

#3

x = 1
for i in matrix:
    x += matrix.count(i)
print("""
3. feladat
EU tagállamainak száma:""", x, "db")

#4

csat1 = 0
for i in matrix:
    d = i[1].split(".")
    if d[0] == "2007":
        csat1 += 1

print("""
4. feladat
2007-ben""", csat1, "ország csatlakozott.")

#5

for i in matrix:
    if i[0] == 'Magyarország':
        d = i[1]

print("""
5. feladat
Magyarország csatlakozásának dátuma:""", d)

#6

csat2 = False
for i in matrix:
    d = i[1].split(".")
    if d[1] == "05":
        csat2 = True
        
if csat2:
    print("""
6. feladat
Májusban volt csatlakozás!""")
else:
    print("""
6. feladat
Májusban nem volt csatlakozás!""")

#7 TESZT
lko = ""
for i in range(csat1 - 1):
    d1 = matrix[i][1].split(".")
    d2 = matrix[i + 1][1].split(".")
    if d2 > d1:
        lko = matrix[i + 1][0]

print("""
4. feladat
2007-ben""", lko, "ország csatlakozott.")
