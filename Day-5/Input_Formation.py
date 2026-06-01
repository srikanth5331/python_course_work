Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = input()
srikanth
name
'srikanth'
name = intput("enter your name: ")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    name = intput("enter your name: ")
NameError: name 'intput' is not defined. Did you mean: 'input'?
name = input("enter your name: ")
enter your name: vamsi
name
'vamsi'
age = input("enter your age: ")
enter your age: 22
age
'22'
type(age)
<class 'str'>
gpa = float(input("enter the cpa: "))
enter the cpa: 7.9
gpa
7.9
type(gpa)
<class 'float'>
'subbu nagendra sahith vamsi rishi harish'.split(' ')
['subbu', 'nagendra', 'sahith', 'vamsi', 'rishi', 'harish']
names = input("enter the names : ").split()
enter the names : subbu nagendra sahith vamsi rishi harish
names
['subbu', 'nagendra', 'sahith', 'vamsi', 'rishi', 'harish']
products = input("enter the products")
enter the productslaptop mouse charger keyboard
products
'laptop mouse charger keyboard'
topics = tuple(input("enter the topics : ").split())
enter the topics : token statement
>>> enter the topics : token statement
SyntaxError: invalid syntax
>>> topics
('token', 'statement')
>>> op = set(input("enter the oper: ").split())
enter the oper: in not in is is not not and or not
>>> op
{'is', 'in', 'not', 'and', 'or'}
>>> marks = input("enter the marks: ").split()
enter the marks: 34 76 89 21 22
>>> marks
['34', '76', '89', '21', '22']
>>> int(['34', '76', '89', '21', '22'])
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int(['34', '76', '89', '21', '22'])
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> map(int,input("enter the marks: ").split())
enter the marks: 1 23 4 5
<map object at 0x000001FF2532E920>
>>> list(map(int,input("enter the marks: ").split()))
enter the marks: 4 5 6 7 8
[4, 5, 6, 7, 8]
>>> prices = tuple(map(int,input("enter the marks: ").split()))
enter the marks: 45 67 89 09
>>> prices
(45, 67, 89, 9)
>>> rating = set(map(int,input("enter the marks: ").split()))
enter the marks: 2 4 6 7 9
>>> rating
{2, 4, 6, 7, 9}
>>> per = list(map(float,input("enter the marks: ").split()))
enter the marks: 56.3,23.4
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    per = list(map(float,input("enter the marks: ").split()))
ValueError: could not convert string to float: '56.3,23.4'
>>> prices = tuple(map(float,input("enter the prices: ").split()))
enter the prices: 5667 7890 1257 68979
>>> prices
(5667.0, 7890.0, 1257.0, 68979.0)
