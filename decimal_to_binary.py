def add_binary(a,b):
    bin=''
    c=a+b
    if c!=1:
        while c//2>=1:
            q=c//2
            r=c%2
            c=q
            bin+=str(r)
            if c==1:
                bin+=str(c)
    else:
        bin='1'

    return bin[::-1]


#Another optimized way of doing it
def binary_con(a,b):
    return format(a+b,'b')
