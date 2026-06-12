'''
s='python'
#py pt ph po pn yt yh yo yn th to tn ho hn on
for i in range(len(s)):
    for j in range(i+1,len(s)):
        print(s[i],s[j],sep='',end=' ')

       '''
'''
l = [[1,2,3],[4,5,6],[7,8,9]]
#sum=45
sum = 0
for i in l:
    for j in i:
        sum+=j
print(f'sum = {sum}')
'''
'''
for row in range(5):
    for col in range(5):
        print(col,end=' ')
    print()    
0 - 01
1 - 01
2 - 01
3 - 01
4 - 01
'''

'''
n = int(input("enter the size:"))
for row in range(n):
    for col in range(n):
        print("*",end=' ')
    print() 
'''
'''
n = int(input("entera size"))
for row in range(n):
    for col in range(n):
        print(col % 2,end='')
    print()

'''

'''
n = int(input("enter a number"))
for row in range(n):
    for col in range(row+1):
        print('*',end=' ')
    print()    
'''
'''
n = int(input("enter a number"))
for i in range(n):
    for j in range(n-i):
        print('*',end='')
    print()    
'''


'''
n = int(input("enter a number"))
for i in range(n):
    for sp in range(n-i-1):
        print(' ',end=' ')
    for i in range(i+1):
        print('*',end=' ')
    print()    
    
'''
'''
n = int(input('enter a number'))
for row in range(n):
    for col in range(n):
        print((row+col)%2,end='')
    print()    

'''

n = int(input('enter a number'))
c=1
for row in range(n):
    for col in range(row+1):
        print(c,end='')
        c+=1
    print()    
















    
