# Logical Operators
#and - or - not

x = 5
y = 10

## and 
print( x > y ) # => true
print( x > y and y < x ) # => true 
print( x < y and y < x ) # => false 
# in and the two conditions should be true 
# if one of the conditions response (false) the result is false .

## or
print( x > y or y < x ) # => true 
print( x > y or y > x ) # => true 
# in or one of the two conditions be true to get true response .
# if the two conditions response (false) the result is false .

## not
print( not True ) # => false 
print( not False ) # => true 
# in not you reverse the result, if you want to reverse true ? you should write (not) before it .