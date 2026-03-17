print('bienvenido a peluqueria ****')
hora = int(input('hora de llegada del cliente(0-23): '))
if hora in range(6, 11):
    print('manana')
elif hora in range(12, 17):
    print('tarde')
elif hora in range(18, 22):
    print('noche')
else:
    print('fuera de horario')