#baxtypes.1.py
#from type() and id()s section of Python Essential Training 
print()
baxtuple01 = (1,'two',3,[4, 'four'],5) #() = tuple. Tuples are immutable
baxtuple02 = [1,'two',3,[4, 'four'],5] #[] = list. Lists are mutable
#baxtuple[2]=777 #gives error as you cannot change a tuple
print('baxtuple01 is {}'.format(baxtuple01))
print('All of baxtuple01 has type:', type(baxtuple01))
print('But elenent 3 of baxtuple01 has type :', type(baxtuple01[3]))
print()
print('Even if the entire tuple is identical, the id# is different..hmmm')
print('id of baxtuple01 is:', id(baxtuple01))
print('id of baxtuple02 is:', id(baxtuple02))
print()
print('But if any elements in tuples are identical, they return the same id')
print('id of baxtuple01[0] is:', id(baxtuple01[0]))
print('id of baxtuple02[0] is:', id(baxtuple02[0]))
print()
print('Are baxtuple01[0] and baxtuple02[0] the same?')
if baxtuple01[0] is baxtuple02[0]:
        print('yes, baxtuple01[0] is baxtuple02[0]')
else:
        print('no, baxtuple01[0] is not baxtuple02[0]')

print()

print()
print('Is baxtuple01[0] a tuple?')
if isinstance (baxtuple01, tuple):
        print('baxtuple01 is a tuple')
if isinstance (baxtuple01, list):
        print('baxtuple01 is actually a list')
if isinstance (baxtuple02, tuple):
        print('baxtuple02 is a tuple')
if isinstance (baxtuple02, list):
        print('baxtuple02 is actually a list')        
else:
        print('Huh...nothing rcognizable as tuples or lists.')

print()
for i in baxtuple01:
        print('baxtuple01 is {}'.format(i))
        print(type(baxtuple01))
print()

