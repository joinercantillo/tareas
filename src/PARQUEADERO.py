print('cauntas horas estuvo el vehiculo en el estacionamiento?')
horas = int(input())
extras = 3000

if horas == 1:
    print('el precio es: ', 5000)
elif horas > 1:
    print('el valor a pagar es: ',5000 + (horas -1) * 3000 )