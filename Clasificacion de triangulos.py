#Programa de Clasificación de triangulos
l1=int(input("Ingresa la primer longitud del triangulo: "))
l2=int(input("Ingresa la segunda longitud del triangulo: "))
l3=int(input("Ingresa la terceera longitud del triangulo: "))
if l1==l2 and l2==l3:
    print("El triangulo es equilátero")
elif l1==l2 or l1==l3 or l2==l3:
    print("El triangulo es isósceles")
else:
    print("El triangulo es escaleno")
