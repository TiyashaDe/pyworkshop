colors=["Red","Yellow","Blue","Orange"]
for colors in colors:
    print(f"The color is:(color)")
print("outside of the loop",colors)
range(5)
list(range(5))
list(range(5,7))
for num in range(3,7):
    print(num)
colors=["Red","Yellow","Blue","Orange"]
enumerate(colors)
list(enumerate(colors))
colors
for index,color in enumerate(colors):
    print(f"{index} colors at:{colors}")
hex_colors={"Red":"aFF000","Green":"a00677","Blue":"a0089"}
for foo in hex_colors:
    print(foo)  
    
hex_colors.items()
for key,value in hex_colors.items():
    print(key)
    print("---")
    print(value)
val=0
while val < 5:
    print(val)
    val+= 1
    
names=["Riya","Piya","Madhu"]
def return_target(target="stan"): 
 for name in name:
    if name=="target":
        return name
 return_target() 
 return_target(target="Riya") 
   
