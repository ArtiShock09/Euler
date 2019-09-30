import math

def findb(a):
    flag=1000*(500-a)%(1000-a)==0
    if flag :
        return 1000 * (500 - a) / (1000 - a)
    else:
        return 0

def findabc():
    n=range(1,499)
    for a in n:
        b= findb(a)
        if b !=0:
            c= math.sqrt(a*a+b*b)
            print(" A and B and C %s, %s, %s " % (a, b,c))
            return  a*b*c
    return 0

if __name__ == "__main__":
    abc=findabc()
    print abc

