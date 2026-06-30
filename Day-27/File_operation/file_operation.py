
'''
file = open('sample.txt','r')

print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()

'''
'''

try:
    file = open('sample.txt','r')
except FileNotFounder:
    print("File is not there")

else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()
'''

'''
with open('sample.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()
'''


'''
with open('sample.txt','a') as file:
    file.write('praneeth\nshiva\nsrikanth')
'''

with open('sample.txt','w') as file:
    file.write('praneeth\nshiva\nsrikanth')




























