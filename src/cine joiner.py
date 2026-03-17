print("BIENVENIDO AL CINE *****")
print("INGRESE SU EDAD: ")
edad = int(input())

if edad < 12:
    print("El precio de su boleta es: 8000")
elif edad in range(12, 59):
    print("El precio de su boleta es: 12000")
elif edad > 59:
    print("El precio de su boleta es: 9000")