clases =int(input('BIENVENIDO A LA ACEDEMIA DE BAILE **** \n cuantas veces asistio a clase el estudiante en este mes?'))
if clases < 5:
    print('asistencia baja')
elif clases in range (5, 8):
    print('asistencia media')
elif clases > 9:
    print('asistencia alta')
    