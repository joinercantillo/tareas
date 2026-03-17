#task 1

frutas = ['mango', 'uva', 'lulo','mora', 'tomate']
frutas.append('pera')
print("se agrego una fruta", frutas)
frutas.remove('uva')
frutas.pop()
print(frutas)

#task 2

numeros = [4, 2, 7, 2, 9, 1, 2]
numeros.sort()
print(f"el numero 2 aparece ", numeros.count(2), "veces")
print(numeros)
print('el numero 7 aparece',numeros.index(7), 'veces')

#task 3

a = [1, 2, 3]
b = [4, 5, 6]
nuevalista = []

nuevalista = a.copy()
print(nuevalista)
nuevalista.extend(b)
print(nuevalista)
print('la lista final esl: \n', nuevalista)

#task 4

estudiantes = ['homero', 'lisa', 'bart', 'maggie']
print(estudiantes)
estudiantes.clear()
print(estudiantes)

#task 5
persona = {'nombre': 'ana', 'edad':25, 'ciudad':'bogota'}
print('la edad es ', persona.get('edad','desconocido'))
print('el numero de telefono es', persona.get('telefono','desconocido'))

#task 6
persona.update({'profesion':'estudiante'})
print(persona)
persona.update({'edad': 50})
print(persona)

#task 7

productos = {"pan": 1500, "leche": 3200, "huevos": 9000}

for i in productos.keys():
    print(i)
for i in productos.values():
    print(i)
for i in productos.items():
    print(i)

#task 8

d1 = {"a": 1, "b": 2}
d2 = {"b": 5, "c": 3}

d1.update(d2)
print(d1) #la variable "b" se actualizo y paso de valer 2  a valer 5

#task 9

dicc = {"bart": 14, "lisa": 13, "homero": 55, "marge":50}
triturado = dicc.popitem()
print(dicc)
print(triturado)


#task 10

estudiantes = [ {"nombre":"luis", "nota": 4.5}, {"nombre":"marta", "nota": 3.8}, {"nombre":"carlos", "nota": 4.2}]
print(estudiantes)
prom = sum(i["nota"] for i in estudiantes) / len(estudiantes)
print(prom)
maiornota = [i for i in estudiantes if i["nota"] > 4.0]
print(maiornota)
