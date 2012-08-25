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

z = fibonacci(12)
print(z)

x = 3
x = f(x)
print(x)

y = sqrt(x)

print(y)
