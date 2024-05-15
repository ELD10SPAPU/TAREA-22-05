prom = 0
altura = 0
n = 0

while altura >= 0:
    print("Ingrese (0) para salir")
    altura = float(input("Ingrese la altura: "))
    if altura == 0:
        break
    prom = prom + altura
    n = n + 1

prom = prom/n
print("El promedio de alturas es: ", prom)