n=50
c=1
for i in range (1,n+1):
    k=0
    for j in range(1,i+1):
        if(i%j == 0):
            k=k+1
    if(k <= 2):
        c=c*i

print(c)


