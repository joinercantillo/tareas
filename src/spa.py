print('BIENVENIDO AL SPA *****')
print('TENEMOS LOS SIGUIENTES SERVICIOS ' \
'\n -1- massage ' \
'\n -2- facial ' \
'\n -3- manicure ' \
'\n escoja una de las opciones' )
services = {'massage':'massage',
            '1':'massage',
            'facial':'facial',
            '2':'facial',
            'manicure':'manicure',
            '3':'manicure'}
            
service = input().lower().strip()
result = services.get(service, 'servicio no encontrado')
print(result)




