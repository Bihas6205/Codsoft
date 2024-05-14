
# <img src="https://github.com/Bihas6205/Codsoft/blob/main/pngwing.com.png" height="40px" width="40px"> Calculator  
**Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result**  

```python
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
           
```

**Output**
```
Enter Number 1: 2
Enter Number 2: 3
Enter the operation to be performed like +,-,*,/ :
+
2  +  3  =  5
```
