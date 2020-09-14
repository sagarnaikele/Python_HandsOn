# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1

noOfRows=5
for row in range(0,noOfRows):
    for col in range(row+1,0,-1):
        print(col, end=' ')
    print()