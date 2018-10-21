'''
Looks like you cannot treat the would-be comments below
as comments. I THINK this is because they are really UNIX
lines that just happen to begin with a #
But if you comment them out with a tripe quote, all is well.
#!/usr/bin/env python3 (This is the shebang line for UNIX)
# Copyright 2009-2017 BHG http://bw.org/
'''
print()
print('In Python, a class is a defenition, and an object is an instance of a class.')

class Duck:
    baxsound = 'BAX QUACK!'
    baxwalking = 'BAX WALKS LIKE BIG ASS DUCK IN GIANT ALL-CAPS DAMMIT!!!'

    def quack(self):

        print('Quaaack!')
        print(self.baxsound)

    def walk(self):
        print('Walks like a duck.')
        print(self.baxwalking)
        

def main():
    donald = Duck() #"donald" is now an object of the class "Duck"
    donald.quack()  #method "quack"
    donald.walk()   #method "walk"


if __name__ == '__main__': main()
print()