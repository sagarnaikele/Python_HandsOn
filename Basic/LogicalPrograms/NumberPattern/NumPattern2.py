# 10987
#  654
#   32
#    1
startNum=4
NumStorage=10

for row in range(startNum,0,-1):
    for space in range(startNum,row,-1):
         print('',end=' ')
    for col in range(NumStorage, NumStorage-row,-1):
        print(col,end='')
        NumStorage=col-1
    print()