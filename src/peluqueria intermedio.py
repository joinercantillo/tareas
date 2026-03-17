print('WELCOME TO BARBER ****')
quantitys = []
maxservice = []
price = []
for i in range(1, 8):
    name = str(input('enter the client`s name: '))
    service = int(input('select a service \n -1- hair cut \n -2- hair brushing \n -3- hair dye'))
    quantitys.append(1)
    if service == 1:
        maxservice.append(1)
    elif service == 2:
        maxservice.append(2)
    elif service == 3:
        maxservice.append(3)
    values = int(input('enter the price of that service'))
    price.append(values)
sum1 = maxservice.count(1)
sum2 = maxservice.count(2)
sum3 = maxservice.count(3)
print('total of the day: ', sum(price))
print('the quantity of clients is: ', sum(quantitys))

if sum1 > sum2 and sum1 > sum3:
    print('the service most wanted is hair cut ')
elif sum2 > sum1 and sum2 > sum3:
    print('the service most wanted is hair brushing ')
elif sum3 > sum1 and sum3 > sum2:
    print('the service most wanted is hair dye')