print('bienvendo a tienda deportiva ****')
productos = []
for i in range(1,7):
    precio = int(input('ingrese el precio del producto: '))
    
    productos.append(precio)

mayores = [i for i in productos if i > 1000]
print(mayores) 