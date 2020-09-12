def IsArmstrong(number):
    #123  ---->
    #1*1*1 + 2*2*2 + 3*3*3
    cloneNumber=number
    sum=0
    power=findPower(cloneNumber)
    while cloneNumber>0:
        nextSingleDigit=int(cloneNumber%10)
        tempAlloc=pow(nextSingleDigit,power)
        sum=sum+tempAlloc
        cloneNumber=int(cloneNumber/10)
    return sum == number

def findPower(number):
    power=0
    while number>0:
        power=power+1
        number=int(number/10)
    return power

#Calling and execution   
maxLimit = int(input("Find all armstrong numbers from 1 to ? "))
for num in range(1, maxLimit): 
    if IsArmstrong(num): 
        print(num)
