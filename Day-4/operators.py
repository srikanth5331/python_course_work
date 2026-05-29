Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 20
b = 10
a+b
30
a - b
10
a*b
200
a/b
2.0
9/2
4.5
a**2
400
6**3
216
a%b
0
17%4
1
17%3
2
a>b
True
a<=b
False
a==b
False
a!=b
True
y=5
y
5
y=y+5
y
10
y=y+10
y
20
y +=10
y
30
y-2=
SyntaxError: cannot assign to expression
y-=20
y
10
y*=4
y
40
y*2
80
y//=10
y
4
y=y+10
y
14
y+=20
y
34
y/=2
y
17.0
20
20
\
a%10==0
True
a%20==0 or b %20==0 or a>b
True
a%20==0 or b %20==0 or a<b
True
a%22==0 or b %20==0 or a>b
True
not a>b
False
#str,list,tuple,set,dict
a = "python programming"
a
'python programming'
"y" in a
True
"g" in a
True
"z" not in a
True
"r" not in a
False
l = ["java,"python","mysql","c++/","c","html"]
     
SyntaxError: unterminated string literal (detected at line 1)
l = ["java','python','mysql','c++/','c','html']
     
SyntaxError: unterminated string literal (detected at line 1)
l = ['java','python','mysql','c++/','c','html']
     
'mysql' in l
     
True
t = ('laptop','mobile','mouse','keyboard')
     
'laptop' in t
     
True
'charger' in t
     
False
t = {1,2,3,4,5,6,7,78}
     
t
     
{1, 2, 3, 4, 5, 6, 7, 78}
4 in t
     
True
50 not in t
     
True
d = {'egg':8,'oil':120,'sugar':40,'salt':30}
     
oil in d
     
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    oil in d
NameError: name 'oil' is not defined
'oil' in d
     
True
120 in d
     
False
'sugar' in d
     
True
'chilli' in d
     
False
l =[1,2,3,4,5]
     
m =[1,2,3,4,5]
     
l==m
     
True
n=m
     
n
     
[1, 2, 3, 4, 5]
n==m
     
True
l is m
     
False
n is m
     
True
id(l)
     
2359426671040
id(m)
     
2359426399616
id(n)
     
2359426399616
>>> l is not in m
...      
SyntaxError: invalid syntax
>>> l is not m
...      
True
>>> n is not l
...      
True
>>> 8 & 14
...      
8
>>> 8 & 7
...      
0
>>> 8 | 7
...      
15
>>> 10 ^ 11
...      
1
>>> 
>>> ~12
...      
-13
>>> 15>>1
...      
7
>>> 15>>3
...      
1
>>> 15>>2
...      
3
>>> 15>>1
...      
7
>>> 4<<2
...      
16
