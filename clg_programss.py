
#GCD CALCUALTION 
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
print(gcd(98,30))

def linear_search(arr,key):
    for i in arr:
        if i == key:
            return i
    return -1


