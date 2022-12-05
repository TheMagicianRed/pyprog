# This function computes the n-th power of a without using built-in functions.
def power(a, n):
    p = 1
    for i in range(0, n):
        p = a * p

    return p

# This function computes the n times with a is multiplicated.
def sumn(a, n):
    s = 0
    for i in range(0, n):
        s = s + a
    return s


# This function sum the n first(s) number(s)
def sumfn(n):
    s = 0
    for i in range(0, n):
        s = s + i + 1
    return s

# This function sum the n first(s) number(s)
def sumfn(n):
    s = 0
    for i in range(0, n+1):
        s = s + i
    return s
        
# This function sum the n first(s) number(s)
def sumfnnew(n):
    s = 0
    for i in range(0, n):
        s = s + i + 1
    return s


def rpow(a, n):
    if n == 0:
        return 1 
    else:
        return a * rpow(a, n-1)


def sumfrn(n):
    if n == 0:
        return 0
    else: 
        return n + sumfrn(n-1)



