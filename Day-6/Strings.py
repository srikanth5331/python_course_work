Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = "python programming"
len(s)
18
sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
min(s)
' '
max(s)
'y'
ord('a')
97
ord('A')
65
ord('0')
48
ord(' ')
32
che(98)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    che(98)
NameError: name 'che' is not defined. Did you mean: 'chr'?
chr(98)
'b'
che(120)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    che(120)
NameError: name 'che' is not defined. Did you mean: 'chr'?
chr(120)
'x'
chr('65')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    chr('65')
TypeError: 'str' object cannot be interpreted as an integer
s = "python programming"
s.upper()
'PYTHON PROGRAMMING'
s.lower()
'python programming'
s.Capitalize()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s.Capitalize()
AttributeError: 'str' object has no attribute 'Capitalize'. Did you mean: 'capitalize'?
s.capitalized()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.capitalized()
AttributeError: 'str' object has no attribute 'capitalized'. Did you mean: 'capitalize'?
s.capitalize()
'Python programming'
s.title()
'Python Programming'
s.swapcase()
'PYTHON PROGRAMMING'

s.center(38,'*')
'**********python programming**********'
s.ljust(28,'-')
'python programming----------'
s.rjust(28,'-')
'----------python programming'
'123'.zfill(10)
'0000000123'
'123'.zfill(2)
'123'
s = "python programming"
s.find('o')
SyntaxError: multiple statements found while compiling a single statement
s = "python programming"
s.find('o')
4
s.rfind('o')
9
s.find('z')
-1
>>> s.index('o')
4
>>> s.rindex('o')
9
>>> s.index('z')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> s.rindex('o')
9
>>> s.replace('python','java')
'java programming'
>>> s.maketrans('s.maketrans('python','123456'))
...             
SyntaxError: unterminated string literal (detected at line 1)
>>> s.maketrans('s.maketrans('python','123456'))
...             
SyntaxError: unterminated string literal (detected at line 1)
>>> s.maketrans(('python','123456'))
...             
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s.maketrans(('python','123456'))
TypeError: if you give only one argument to maketrans it must be a dict
>>> s.translate(s.maketrans('python','12345565'))
...             
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s.translate(s.maketrans('python','12345565'))
ValueError: the first two maketrans arguments must have equal length
>>> s='java,python,javascript,c,c++'
...             
>>> s.split(',')
...             
['java', 'python', 'javascript', 'c', 'c++']
>>> s.split(',',2)
...             
['java', 'python', 'javascript,c,c++']
>>> g = 'sdfgh'
...             
