#Program to find the kth max and min. number from list.
#Creating List
arr = []
print("Enter numbers of elements in list:-")
num = int(input())
for i in range(0, num):
    ele = int(input())
    arr.append(ele)
print(arr)
arr.sort()
print(arr)
L = len(arr)
print("Enter Kth value for max:-")
M = int(input())
print(arr)
print(arr[L-M])
print("Enter value for kth min:-")
N = int(input())
print(arr[N-1])