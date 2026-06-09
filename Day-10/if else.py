Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
data = {
    'ramakanth':{'status':True,'python':98,'mysql':95,'flask':94},
    'prakash':{'status':True,'python':78,'mysql':65,'flask':84},
    'naresh':{'status':False,'python':None,'mysql':None,'flask':None},
    'vamsi':{'status':True,'python':68,'mysql':55,'flask':64},
    'rishi':{'status':True,'python':33,'mysql':25,'flask':34}
    }
name = input("Enter the name: ")

if name in data:
    if data[name]['status']:
        total = data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg = total/3
        if avg > 90:
            print(f"Congrations {name}, You got first class!!!")
        elif avg > 70:
            print(f"Good {name}, keep it up for the next time!!")
        elif avg > 35:
            print(f"Better {name}, work hard next time!")
        else:
            print(f"{name}, you have failed in the exam.Bring your parents.")
    else:
        print(f"{name} didn't write the exam.Bring your parents")
else:
    print(f"{name}'s data is not found")
    
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> data = {
...     'ramakanth':{'status':True,'python':98,'mysql':95,'flask':94},
...     'prakash':{'status':True,'python':78,'mysql':65,'flask':84},
...     'naresh':{'status':False,'python':None,'mysql':None,'flask':None},
...     'vamsi':{'status':True,'python':68,'mysql':55,'flask':64},
...     'rishi':{'status':True,'python':33,'mysql':25,'flask':34}
...     }exam.Bring your parents.")
...     else:
...         print(f"{name} didn't write the exam.Bring your parents")
... else:
...     print(f"{name}'s data is not found")\
...                      
SyntaxError: unterminated string literal (detected at line 7)
>>> 
>>> '''
... #Checking Budget for planning
... 
... budget = int(input("Enter the budget: "))
... 
... if budget > 50000:
...     print("You can go for the trip")
... 
... elif budget > 30000:
...     print("You can go for pub")
... 
... elif budget > 10000:
...     print("You can go for the shopping")
... 
... elif budget > 5000:
...     print("You can go for cafe")
... 
... elif budget > 2000:
...     print("You can go for the movie")
... 
... elif budget > 500:
...     print("You can recharge your phone")
... 
... else:
...     print("Take Rest")
... 
