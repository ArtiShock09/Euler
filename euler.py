
def mult35(n):
    sum=0
    for i in range(n):
        if i%3==0 or i%5==0:
            sum=sum+i
    return sum

def gauss(n):
    return  n*(n+1)/2

if __name__ == "__main__":
    print mult35(1000)
    print 3*gauss(333)+5*gauss(199)-15*gauss(66)