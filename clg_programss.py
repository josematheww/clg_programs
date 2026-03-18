# 1 GCD CALCUALTION 

'''
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
print(gcd(98,30))
'''

# 2 linear search and binary search
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
# 3 power 

'''
base = int(input("enter the base mof number to calculate poer of that number"))
exp= int(input("enter the power of the number"))
res=1
for i in range(exp):
    res*=base
print(res)

'''

#4  to find the maximum of a list
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

# 5 root of a number

'''
import math

n=int(input("enter the number to calculate the root"))
x=n
for i in range(10):
    x=.5*(x+n/x)

print(math.sqrt(n))
print(x)
'''
# 6 selction sort
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
# 7 merge sort
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
'''

# 8 prime numbers
'''
n=int(input("enter the number of prime numbers you want to generate"))
count=0
num=2
while count < n:
    for i in range(2,int(num**.5) +1):
        if num % i ==0:
            break
    else:
        print(num , end=" ")
        count+=1
    num+=1
'''

#matrix multiplication
'''
a=[[1,2,3],
   [4,5,6]]
b=[[1,2],
   [3,4],
   [5,6]]

res=[[0,0],
     [0,0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            res[i][j]+=a[i][k]*b[k][j]
for i in res:
    print(i,)
'''

#count the numebrs of words in the text file
'''
import sys
 
if len(sys.argv)!=2:
    print("enter the proper file modulation")
else:
    with open (sys.argv[1], 'r') as f:
        text=f.read()
        word=len(text.split())
print(word)
'''