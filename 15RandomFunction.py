import random
high=1000
low=1
result=random.randint(low,high)
print("Random number is ", result)
while True:
    b=(high+low)//2
    if result > b:
       low=b
       print (b,"low")
       continue
    elif result < b:
        high=b
        print (b,"high")
        continue
    elif result==b:
        print("We found the number",b)
        break
