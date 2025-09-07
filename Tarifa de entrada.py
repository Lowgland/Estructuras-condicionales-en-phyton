#Tarifa de entrada
edad=int(input("Ingresa tu edad: "))
if edad<12:
    print("El costo es de $50 ")
elif 12<=edad<17:
    print("El costo es de $80")
else:
    print("El costo de es $120")
