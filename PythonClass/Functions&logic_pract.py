def add_numbers(x,y):
 return x+y
add_numbers(4,5)
def add_numbers(a,b,c):
 return(a*b+c)
add_numbers(5,6,8)
x=2
def my_func():
    x=3
    print(x,"in function")
x
def add_numbers(x,y,operation="add"):
    if operation=="add":
        return x+y
    else:
        return x-y
    
add_numbers(3,2)
add_numbers(3,2,operation="something else")
None
True
5<3
3>5
3<5==True
3<5
if True:
    print("hi")
else:
    print("bye")
if False:
    print("1")
elif True:
    print("2")
else:
    print("3")
    
def fizzbuzz(number):
    if number%3==0 and number%5==0:
        print("fizzbuzz")
    fizzbuzz(3)
    fizzbuzz(5)
def fizzbuzz(number):
    if (number % 3==0) and (number % 5==0):
        print("fizzbuzz")
    fizzbuzz(5)