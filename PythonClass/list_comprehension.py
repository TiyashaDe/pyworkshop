names=["nina","riya","rose","jimmy"]
my_list=[]
for name in names:
    my_list.append(len(name))
print("Before:",my_list)
my_list=[len(name)for name in names]
print("After:",my_list)
my_list=[name for name in names if len(name) %2 !=0]
print("After:",my_list)
my_list=[name for name in names if len(name) %2 ==0]
print("After:",my_list)
names_string="nina,riya,rose,jimmy"
names_string.split (",")
names_string
names_list=names_string.split(",")
names_list 
my_num=[1,2,4]
[num>2 for num in my_num] 
",".join([str(num*2) for num in my_num]) 
list_comp=(x**2 for x in range(10) if x%2==0)
gen_comp=(x**2 for x in range(10) if x%2==0)
type(gen_comp)
gen_comp
for item in gen_comp:
    print(item)