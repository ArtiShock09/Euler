from  euler3  import findPrimes6

if __name__ == "__main__":
    n=100000
    mult=1
    for a in range(1,n):
        b = a*(a+1)/2
        (res,fact)=findPrimes6(b)
        if mult<len(set(fact)):
            mult=len(set(fact))
        print "our number is "+ str(b)+" divisors:"+str(len(set(fact)))
        if mult>=500:
            break

