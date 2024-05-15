sueldo = 0
contmas = 0
contmenos = 0
sueldototal = 0

while sueldo >= 0:
    print("Ingrese (-1) para salir")
    sueldo = int(input("Ingrese el sueldo: "))
    if sueldo < 0:
        break

    if sueldo >= 500000:
        contmenos = contmenos + 1

    if sueldo > 900000:
        contmas = contmas + 1
    
    sueldototal = sueldototal + sueldo

print("La cantidad de empleados que cobran entre $500.000 y $900.000 es: ", contmenos)
print("la cantidad de empleados que cobran mas de $900.000 es: ", contmas)
print("Lo que gasta la empresa en total en sueldos es de: ", sueldototal)