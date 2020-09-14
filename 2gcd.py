#divide and conquer gcd
# /2

def gcd(a,b): #must a>b

    if a < b :
        return gcd(b,a)
    
    if a==0 or b==0:#exit condition
        return a+b
    if a ==b: #exit condition
        return a


    if (a%2==0) and (b%2==0):
        return 2*gcd(a//2, b//2)

    if a%2==0:
        return gcd(a//2, b)
    elif b%2==0:
        return gcd(a, b//2)
    else:  #both odd
        return gcd((a-b)//2, b)


print(gcd(21,36))
print(gcd(17,7))

a =int(input('pls input num1:'))
b = int(input('pls input num2:'))
print('re:', gcd(a,b))

