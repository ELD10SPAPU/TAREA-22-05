preguntas=int(input("Ingrese la cantidad de preguntas: "))
respuestas=int(input("Ingrese la cantidad de preguntas correctas: "))
nota = respuestas/preguntas
if nota >= 0.95:
    print("Obtuvo el nivel maximo")
else:
    if nota >= 0.7:
        print("Obtuvo el nivel medio")
    else:
        if nota >= 0.4:
            print("Obtuvo el nivel regular")
        else:
            if nota <0.4:
                print("Fuera de nivel")