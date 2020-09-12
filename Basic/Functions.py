def Sum(arg1, arg2=None):
    if arg2==None:
        print("The input type is "+ str(type(arg1)))
        sum=0
        for item in arg1:
            sum=sum+item
        return sum
    else:
        if type(arg1)!=type(arg2):
            print("Type miss match")
            return
        else:
            return arg1+arg2


#* means we can pass multiple arguments
#single * is tuple variable
#double * is dictionary variable
def FuncWithArg(*arg1, **arg2):
    print(arg1, type(arg1))
    print(arg2, type(arg2))


# print(Sum([12,43,54,67,8]))
# print(Sum({14,3,46,87,18}))
# print(Sum((1,4,11,45,68)))

# print(Sum(2,3))
# print(Sum(2,'3'))
FuncWithArg(12,11,12,32,Sagar=23, Naikele=24)



