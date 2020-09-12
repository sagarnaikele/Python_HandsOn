# ****
#  ***
#   **
#    *

# ****
# ***
# **
# *


inp=5
for row in range(1,inp):
    for space in range(1, row):
        print("", end=' ')
    for star in range(row, inp):
        print("*",end='')
    print()

for row in range(1,inp):
    for star in range(row, inp):
        print("*",end='')

    print()

