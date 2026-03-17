print("BIENVENIDO A CAFETERIA ****")
print("NUESTRAS BEBIDAS SON: \n -1- cafe=4000 \n -1- te = 3500 \n -1- jugo = 5000 ")
bebidas = {"cafe": 4000, "te": 3500, "jugo":5000}
opcion = int(input("escoja una opcion(1-3): "))
if opcion == 1:
    print("cuantas unidades necesita?")
    sum1 = int(input())
    print("su cuenta final es: ", sum1 * bebidas["cafe"] )
elif opcion == 2:
    print("cuantas unidades necesita?")
    sum2 = int(input())
    print("su cuenta final es: ", sum2 * bebidas["te"] )
elif opcion == 3:
    print("cuantas unidades necesita?")
    sum3 = int(input())
    print("su cuenta final es: ", sum3 * bebidas["jugo"] )
