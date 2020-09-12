#lambda functions are mainly used to pass as 
# a argument to a function or return function form function
from functools import reduce

Add = lambda x,y: x+y
IsGreater=lambda x:x>5
Double =lambda x: x*2


my_list=[1,2,3,4,5,6,7,8,9]
my_list1=[1,2,5]
#Below line with double each element of my list and print
print(list(map(Double,my_list))) 

#reduce will add 1st two element and 
# then sum will be added to next element
print(reduce(Add,my_list)) 

#Filter will take bool function as 
# input and will compare list accordingly
print(list(filter(IsGreater,my_list)))


