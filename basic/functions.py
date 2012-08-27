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
    assert x >= 0, 'x must be non-negative ,not ' + str(x)
    assert epsilon > 0,'epsilon must be positive, not ' + str(epsilon)
    low  = 0
    high = max(x, 1.0)
    guess = (low + high)/2.0
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 100:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
        ctr += 1
    assert ctr <= 100, 'Iteration count exceeded'
    print ('Bi method  Num iterations:  ', ctr , 'answer : ' , guess)
    return guess


def squareRootNR(x , epsilon):
    assert x >= 0, 'x must be non-negative ,not ' + str(x)
    assert epsilon > 0,'epsilon must be positive, not ' + str(epsilon)
    x = float(x)
    guess = x/2.0
    #guess = 0.001
    diff = guess**2 - x
    ctr = 1
    while(abs(diff) > epsilon and ctr <= 100):
        guess = guess - diff/(2.0*guess)
        diff = guess**2 - x
        ctr += 1
    assert ctr <= 100 ,'Iteration count exceeded'
    print ('NR method  Num ,iterations: ', ctr ,'Answer : ',guess)
    return guess


squareRootBi(24,0.001)
squareRootNR(24,0.001)
squareRootBi(0.25,0.0001)
squareRootNR(0.25,0.0001)

z = fibonacci(12)
print(z)

x = 3
x = f(x)
print(x)

y = sqrt(x)

print(y)
