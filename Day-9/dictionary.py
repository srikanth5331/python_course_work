Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d ={}
d=dict()
type(d)
<class 'dict'>
d[1]='int'
d
{1: 'int'}
d ={'k1':'v1','k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d={}
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d['demo']='str'
d
{1: 'int', 12.3: 'float', 'demo': 'str'}
d[2+3j]='complex'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex'}
d[False]='bool'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex', False: 'bool'}
d={}
d[1]=1
d
{1: 1}
d[23]=23.4
d[3]='dffghhk'
d[4]=3+4j
d[5]=[1,2,3]
d[6]=(1,2,3)
d[7]={1:3}
d[8]={1:1,2:2}
d[9]=False
d
{1: 1, 23: 23.4, 3: 'dffghhk', 4: (3+4j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1: 3}, 8: {1: 1, 2: 2}, 9: False}
d={}
d[1]=2
d[2]=2
d[3]=2
d[4]=2
d
{1: 2, 2: 2, 3: 2, 4: 2}
d
{1: 2, 2: 2, 3: 2, 4: 2}
d[3]
2
d={1:2,2:2,3:2,4:2}
d[4]
2
d[6]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    d[6]
KeyError: 6
d[1]
2
d[4]
2
d={'komalatha':89,'bhargavi':76,'subbu':90,'nagendra':76,'dinesh':50}
d['bhargavi']
76
d['subbu']
90
d['komalatha']
89
d.get('sahith')
d.get('akhil','user not found')
'user not found'
d.get('subbu','user not found')
90
d
{'komalatha': 89, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 50}
'dinesg' in d
False
'subbu' in d
True
'sahith' not in d
True
d.keys()
dict_keys(['komalatha', 'bhargavi', 'subbu', 'nagendra', 'dinesh'])
d.values()
dict_values([89, 76, 90, 76, 50])
d.iems()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    d.iems()
AttributeError: 'dict' object has no attribute 'iems'. Did you mean: 'items'?
d.items()
dict_items([('komalatha', 89), ('bhargavi', 76), ('subbu', 90), ('nagendra', 76), ('dinesh', 50)])
sorted(d)
['bhargavi', 'dinesh', 'komalatha', 'nagendra', 'subbu']
max(d)
'subbu'
min(d)
'bhargavi'
len(d)
5
d['dinesh']
50
d
{'komalatha': 89, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 50}
d['dinesh']=100

d
{'komalatha': 89, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100}
d['komalatha']=60
d
{'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100}
>>> d['rishi']=87
>>> d
{'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100, 'rishi': 87}
>>> d.update({'praneeth':90,'mandeep':80})
>>> d
{'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100, 'rishi': 87, 'praneeth': 90, 'mandeep': 80}
>>> d.popitem()
('mandeep', 80)
>>> d
{'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100, 'rishi': 87, 'praneeth': 90}
>>> d.popitem()
('praneeth', 90)
>>> d
{'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100, 'rishi': 87}
>>> d.pop('subbu')
90
>>> d
{'komalatha': 60, 'bhargavi': 76, 'nagendra': 76, 'dinesh': 100, 'rishi': 87}
>>> del d['komalatha']
>>> d
{'bhargavi': 76, 'nagendra': 76, 'dinesh': 100, 'rishi': 87}
>>> d.clear()
>>> d
{}
>>> d={'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100, 'rishi': 87, 'praneeth': 90, 'mandeep': 80}
>>> d
{'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100, 'rishi': 87, 'praneeth': 90, 'mandeep': 80}
>>> d.setdefault('rishi',0)
87
>>> d
{'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100, 'rishi': 87, 'praneeth': 90, 'mandeep': 80}
>>> d.setdefault
<built-in method setdefault of dict object at 0x000001ED3DDC3FC0>
>>> d.setdefault('satish',0)
0
>>> d
{'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100, 'rishi': 87, 'praneeth': 90, 'mandeep': 80, 'satish': 0}
>>> d.setdefault('satish',0)
0
>>> d
{'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100, 'rishi': 87, 'praneeth': 90, 'mandeep': 80, 'satish': 0}
