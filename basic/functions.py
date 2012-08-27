def sqrt(x):
    ans = 0
    if (x >= 0):
        while ans*ans < x:
            ans += 1
        if ans*ans != x:
            print(x , 'is not a Integer square！\n')
            return None
        else:
            return ans
    else:
        print(x,'must > 0 !\n')
        return None

def f(x):
    x = x + 1
    return x

def fibonacci(x):
    if x == 1 or x == 0 : return 1
    else : return fibonacci(x - 1) + fibonacci(x - 2)

def squareRootBi(x,epsilon):
    assert x >= 0
    assert epsilon > 0
    low  = 0
    high = x
    guess = (low + high)/2.0
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 100:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
        ctr += 1
    assert ctr <= 100
    print (ctr,guess)
    return guess


a = squareRootBi(24,0.001)
print(a)

z = fibonacci(12)
print(z)

x = 3
x = f(x)
print(x)

y = sqrt(x)

print(y)
