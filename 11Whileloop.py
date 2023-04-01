i=0
while i < 10:
    print(i)
    i+=1


# variable
available_exit=["north","south","east","west"]

a=""
while True :
    a = input("please enter value:")
    if a=="quit":
        print("you quitted the game")
        break

    if a in available_exit:
        print("you exitted from the game sucessfully")
        break

#binary search low = 0; high = 1000 user input in between

low=0
count=0
high=1000
a = int(input("please enter the number between 0 and 1000:"))
while True:
    count+=1
    if a <=1000 or a>0:
        print(low,high)
        mid= (low+high)//2
        if mid > a:
            high=mid
        elif mid<a:
            low=mid
        elif a==mid:
            print(count)
            break



