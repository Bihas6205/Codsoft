# <img src="https://github.com/Bihas6205/Codsoft/blob/main/pngwing.com.png" height="40px" width="40px"> Password generator  
**A password generator is a useful tool that generates strong and
random passwords for users. This project aims to create a
password generator application using Python, allowing users to
specify the length and complexity of the password.**
  

```python
import string
import random
length=int(input("Enter the desired length of the password: "))
pass1=''.join(random.choices(string.ascii_letters,k=length))
print("The Random generated Password is: ",pass1)

```

**Output**
```
Enter the desired length of the password: 10
The Random generated Password is:  LIZMCglmOW
```
