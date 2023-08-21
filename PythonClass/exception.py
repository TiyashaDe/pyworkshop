try:
 int=("a")
except ValueError:
 print("An exception happened.") 
 
print("End of the program.") 
try:
 int=("a")
 d={}
 d["a"]
except ValueError:
 print("An exception happened.") 
 
print("End of the program.") 
#python Hierarchy
issubclass(ZeroDivisionError, ArithmeticError)
issubclass(ArithmeticError, Exception)
issubclass(Exception, BaseException)
issubclass(ZeroDivisionError,BaseException)