#Calculator API

#Version: 1.1

###SETUP###
#Import API: "import assets.APIs.simple_calcualtor as sc"
#Use "sc.addition(num1, num2) for addition"
#Use "sc.subtraction(num1, num2) for subtraction"
#Use "sc.multiplication(num1, num2) for multiplication"
#Use "sc.division(num1, num2) for division" 


def addition(num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    answer = num1+num2
    return answer

def subtraction(num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    answer = num1-num2
    return answer

def multiplication(num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    answer = num1*num2
    return answer

def division(num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    answer = num1/num2
    return answer