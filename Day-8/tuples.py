Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t = (1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=()
t=(1,1,1,1,1)
t
(1, 1, 1, 1, 1)
t =(1,1.1,'tryu',[])
t
(1, 1.1, 'tryu', [])
t=(10, 20, 30, 40, 50, 90, 80, 70)
t*4
(10, 20, 30, 40, 50, 90, 80, 70, 10, 20, 30, 40, 50, 90, 80, 70, 10, 20, 30, 40, 50, 90, 80, 70, 10, 20, 30, 40, 50, 90, 80, 70)
t
(10, 20, 30, 40, 50, 90, 80, 70)
t =(10, 20, 30, 40, 50)
t[1]
20
t[4]
50
t[2]
30
t[1]
20
t
(10, 20, 30, 40, 50)
t[:3]
(10, 20, 30)
t
(10, 20, 30, 40, 50)
t[3:]
(40, 50)
t[1:4]
(20, 30, 40)
t[2:]
(30, 40, 50)
t[::2]
(10, 30, 50)
t[-1:-4:-1]
(50, 40, 30)
t
(10, 20, 30, 40, 50)
10 in t
True
30 in t
True
60 not in t
True
10 not in t
False
len(t)
5
sorted(t)
[10, 20, 30, 40, 50]
min(t)
10
max(t)
50
sum(t)
150
t.count(t)
0
t.count(10)
1
t.index(10)
0
t =1, 2, 3, 4, 5
a=(1,2,4)
a
(1, 2, 4)
x,y,z=a
x
1
y
2
z
4
t=(1,2,3,[4,5,6],7,8)
t
(1, 2, 3, [4, 5, 6], 7, 8)
t[2]
3
t[4]
7
t[3]
[4, 5, 6]
t[3]
[4, 5, 6]
t[3].append(10)
t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
s=set()
s={1,1,1,1,1}
s
{1}

s ={987,654,345,56,345,1,2,34,6,56}
s
{1, 2, 34, 6, 654, 56, 345, 987}
s=set()
s
set()
s.add(1)
s
{1}
s.add(56.567)
s
{56.567, 1}
s.add("kjhy")
s
{56.567, 1, 'kjhy'}
s.add([1,2,3,,3])
SyntaxError: invalid syntax
s.add([1,2,3,3])
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    s.add([1,2,3,3])
TypeError: unhashable type: 'list'
s.add((1,2,3,4))
s
{56.567, 1, 'kjhy', (1, 2, 3, 4)}
s
{56.567, 1, 'kjhy', (1, 2, 3, 4)}
s.add(false)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    s.add(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
s.add("false")
s
{1, 'kjhy', (1, 2, 3, 4), 56.567, 'false'}
i in s
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    i in s
NameError: name 'i' is not defined
1 in s
True
2 in s
False
false not in s
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    false not in s
NameError: name 'false' is not defined. Did you mean: 'False'?
a={1,2,3,4,5,6,8,10}
b={6,7,8,9}
a | b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a.intersection(b)
{8, 6}
>>> a & b
{8, 6}
>>> #{1}{2}{3}{5}{1,3}{1,2}{8,10}
>>> a <= {1}
False
>>> a >={1}
True
>>> a <= {1,2,3,4,5,6,8,10,11,12}
True
>>> a >= {6,10,8}
True
>>> a
{1, 2, 3, 4, 5, 6, 8, 10}
>>> b
{8, 9, 6, 7}
>>> a.isdisjoint(b)
False
>>> a.isdisjoint({90,80})
True
>>> a.add(17)
>>> a
{1, 2, 3, 4, 5, 6, 8, 10, 17}
>>> a.add(14)
>>> a
{1, 2, 3, 4, 5, 6, 8, 10, 14, 17}
>>> a.update({11,12,13})
>>> a
{1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 13, 14, 17}
>>> a.pop()
1
>>> a.pop()
2
>>> a.remove(6)
>>> a
{3, 4, 5, 8, 10, 11, 12, 13, 14, 17}
>>> a.discard(3)
>>> a
{4, 5, 8, 10, 11, 12, 13, 14, 17}
>>> a.clear()
>>> a
set()
