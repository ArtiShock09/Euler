


def checkIsPrime(n):
    i=n-1
    while i>=2:
        if n%i==0:
            return False
        i-=1
    return True

def getPal():
    for i in reversed (range(9)):
        for j in reversed(range(10)):
            for k in reversed(range(10)):
                yield  (i+1)*100000+j*10000+k*1000+k*100+j*10+i+1
    yield 0


def addFact(fact,n):
    i=0
    l=len(fact)
    while i<l:
        m=fact[i]*n
        fact.append(m)
        i+=1
    return sorted(list(set(fact)))


def findPrimes6(n):
    res=[]
    fact=[1]
    while n%2==0:
        res.append(2)
        fact=addFact(fact,2)
        n=int(n/2)
    while n%3==0:
        res.append(3)
        fact = addFact(fact, 3)
        n=int(n/3)
    d=1
    while d<=n:
        f=[-1,1]
        for i in f:
            x=6*d+i
            while n%x==0:
                n=int(n/x)
                if checkIsPrime(x):
                    res.append(x)
                    fact = addFact(fact, x)

        d+=1
    return (res,fact)

if __name__ == "__main__":

    pal=getPal()
    n=1
    while n !=0:
        n = pal.next()
        (res, fact) = findPrimes6(n)
        a=0
        for i in  list(filter(lambda x: x >99 and x<1000, fact)):

            l=n/i
            if l>99 and l<1000:
                a=n
                break
        if a==n:
            break


    print a



