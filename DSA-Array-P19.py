# Find the common elements in 3 sorted array
def intersection(list1,list2,list3):
    list4 = [value for value in list1 if value in list2 and list3 ]
    return list4

list1 = []
print("Enter numbers of size of list:-")
num = int(input())
print("Enter Elements:-")
for i in range(0, num):
    ele1 = int(input())
    list1.append(ele1)
list1.sort()
list2 = []
print("Enter numbers of size of list:-")
num = int(input())
print("Enter Elements:-")
for i in range(0, num):
    ele2 = int(input())
    list2.append(ele2)
list2.sort()
list3 = []
print("Enter numbers of size of list:-")
num = int(input())
print("Enter Elements:-")
for i in range(0, num):
    ele3 = int(input())
    list3.append(ele3)
list3.sort()
print(intersection(list1,list2,list3))