# Given a array which consists only 0,1,and 2. sort these elements without using any sorting algo
arr = [2,1,0]
brr =[]
n = len(arr)
for i in range(0,n ):
    if arr[i]<arr[i+1]:
        brr.append(arr[i])



print(brr)