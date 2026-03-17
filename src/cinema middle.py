print('welcome to the cinema')
people = []
validation = -1
capacity = int(input('whats the cinema capacity?'))
while validation != 0:
    age = int(input('enter the age: '))
    validation = int(input('do you want add another person?y=1/n=0 \n'))
    people.append(age)

print('total persons: ', len(people))
menor = [i for i in people if i < 18]
adult = [i for i in people if i in range (18, 60)]
senior = [i for i in people if i > 59] 
cont = len(people) + len(senior)
print('the number of children is: ', len(menor))
print('the number of adults is: ', cont)
print('the number of seniors is: ', len(senior))
if len(people) > capacity:
    print('cinema is full')





