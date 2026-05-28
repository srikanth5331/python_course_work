Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 10
a
10
float(a)
10.0
a = 10
a
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
bool(a)
True
b = 10.5
int(b)
10
complex(b)
(10.5+0j)
str(b)
'10.5'
list(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
boo;(b)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    boo;(b)
NameError: name 'boo' is not defined. Did you mean: 'bool'?
bool(b)
True
bool(b)
True
c=2+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
str(c)
'(2+3j)'
bool(c)
True
s ="python"
list(s)
['p', 'y', 't', 'h', 'o', 'n']
tupke(s)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    tupke(s)
NameError: name 'tupke' is not defined. Did you mean: 'tuple'?
tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
set(s)
{'o', 'h', 'y', 'n', 'p', 't'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
l = [1,2,3,4,5]
int(l)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
>>> atr(l)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    atr(l)
NameError: name 'atr' is not defined. Did you mean: 'str'?
>>> str(l)
'[1, 2, 3, 4, 5]'
>>> tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
>>> set(l)
{1, 2, 3, 4, 5}
>>> tuple(l)
(1, 2, 3, 4, 5)
>>> bool(l)
True
>>> t =(1,2,3,4)
>>> int(t)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
>>> str(t)
'(1, 2, 3, 4)'
>>> list(t)
[1, 2, 3, 4]
>>> set(t)
{1, 2, 3, 4}
>>> dict(t)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(t)
True
>>> s= {1,2,3,4,5}
>>> str(s)
'{1, 2, 3, 4, 5}'
>>> list(s)
[1, 2, 3, 4, 5]
>>> tuple(s)
(1, 2, 3, 4, 5)
