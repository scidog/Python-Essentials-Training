'''
Looks like you cannot treat the would-be comments below
as comments. I THINK this is because they are really UNIX
lines that just happen to begin with a #
But if you comment them out with a tripe quote, all is well.
#!/usr/bin/env python3 (This is the shebang line for UNIX)
# Copyright 2009-2017 BHG http://bw.org/
'''

print()
import platform

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))
    print('Bax line 1')
print('Bax line 2. LIne prints before "Bax line 1" if not indented properly.')

if __name__ == '__main__': main()
print()