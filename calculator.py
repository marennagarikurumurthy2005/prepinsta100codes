
import math
def calculation(num1,op,num2):
    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='*' or op=='x' or op=='X':
        return num1*num2
    elif op=='/':
        if num2==0:
            return 'divisor cant be zero'
        else:
            return num1/num2
    else:
        return "something went wrong"




input1=int(input("Enter Number 1"))
operator=input("enter the operator to do operation: \n addition \t (+) \n substraction  \t (-) \n multiplication (* or X) \n division  \t (/) \n Enter your choice:")
input2=int(input("Enter number 2"))
cal=calculation(input1,operator,input2)
print(cal)
