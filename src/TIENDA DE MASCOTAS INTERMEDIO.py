print('WELCOME TO PET STORE')
food = []
toy = []
accesory = []
pricefood = []
pricetoy = []
priceaccesory = []

for i in range (1,4):
    category = int(input('what type of product do you want to buy? \n -1- food \n -2- toy \n -3- accesory \n'))
    if category == 1:
        food.append(1)
        Value = int(input('what`s the value of the product?: '))
        pricefood.append(Value)
    elif category == 2:
        toy.append(1)
        Value = int(input('what`s the value of the product?: '))
        pricetoy.append(Value)
    elif category == 3:
        accesory.append(1)
        Value = int(input('what`s the value of the product?: '))
        priceaccesory.append(Value)

print(sum(pricefood), '$ worth of food was sold \n' )
print(sum(pricetoy), '$ worth of toys was sold \n' )
print(sum(priceaccesory), '$ worth of accessories was sold \n')
if sum(priceaccesory) > sum(pricefood) and sum(priceaccesory) > sum(pricetoy):
    print("la categoria en la que mas se vendio fue accesorio")
elif sum(pricefood) > sum(priceaccesory) and sum(pricefood) > sum(pricetoy):
    print("la categoria en la que mas se vendio fue food")
elif sum(pricetoy) > sum(pricefood) and sum(pricetoy) > sum(priceaccesory):
    print("la categoria en la que mas se vendio fue toy")


    
