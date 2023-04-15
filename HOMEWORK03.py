import os


file1=open('./resources/config.cfg','r')
alllines = file1.readlines()
for line in alllines:
    print(line)
file1.close()
print('Enter matrix - ')
count=0
y=[[0],[0],[0]]
while True:
    print(count)
    x=input()
    y[count]=x.split(' ')
    print(y[count])
    count += 1
    if count==len(y[0]):
        break

sep=","
res=[['','',''],['','',''],['','','']]

k=len (y[0])
for j in range(0,k):
    for i in range(0,k):
        #print(y[i][j])
        res[j][i]=y[i][j]
        #print (y[i][j],y[i][j],y[i][j])

for i in range(0,k):
    res[i] = sep.join(res[i])
    res[i] = res[i].replace(",", " ")
    print(res[i])



