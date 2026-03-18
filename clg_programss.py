#GCD CALCUALTION 

'''
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
print(gcd(98,30))
'''

# linear search and binary search
'''

def linear_search(arr,key):
    for i in arr:
        if i == key:
            return i
    return -1

def bin_ser(arr,key):
    low,high=0,len(arr)
    
    while low < high:
        mid = (low + high )//2
        if arr[mid]==key:
            return mid
        elif arr[mid] < key:
            low=mid+1
        else:
            high = mid-1    
    return -1
arr=[1,2,3,4,5,6]
key=6
print("found" if linear_search(arr,key) != -1 else "not found the element")
print("found" if bin_ser(arr,key) != -1 else "not found the element")

'''
#power 

'''
base = int(input("enter the base mof number to calculate poer of that number"))
exp= int(input("enter the power of the number"))
res=1
for i in range(exp):
    res*=base
print(res)

'''

# to find the maximum of a list
'''
a=sorted(list((map(int,input('enter the numbers').split()))))
print(a)
print(max(a))
max=a[0]
for i in a:
    if i > max:
        max=i
print(max)
'''

#root of a number

'''
import math

n=int(input("enter the number to calculate the root"))
x=n
for i in range(10):
    x=.5*(x+n/x)

print(math.sqrt(n))
print(x)
'''
#selction sort
'''
def selection_sort(arr):
    for i in range(len(arr)):
        mid=i
        for j in range(i+1, len(arr)):

            if arr[j] < arr[mid]:
                mid=j
        arr[i],arr[mid]=arr[mid],arr[i]
    return arr

def liner_Search(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j >=0 and arr[j] >key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr    
    
print(liner_Search(arr=[9,7,6,5,43,2]))

'''
def merge(arr):
    if len(arr) > 1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merge(left)
        merge(right)

        lp=rp=fp=0

        while lp < len(left) and rp < len(right):
            if left[lp] < right[rp]:
                arr[fp]=left[lp]
                lp=lp=1
            else:
                arr[fp]=right[rp]
                rp+=1
                fp+=1

        while lp < len(left):
            arr[fp]=left[lp]
            lp+=1
            fp+=1
        while rp < len(left):
            arr[fp]=right[rp]
            rp+=1
            fp+=1
    return arr
print(merge(arr=[8,7,6,5,4,4,3,2,1]))