num1= int(input("Type the first number: "))
num2=int(input("Type the second number: "))

election=0

while election != 6:
    print("""Indicate the operation to be performed:
          1) Addition
          2) Subtraction
          3) Multiplication
          4) Division
          5) Change values
          6) Exit
          """)
    
    election = int(input())
    if election==1:
        print(" ")
        print("The result of adding:",num1,"+",num2,"=",num1+num2)

    if election==2:
        print(" ")
        print("The result of subtracting:",num1,"-",num2,"=",num1-num2)

    if election==3:
        print(" ")
        print("The result of multiplying:",num1,"*",num2,"=",num1*num2)

    if election==4:
        print(" ")
        print("The result of dividing:",num1,"/",num2,"=",num1/num2)

    if election==5:
        num1= int(input("Type the first number: "))
        num2=int(input("Type the second number: "))
    
    if election==6:
        print("Thank you for using the calculator. Made by Edwin")