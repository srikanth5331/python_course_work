Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s ='    hello    world'
s
'    hello    world'
s.strip()
'hello    world'
s.lstrio()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s.lstrio()
AttributeError: 'str' object has no attribute 'lstrio'. Did you mean: 'lstrip'?
>>> s.lstrip()
'hello    world'
>>> s.rstrip()
'    hello    world'
>>> s ='strings.py'
>>> s
'strings.py'
>>> s.startswith('str')
True
>>> s.startswith('ghj')
False
>>> s.endswith('py')
True
>>> s.endswith('js')
False
>>> 'ssdfghj'.isalpha()
True
>>> 'sdfghjjkfghh'.isalpha()
True
>>> 'sowmya@1234'.isalpha()
False
>>> '23456789'.isalpha()
False
>>> 'ewrtyuii'.islower()
True
>>> 'ASDFGHH@#$%'.islower()
False
>>> ' '.ispace()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    ' '.ispace()
AttributeError: 'str' object has no attribute 'ispace'. Did you mean: 'isspace'?
>>> ' '.isspace()
True
>>> 'Py Prg Lan'.istitle()
True
>>> 'py_python'.isidentifier()
True
>>> 'py@1123'.isidentifier()
False
