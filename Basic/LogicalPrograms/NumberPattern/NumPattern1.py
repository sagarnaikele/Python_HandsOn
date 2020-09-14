# 1
# 23
# 456
# 78910

startNum=5
NumStorage=0

for row in range(1, startNum):  #1,2
    for col in range(NumStorage+1, NumStorage+row+1): #1->2,2->4 (for condition is 1st Num < 2nd Number)
        print(col, end='') #1
        NumStorage=col  #1
    print()

#other and better way
#(NumStorage+1, NumStorage+row+1) this condition is simplified as (NumStorage=col+1)
startNum=5
NumStorage=1
for row in range(1, startNum):  #1,2
    for col in range(NumStorage, NumStorage+row): #1->2,2->4 (for condition is 1st Num < 2nd Number)
        print(col, end='') 
        NumStorage=col+1  
    print()