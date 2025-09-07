#Comparación de tres números
n1=int(input("Ingresa el primer número: "))
n2=int(input("Ingresa el segundo número: "))
n3=int(input("Ingresa el tercer número: "))
if n1==n2 and n2==n3:
    print("Todos los numeros son iguales")
else:
    num_Mayor=max(n1,n2,n3)
    num_Menor=min(n1,n2,n3)
    print("El numero mayor es: ",num_Mayor)
    print("El numero menor es: ",num_Menor)
