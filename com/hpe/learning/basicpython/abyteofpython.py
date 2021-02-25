'''
this code is developed with a byte of python
'''


print ("Chapter 6: Basics\n")
# ================================================\n
print ("Hello World")
print ("Printing a line with special characters - I'm learning Python *****\n")
print ('''
well this is printing multiple lines ---->
Line 1: I think this is ok \nLine 2: seriously
Line 3: try printing multiple lines\n\n\n
''')


print ("Format - method")

print ('''String are Immutable - it means once defined the string and it can't be changed in future
this is why format method play vital role -\n
see below for the example
''')

age = 40
name = 'Thigotpi'
print ("{} which is {} years old, is still learning Python".format(name, age))


print ("this is first line. \
this is second line." r"this is third line")

print ("Logical line and Physical line")
print ('''
Physical line: line/statement written by the program what we see
Logical line: lines what the python sees and executes
''')

i = "Samson"
print ("the name of the boy is :", i)
print ("\n\n\n\n")


print ("Chapter 6: Basics\n")

a = 'la'
b = 3
mul = a*b
print ("multiplication =", mul)

c = 3
pow = b**c
print ("power = ", pow)
print ("\n\n")
print ("Find the area and perimeter\n")
length = 10
breadth = 5
area = length * breadth
perimeter = 2 * (length + breadth)
print ("area =", area)
print ("perimeter =", perimeter)
print ("\n\n\n\n")

print ("Chapter 7: Control Flow\n")

print("Taking input and manipulate and printing\n")
a = 23


#from pip._vendor.distlib.compat import raw_input

#guess = int(raw_input("Enter any number = "))
guess = int(input("Enter any number = "))
print("Now we are checking if the given number is even or odd")
if a/2 == 0:
    print("then the given number is Even")
else:
    print("the given number is odd")
    
    print ("Now time to check if the number of bigger number or smaller number")
    