'''
Looks like you cannot treat the would-be comments below
as comments. I THINK this is because they are really UNIX
lines that just happen to begin with a #
But if you comment them out with a tripe quote, all is well.
#!/usr/bin/env python3 (This is the shebang line for UNIX)
# Copyright 2009-2017 BHG http://bw.org/
'''
print()

#below we put this def here just to show that you can call it whenever
def bax_prime_list():
    print('Here are the primes from 1 to 100')
    for p in range(100):
        if isprime(p):
            print(p, end=' ', flush=True)
print()

def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True
n= int(input("Input number please: "))
#n = 6
if isprime(n):
    #print(f'{n}is prime')
    print(n, 'is prime')

else:
    #print(f'{n} not prime')
    print(n, 'is not prime')
print()

#...and here we call the def
bax_prime_list()
print()
print()