from importlib.util import spec_from_file_location


spending = [("John", 30), ("Greg", 40), ("John", 50)]
total = 0
totalList = []
for var in spending:
    if var[0] in totalList:
        continue
    totalList.append((var[0], var[1]))
print(totalList)