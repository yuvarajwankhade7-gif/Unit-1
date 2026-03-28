#1. Create and access list elements
#2. Add and Remove list elements
#3. Sort list element
#4. Reverse list element




list1= [1,2,3,4,5]

list2 = list(map(int,input("Enter list of integers:").strip().split()))

print(list1,list2)


list1=[1,2,3,4,5,6,7]
print(list1[3:-1])
print(list1[5])


list1=[1,2,3,4]
list1 = list1+[5]
list1.insert(len(list1),6) 
list1[-1] = 7             
print(list1)


list1=[1,2,3,4,5,6,7]
list1.remove(5)
print(list1)


list1 = [2,4,3,1,6]
list1.sort()

list1 = [2,1,4,3,9,6,5,8]
sorted_list1 = sorted(list1)
print(sorted_list1)


list1=[1,2,3,4,5,6,7,8,9,10]
list1.reverse()

list1=[1,2,3,4,5,6,7,8,9,'a','b','c']

if 1 in list1:
    print("YES")
print(list1[::-1])