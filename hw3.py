import math
import csv
import os
def prob1(word):
    cons = 0
    vowel = 0
    word = word.lower()
    for char in word:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            vowel += 1
        else:
            cons += 1
    
    if vowel > cons:
        return True
    elif vowel < cons:
        return False
    else:
        return None

def prob2(height, radius):
    return math.pi*height*radius*radius

def prob3(arrayStrings):
    fullStr = ""
    for str in arrayStrings:
        fullStr += ", "
        fullStr += str
    fullStr = fullStr[2:-1]
    return fullStr
        
def prob4(ListOfLists):
    for list in ListOfLists:
        list = prob3(list)
    with open('hw3.csv', 'w') as f:
        write = csv.writer(f)
        write.writerows(ListOfLists)
        
def prob5():
    with open('hw3.csv', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
        return rows

def prob6(x, y):
    try:
        return x/y
    except:
        print("can't divide")
    
def prob7(nums):
    shortList = []
    for num in nums:
        if num in shortList:
            continue
        else:
            shortList.append(num)
    return shortList

def prob8(name):
    os.mkdir(name)

print(prob1("WoOord"))
print(prob2(3, 4))
print(prob3(["test","word","jojfd"]))
print(prob4([["00", "01", "02"],["we", "tok", "knh"],["test", "test2", "test3"]]))
print(prob5())
print(prob6(4,0))
print(prob7([6,7,3,2,4,4,1,2,7,6,4,5,9,0,3,4,66]))
print(prob8("hw3-folder"))