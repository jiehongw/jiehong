n=int(input("please enter the test number:"))
primelist=[1]*n
primelist1=[]
for i in range(0,n):
    if primelist[i]==1:
        primelist1=primelist1+[i+2]
        for j in range(2*i+2,n,i+2):
            primelist[j]=0
odd=4
while odd<=n:
    sss=str(odd)
    for i in range(0,n):
        if primelist1[i]>(odd/2):
            break
        p2=odd-primelist1[i]
        if p2 in primelist1:
           sss=sss+"="+str(primelist1[i])+"+"+str(p2)
    print(sss)
    odd=odd+2
input("Press <enter>")  
