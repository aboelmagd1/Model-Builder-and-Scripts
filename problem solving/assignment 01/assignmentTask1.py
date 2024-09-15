import os
def checkINT ():
    while True :
        inputeUserINT = input("pease Enter count of students \n")
        try:
            numberOfStudents = int(inputeUserINT)
            return numberOfStudents
            break
        except:
            print("_____please enter number_____")
        
def checkFlout (numOfS):
    while True :
        inputeUserFlout = input("pease Enter dgreeee of student NO: {numOfS} \n".format(numOfS= numOfS+1))
        try:
            dgreeOfStudents = float(inputeUserFlout)
            return dgreeOfStudents
            break
        except:
            print("_____please Enter number_____")
        
counts = int(checkINT())
allDgrees = []
for i in range(counts):
    allDgrees.append(checkFlout(i))
print(allDgrees)
sum = 0
for i in allDgrees:
    sum = i + sum
print("Average is : {average}".format(average = sum/len(allDgrees)))
allDgrees.sort()
print(f"Range is : {allDgrees[-1] - allDgrees[0]}")
with open("re.txt" ,"w") as txt:
    txt.write(f"Average is : {sum/len(allDgrees)}\nRange is : {allDgrees[-1] - allDgrees[0]}")
    txt.read
    txt.close
os.startfile("re.txt")