#task 2

print("BIENVENIDO AL GIMNASIO **** ")
print("INGRESE SU EDAD: ")
edad = int(input())

if edad < 13:
    print("no puede ingresar")
elif edad in range(13, 17):
    print("clase juvenil")
elif edad in range(17, 60):
    print("clase general")
elif edad > 59:
    print("clase senior")
    