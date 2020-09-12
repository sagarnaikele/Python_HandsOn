#for loop
#in checks is item present in collection and returen true/false
theList=[1,2,3,4,5]
theTuple={6,7,8,9,10}
theSet=(11,12,13,14,15)
theDictionary={
    "name": "Sagar",
    "job": "Software Engineer"
}

print("---------------List---------------")
for item in theList:
    print(item)
    if item==2:
        break

print("---------------Tuple---------------")
for item in theTuple:
    print(item)

print("---------------Set---------------")
for item in theSet:
    print(item)
else:
    print("Finished")

print("Dictionary")
for key, value in theDictionary.items():
    print("Key is " +key +" value is "+ value)