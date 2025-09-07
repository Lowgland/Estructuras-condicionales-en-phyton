#Conversor de calificaciones
cal=int(input("Ingresa la calificación entre 0-100: "))
if cal>100 or cal<0:
    print("Calificacion erronea")
elif cal<60:
    print("F")
elif 69>=cal>=60:
    print("D")
elif 79>=cal>=70:
    print("C")
elif 89>=cal>=80:
    print("B")
else:
    print("A")
