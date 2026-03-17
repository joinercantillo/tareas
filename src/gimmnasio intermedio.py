personas = {}
bajo = {}
intermedio = {}
alto = {}


for i in range(1, 3):
    print('--- DATOS DEL CLIENTE ---')
    nombre = input('Ingrese el nombre: ')
    dias = int(input('Ingrese días: '))
    minutos = int(input('Minutos por día: '))
    
    
    personas[nombre] = dias

print("\nDiccionario completo:", personas)


for nombre, dias in personas.items():
    if dias < 3:
        bajo[nombre] = dias
        print("Clientes con pocos días:", bajo)
    if dias in range(3, 4):
        intermedio[nombre] = dias
        print("Clientes con pocos días:", intermedio)
    if dias > 4:
        alto[nombre] = dias
        print("Clientes con pocos días:", alto)


