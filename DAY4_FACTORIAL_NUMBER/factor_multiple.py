def fact(l1,l2) :
    lis1=[]
    lis1=l1
    lis2=[]
    lis2=l2
    mult=1
    i=0
    j=0
    while i < len(lis1):
        j=0
        while j < len(lis2):
            if lis1[i] == lis2[j]:
                mult=mult*lis1[i]
                lis1.pop(i)
                lis2.pop(j)

            else:
                j=j+1

        i=i+1
    return mult

