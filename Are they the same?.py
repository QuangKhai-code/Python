import math
def comp(a,b):
    print(a,b)
    c=[]
    d=[]
    if a==None or b==None:
        return False
    for j in sorted(a):
        c.append(abs(j))
    for l in sorted(b):
        d.append(math.sqrt(l))
    if sorted(c)==sorted(d):
        return True
    return False
