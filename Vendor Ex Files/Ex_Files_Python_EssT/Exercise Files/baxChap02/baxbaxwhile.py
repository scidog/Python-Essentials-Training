'''
Looks like you cannot treat the would-be comments below
as comments. I THINK this is because they are really UNIX
lines that just happen to begin with a #
But if you comment them out with a tripe quote, all is well.
#!/usr/bin/env python3 (This is the shebang line for UNIX)
# Copyright 2009-2017 BHG http://bw.org/
'''
print()

words = ['one', 'two', 'three', 'four', 'five']

print()

n = 0
while(n < 5):
    print(words[n])
    n += 1

print('----')

for i in words:
    print(i)
print()