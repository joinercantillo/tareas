print("BIENVENIDO A TIENDA DE MASCOTAS ****")
animal = {"gato":"se recomienda la compra de alimento Cat Chow", "conejo":"se recomienda la compra de alimento solla para conejos", "perro":"se recomienda la compra de alimento Dog Chow"}
print("seleccione el animal para el cual quiere comprar alimento: \n -1- gato \n -2- perro \n -3- conejo")
option = int(input())
if option == 1:
    print(["gato"])
elif option == 2:
    print(["perro"])
elif option == 3:
    print(["conejo"])