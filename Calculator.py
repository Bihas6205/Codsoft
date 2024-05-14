num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))
print("Enter the operation to be performed like +,-,*,/ :")
op=input()
if op=='+':
    print(num1," + ",num2," = ",num1+num2)
elif op=='-':
     print(num1," - ",num2," = ",num1-num2)
elif op=='*':
     print(num1," * ",num2," = ",num1*num2)
else:
     print(num1," / ",num2," = ",num1/num2)