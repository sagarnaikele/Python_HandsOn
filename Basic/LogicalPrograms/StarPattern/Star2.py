#         *
#       * *
#     * * *
#   * * * *

for row in range(0,4):  # main loop for number of row as well as supporting for column
    for col in range(4, row,-1): # column loop for space will loop in reverse from max row number to no row
        print(" ", end=' ')  #4321, 432, 43,4
    for star in range(0,row+1):  # column loop for star will loop 0 to max+1, 0,01,012,0123,01234,012345
        print('*', end=' ')
    print("")
