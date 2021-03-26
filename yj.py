import os
a=[28500,52300,63400,66500,71600,
       75700,77700,86300,107900,112200,114100,128300,155300,179550,189900,190700,
       212200,224400,232500,241600,247200,254800,273900,287100,305500,382200,
   384800,431500,461500,463400,528400,746800,776700,808000]
b=dict()
while(True):
    b.clear()
    sum=int(input("총 얼마?"))
    for i in range(0,len(a)):
        if(a[i]>sum):
            break
        else:
            for j in range(0,int(sum/min(a))):
                tmp=a[i]*j
                if(sum<tmp):
                    b[sum-(a[i]*(j-1))]=str(format(a[i], ','))+" * "+str(j-1)
                    break
    minnum=min(b)
    keystr=format(minnum, ',')
    print(b[minnum],"차액",keystr)
