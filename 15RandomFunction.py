import random
high=1000
low=1
result=random.randint(low,high)
print("Random number is ", result)

count=0
while True:
    b=(high+low)//2
    if result > b:
       low=b
       print (b,"low")
       count+=1
       continue
    elif result < b:
        high=b
        print (b,"high")
        count += 1
        continue
    elif result==b:
        print("We found the number",b," In",count," attempts")
        break
