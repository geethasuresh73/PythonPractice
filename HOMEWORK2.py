dict={1:"excellent",2:"good",3:"fair",4:"poor",5:"unacceptable"}

x=input("Please input grade")
print(dict.get(int(x)))

print(dict.keys())

for i,j in dict.items():
    print (i,j)
    #print(i,dict.get(i))
