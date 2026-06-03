Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[]
l=list()
type(l)
<class 'list'>
l=[1,2,3,4]
m=[7,8,9,3]
l+m
[1, 2, 3, 4, 7, 8, 9, 3]
l*4
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
l=[10,20,30,40,50]
l[4]
50
l[2]
30
l[0]
10
l[1]
20
l[-1]
50
l[-3]
30
l[1:4]
[20, 30, 40]
l[::-1]
[50, 40, 30, 20, 10]
l[-3::-1]
[30, 20, 10]
l
[10, 20, 30, 40, 50]
2o in 1
SyntaxError: invalid decimal literal
20 in l
True
40 in 1
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    40 in 1
TypeError: argument of type 'int' is not iterable
80 in l
False
70 not in l
True
l =[10,20,30,40,50]
id(l)
1690250643904
l[4]=100
l
[10, 20, 30, 40, 100]
l.append(400)
l
[10, 20, 30, 40, 100, 400]
l.insert(4,50)
l
[10, 20, 30, 40, 50, 100, 400]
l.extend([80,90,110])
l
[10, 20, 30, 40, 50, 100, 400, 80, 90, 110]
l.pop()
110
l
[10, 20, 30, 40, 50, 100, 400, 80, 90]
l.pop()
90
l.pop()
80
l.pop(3)
40
l.pop(1)
20
l
[10, 30, 50, 100, 400]
l.remove(100)
l
[10, 30, 50, 400]
l.remove(400)
l
[10, 30, 50]
l.clear()
l
[]
l
[]
l =[10,30,33,40,42,50,70,100]
sorted(l)
[10, 30, 33, 40, 42, 50, 70, 100]
l.sort()
l
[10, 30, 33, 40, 42, 50, 70, 100]
min(l)
10
>>> max(1)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    max(1)
TypeError: 'int' object is not iterable
>>> max(l)
100
>>> l.reverse()
>>> l
[100, 70, 50, 42, 40, 33, 30, 10]
>>> sorted(l,reverse==True)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    sorted(l,reverse==True)
NameError: name 'reverse' is not defined. Did you mean: 'reversed'?
>>> sorted(l,reverse=True)
[100, 70, 50, 42, 40, 33, 30, 10]
>>> l.index(120)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    l.index(120)
ValueError: 120 is not in list
>>> l.index(1)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    l.index(1)
ValueError: 1 is not in list
>>> l
[100, 70, 50, 42, 40, 33, 30, 10]
>>> l.count(30)
1
>>> l
[100, 70, 50, 42, 40, 33, 30, 10]
>>> len(l)
8
>>> sum(l)
375
>>> any([1,2,3,4,5,0,0,0,0,0])
True
>>> all([1,2,3,4,5,0,0,0,0,0])
False
