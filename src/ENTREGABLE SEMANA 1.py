DEFINITIVO SEMANA 1



#TASK 2: DATA ENTRY, THE USER ENTERS THE DATA OFF THE PRODUCT.

 

name = str(input("Enter the product name: "))

cost = float(input("Enter product cost: "))

while cost <= 0:

    cost = float(input("ENTER VALID VALUE: "))

   

quantity = int(input("Enter product amount: "))

while quantity <= 0:

    quantity = float(input("ENTER VALID VALUE: "))

totalcost = cost * quantity

 

print("Product:", name)

print("Cost: ", cost)

print("Stock: ", quantity)

 

#TASK 3 MATHEMATICAL OPERATION: THE CORRESPONDING OPERATIONS ARE PERFORMED TO FIND THE TOTAL COST OF EACH PRODUCT

 

validation = int(input("he information is correct?(y=1/n=0) "))

 

 

while validation == 0:

        name = str(input("Enter the product name:: "))

        cost = float(input("Enter product cost: "))

        while cost <= 0:

            cost = float(input("ENTER VALID VALUE: "))

        quantity = int(input("Enter product amount "))

        while quantity <= 0:

            quantity = float(input("ENTER VALID VALUE: "))

        validation = int(input("The information is correct?(y=1/n=0) "))

if validation == 1:

  

    utputString = str

#TASK 4 SHOW THE RESULTS ON TERMINAL

outputString = ("Product: " + name +

                " /cost: " + str(cost) + " /Stock: " + str(quantity) +

                 " /total: " + str(totalcost) )

print(outputString)

 

# THE PROGRAM TAKES THE DATA THAT THE USER PROVIDES ABOUT THE NAME, QUANTITY, AND PRICE OF A PRODUCT; ALLOWING THE USER TO CORRECT THE INFORMATION ENTERED, USING THE LOOP WHILE THE VALIDATION VARIABLE IS 0, THE USER CORRECTS THE INFORMATION OF THEIR PRODUCT, BUT IF THE VALIDATION VARIABLE IS 1, IT THEN DISPLAYS THE TOTAL VALUE FOR EACH PURCHASE MADE.

