#baxtypes.py

print()
badsum = .1 +.1 +.1 -.3
print('badsum is {}'.format(badsum))  #format is a crazy powerful thing
print(type(badsum))
print("You never want to use floats when calculating money.")
print("This is because computers sacrifice accuracy in favor of precision,")
print("and while NOT ACCURATE the calculation is PRECISE to the cited decimals.")

#looks like I don't have Python 3.6 or greater in VSC yet,
# as "from decimal import *" blah blah does not work.

'''
print()
print("Now we calculate cash accurately.")
from decimal import *
profit = Decimal('0.10')
loss = Decimal('0.30')
goodsum = profit+profit+profit-loss
print('goodsum is {}'.format(goodsum))  #format is a crazy powerful thing
print(type(goodsum))
'''


print()
v = 7.0
print('v is {}'.format(v))  #format is a crazy powerful thing
print(type(v))


#looks like I don't have Python 3.6 or greater in VSC yet,
# as f strings do not work.
print()
a = 1
b = 2
c = 3
#w = f'abc {a} {b} {c}' #f strings available in python 3.6 and later only.
#print()
#print('w is {}'.format(w))  #format is a crazy powerful thing
#print(type(w))

print()
x = 7  #change the typr and see that Pythn tells you what type it is.
print('x is {}'.format(x))  #format is a crazy powerful thing
print(type(x))

print()
y = None
print('y is {}'.format(y))
print(type(y))


print()
z ='''
multi
line
string
'''
print('z is {}'.format(z))
print(type(z))
print()

print()
baxbool =True
print('baxbool is {}'.format(baxbool))
print(type(baxbool))
print()
 
baxlist = [1,2,3,4,5] #[] = list. Lists are mutable
baxlist[2]=777
for i in baxlist:
            print('baxlist is {}'.format(i))
print()


baxtuple = (1,2,3,4,5) #() = tuple. Tuples are immutable
#baxtuple[2]=777 #gives error as you cannot change a tuple
for i in baxtuple:
            print('baxtuple is {}'.format(i))
print()

kk = range(0,10,2) #range is a tuple...I think
for i in kk:
            print('baxrange is {}'.format(i))
print()

l = list(range(0,10,2)) #make range a list to change an element
l[3]=555
for i in l:
        print('baxrange is {}'.format(i))
print()


baxdict = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}
baxdict['key2']=123
for n in baxdict:
        print('baxdict is {}'.format(n))
print()

for key,value in baxdict.items():
        print('key: {}, value: {}'.format(key,value))
print()
