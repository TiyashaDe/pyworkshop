def my_func():
    print("hi")
my_func()
greeting=my_func()
type(greeting)
def my_func():
    return "Hi"
my_func()
greeting=my_func()
greeting
def add_numbers(x,y):
    return x+y
add_numbers(3,4)
result=add_numbers(10,20)
result
def add_numbers(x,y,z=1):
    return x+y+z
add_numbers(65,5)
add_numbers(5,7,8)
def add_numbers(x=4,y=6,z=9):
    return x+y-z
add_numbers(x=4,y=6,z=9)
def add_numbers(x,y,z=1):
    return x+y+z
add_numbers(1,2,3)
def add_numbers(a,b,c):
    return a*b+c
add_numbers(4,6,7)
def create_query(language="JavaScript",num_stars=10,sort="desc"):
    return f"language:{language},num_stars is {num_stars},sort is{sort}"
 create_query()
 create_query(language="Python")
 create_query(num_stars=20)
 #don't use mutable types as default arguments!!
 def do_stuff(my_list=[]):
    my_list.append("stuff!")
do_stuff()
def do_stuff(my_list=[]):
    my_list.append("stuff!")
    return my_list
do_stuff()
do_stuff()
do_stuff()
def do_stuff(my_list=None):
    if my_list==None:
       my_list=[]
       my_list.append("stuff")
    return my_list
do_stuff()
do_stuff()
def print_name(name):
    print(name)
print_name("Riya")
name="Riya"
print("Name outside of the function:(name)")
def try_change_name():
    name="Tina"
    print(f"Name INSIDE of the function:{name}")
    
try_change_name()
name