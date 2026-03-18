print("BIENVENIDO A CAFETERIA ****")
bebidas = [{"name": "cafe", "price": 4000}, {"name": "te", "price": 3500}, {"name": "jugo", "price": 5000}]
for i,opcion in enumerate(bebidas, start=1):
    print(f'{i}, {opcion ["name"]}: {opcion ["price"]}')
opcion_select = int(input("escoja una opcion(1-3): "))
quantity = int(input("ingrese la cantidad: "))

print(f'your total is: {bebidas[opcion_select-1]["price"]*quantity}')
