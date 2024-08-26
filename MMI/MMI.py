from math import gcd
def MMI(a,n):
    if gcd(a,n) != 1:
        print("НОД a и n должен быть 1!!!")
        exit(0)
    else:
        integer = (a**(n-2)%n)
        return integer
print(MMI(3,7))