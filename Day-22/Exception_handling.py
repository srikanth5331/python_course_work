'''
try:
    a = int(input("Enter a number:"))
except ValueError:
    print("Enter the age in a digit[0-9] format")
else:
    print("Age:",a)
finally:
    print("ThankYou")
'''

'''
try:
    a = int(input("Enter a number:"))
    print(12/0)
    print(b)
    print(13+'14')
    print(d[5])
    l=[1,2,3]
    print(l[10])

    
except ValueError:
    print("Enter the age in a digit[0-9] format")
except ZeroDivisionError:
    print("can't divide with zero")
except NameError:
    print("define the var")
except TypeError:
    print("Add the same datatypes")
except KeyError:
    print("Key is not present")
except IndexError:
    print("Index is out of range")
else:
    print("Age:",a)
finally:
    print("ThankYou")
'''

'''
try:
    a = int(input("Enter a number:"))
    print(12/0)
    print(b)
    print(13+'14')
    print(d[5])
    l=[1,2,3]
    print(l[10])

    
except (ValueError,ZeroDivisionError,NameError,TypeError,KeyError,IndexError) as e:
    print("Error occured",e)
else:
    print("No Error occured")
finally:
    print("ThankYou")
'''

'''
try:
    a = int(input("Enter a number:"))
    print(12/0)
    print(b)
    print(13+'14')
    print(d[5])
    l=[1,2,3]
    print(l[10])

    
except Exception as e:
    print("Error occured",e)
else:
    print("No Error occured")
finally:
    print("ThankYou")
'''

try:
    amount = int(input("Enter a amount to withdraw:"))
    if amount<0:
        raise Exception("Enter the amount greater than zero")

    
except Exception as e:
    print("Error occured",e)
else:
    print("No Error occured")
finally:
    print("ThankYou")


























    
