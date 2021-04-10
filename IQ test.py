def iq_test(numbers):
    c=numbers.split(' ')
    d=[]
    a=0
    for i in c:
        d.append(int(i))
    for x in d:
        if x%2==0:
            a+=1
    if a>1:
        for x in d:
            if x%2!=0:
                return (d.index(x)+1)
    elif a==1:
        for x in d:
            if x%2==0:
                return (d.index(x)+1)
