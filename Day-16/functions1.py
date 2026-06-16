'''
n = 10

def display():
    n = 10
    print("Inside:",n)
display()
print("Outside:",n)
'''
'''
n = 10

def display():
    global n
    n = 10
    print("Inside:",n)
display()
print("Outside:",n)
'''
'''
n = 10

def display():
    global n
    n += 10
    print("Inside:",n)

n = 10
display()
print("Outside:",n)
'''
'''
def outer():
    n =10
    def inner():
        nonlocal n
        n+=10
        print("Inner Function:",n)
    inner()
    print("Outer function:",n)
outer()    
'''

'''
s = 'python'
print(len(s))

'''

'''
#int float complex str list tuple set dict bool
#int float complex str tuple bool
#list set dic

def update(n):
    print("Inside:",n)
n = True
update(n)
print("Outside:",n)

'''
'''
def func():
    if basecondi:
        return
    func()
'''    
'''
def func(num):
    if num == 0:
        return
    print(num,end=' ')
    func(num-1)
    print(num,end=' ')
func(5)    

'''
'''
def sumofdigits(n):
    if n ==0:
        return 0
    return n+sumofdigits(n-1)
print(sumofdigits(5))
'''
'''
def power(base,pow):
    if pow ==0:
        return 1
    return base * poqer(base,pow-1)
print(power(2,4))
print(power(3,3))

'''
def reverseofstr(s,ind):
    if ind == 0:
        return s[0]
    return s[ind]+reverseofstr(s,ind-1)
l ="pyhton programming"
print(reverseofstr(l,len(l)-1))


























































































