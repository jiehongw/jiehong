n=int(input("please enter the test number:"))
primelist=[1]*n
f=open('F:\Working Files\python\prime.txt','w')
for i in range(0,n):
    if primelist[i]==1:
        f.write("%d\n"%(i+2))
        for j in range(2*i+2,n,i+2):
            primelist[j]=0
f.close()
