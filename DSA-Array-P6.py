def union(list1,list2):
    list3 = (list1+list2)
    return list3
def intersection(lis1,list2):
    list4 = [ value for value in list1 if value in list2]
    return list4

list1 = [1,2,3,4,5,6]
list2 = [7,8,9,1,2,4]
print(union(list1,list2))
print(intersection(list1,list2))