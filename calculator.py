print("-----CALCULATOR------")
print("Enter a number 1:")
num1=int(input())
print("Enter a number 2:")
num2=int(input())
print("These are the operator you can use:")
print("1.Addition")
print("2.subtration")
print("3.multiplication")
print("4.division")
print("5.modulus")
operator=input("please choose an option from these (1,2,3,4,5):")
if operator == "1":
   # print(num1, "+", num2, "=", num1+num2)
 print("this is an addition operator")
print("sum of two numbers is:",num1+num2)
if operator=="2":
    print("this is an subtration operation")
    print("the difference of two number is:",num1-num2)
if operator=="3":
    print("this is an multiplication operation")
    print("the multiplication of two number is:",num1*num2)
if operator=="4":
    print("this is an division operation")
    print("the division of two number is:",num1/num2)
if operator=="5":
    print("this is an modulus operation")
    print("the modulus of two number is:",num1%num2)






