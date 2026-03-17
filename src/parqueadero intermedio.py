print('WELCOME TO PARKING ****')
bike = {}
auto ={}
totalbike = 0
totalauto = 0
for i in range (1, 3):
    plate = str(input('Enter the licensse plate: '))
    type = bool(input('enter the vehicle type if bike press=1, if auto press=0 '))
    hours = int(input('enter the hours in parking'))
    if type == 1:
        bike.update({'plate': plate, 'type':type, 'hours': hours})
        totalbike += 1 
    elif type == 0:
        auto.append({'plate': plate, 'type':type, 'hours': hours})
        totalauto += 1
totacostlbike = len(bike) * 2000
totacostlauto = len(auto) * 4000
print('total raised is: ', totacostlbike + totacostlauto)
print('the quantity of auto`s is: ', len(auto))
print('the cuantity of bike`s is: ', len(bike))
if totalbike > totalauto:
    print('the vehicle that paid the most was bike' )
else:
    print('The vehicle that paid the most was auto')

