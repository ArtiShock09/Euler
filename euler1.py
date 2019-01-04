def fib(n):
    a, b = 0, 1
    while a<n:
        yield a
        a, b = b, a + b

def even(n):
    a=2
    while a<n:
        yield a
        a=a*2


if __name__ == "__main__":
    res=0
    for i in list(fib(4000000)):
       if i%2==0:
           res=res+i
    print res

