print('BIENVENIDO A CAFETERIA ****')
print('TENEMOS LOS SIGUIENTES HELADOS, SELECCIONE EL DE SU PREFERENCIA: \n -1- cafe \n -2- capuchino \n -3- pastel')
option = -1
validation = -1
productos = {'cafe': 4000, 'capuchino': 7000, 'pastel':6000}
compras = []
while validation != 0:
    print('TENEMOS LOS SIGUIENTES HELADOS, SELECCIONE EL DE SU PREFERENCIA: \n -1- cafe \n -2- capuchino \n -3- pastel')
    option = int(input())
    if option == 1:
        cantidad = int(input('Cuantos quiere comprar?'))
        total = cantidad * productos['cafe'] 
        compras.append(total)
    elif option == 2:
        cantidad = int(input('Cuantos quiere comprar?'))
        total = cantidad * productos['capuchino'] 
        compras.append(total)
    elif option == 3:
        cantidad = int(input('Cuantos quiere comprar?'))
        total = cantidad * productos['pastel'] 
        compras.append(total)
    
    validation = int(input('quiere agregar otro producto? y=1/n=0: ' ))
    final = sum(compras)
    if final > 20000:
        final = final * 0.2
    print(final)

