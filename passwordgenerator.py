import string
import random
length=int(input("Enter the desired length of the password: "))
pass1=''.join(random.choices(string.ascii_letters,k=length))
print("The Random generated Password is: ",pass1)
