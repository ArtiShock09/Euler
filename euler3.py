


def checkIsPrime(n):
    i=n-1
    while i>=2:
        if n%i==0:
            return False
        i-=1
    return True



def findPrimes6(n):
    res=[]
    if n%2==0:
        res.append(2)
        n=int(n/2)
    if n%3==0:
        res.append(3)
        n=int(n/3)
    d=1
    while d<=n:
        f=[-1,1]
        for i in f:
            x=6*d+i
            if n%x==0:
                n=int(n/x)
                if checkIsPrime(x):
                    res.append(x)
        d+=1
    return res


if __name__ == "__main__":

    res=findPrimes6(600851475143)
    print max(res)
