'''
def function_name(arg):
     #stmts
     return
function_name(para)
'''

'''
def wish(name):
    print(f'Welcome to the python couse {name}!')
wish('subbu')
wish('praneeth')
wish('sai durga')
'''

'''
def iseven(num):
    if num%2==0:
        return f"{num} - Even Number"
print(iseven(2))
print(iseven(102))
'''
'''
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact*=1
        return fact

num = int(input("Enter the Number"))
print("Factorial:",factorial(num))

  '''

'''
def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num} - Not prime Number"
    return f"{num} - Prime Number"

num = int(input("Enter the Number: "))
print(isprime(num))
'''

'''
types of arguements
1.postional arguement
2.keyword arguement
3.default arguement
4.var argument
'''
'''
#1.postional arguement

def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)

display('subbu','subbu@gmail.com','subbu@123')
display('subbu@gmail.com','subbu','subbu@123')
display('subbu@gmail.com','subbu@123','subbu')
'''
'''
#keyword arguement

def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)

display(name='subbu',email='subbu@gmail.com',pwd='subbu@123')
display(email='subbu@gmail.com',name='subbu',pwd='subbu@123')
display(email='subbu@gmail.com',pwd='subbu@123',name='subbu')
'''


'''
#default parameter

def display(name,email,pwd=''):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)

display('subbu','subbu@gmail.com','subbu@123')
display('subbu@gmail.com','subbu')
'''
'''
#variable arguement

def display(*names):
    print("Name:",names)

display('subbu','dinesh','naresh','akhil','nagendra')
display('subbu','dinesh','naresh')
display('subbu','dinesh','naresh','akhil')
display('subbu')
display('subbu','dinesh')

'''

def display(**names):
    print("Name:",names)


display(k1='subbu',k2='dinesh',k3='naresh')
display(k1='subbu',k2='dinesh')
display(k1='subbu',k2='dinesh',k3='naresh',k4='akhil')
display(k1='subbu')




























































    
