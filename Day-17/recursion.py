'''
def display(s,ind):
    if ind == len(s):
        return
    print(s[:ind+1])
    display(s,ind+1)
display("Python",0)    
'''
'''
def display(s,ind,l):
    if ind == len(s)-1+1:
        return
    print(s[ind:ind+1])
    display(s,ind+1,l)

    
display("python programming",0,10)

'''
'''
def display(s,ind):
    if ind == len(l):
        return 0
    return l[i]+display(l,ind+1)

l = [1,2,4,5,6,7,3,5,6]   
print(display(1,0))
'''
def display(s,i):
    if i == len(s):
        return 0
    if s[i] in 'aeiouAEIOU':
        return 1+display(s,i+1)
    else:
        return display(s,i+1)

s = 'python programming'
print(display(s,0))

































