# *
# * *
# * * *
# * * * *


for row in range(0,4):
    for column in (0,row+1):  # range is not there hence weired output
        print(column,end=' ')
    print("")

#end is very important, by default it is  \n which is new line, 
# it needs to remove for pattern programs and can be replace woth 
#empty string or space as per output look
# rows = 5
# for row in range(1, rows+1):

#     for column in range(1, row + 1):
#         print(column, end=' ')
#     print("")



for row in range(0,4):
    for column in range (0,row+1):
        print('*',end=' ')
    print("")