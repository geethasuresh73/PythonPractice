dict={1:"excellent",2:"good",3:"fair",4:"poor",5:"unacceptable"}

x=input("Please input grade")
print(dict.get(int(x)))

print(dict.keys())

for i in range(1,6):
    print(i,dict.get(i))
