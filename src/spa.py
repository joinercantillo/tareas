print('BIENVENIDO AL SPA *****')
print('TENEMOS LOS SIGUIENTES SERVICIOS \n -1- masaje \n -2- facial \n -3- manicure \n escoja una de las opciones' )
servicio = str(input())
if servicio == 'masaje' or servicio == 'facial' or servicio == 'manicure':
    print('servicio disponible')
else:
    print('el servicio no existe')
