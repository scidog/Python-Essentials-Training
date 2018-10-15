'''
Looks like you cannot treat the would-be comments below
as comments. I THINK this is because they are really UNIX
lines that just happen to begin with a #
But if you comment them out with a tripe quote, all is well.
#!/usr/bin/env python3 (This is the shebang line for UNIX)
# Copyright 2009-2017 BHG http://bw.org/
'''
print()

def function(n = 1): # "1" is a default value 
    print("Number was", n)
    return n    #allows use of "x = finction() statement below"
    
function(47) #number in the () here overrides the default val above

             #structure below yields a "None"...abscence of value
             #UNLESS one puts a return in the def
x = function(99)
print(x)

print()