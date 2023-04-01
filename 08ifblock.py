a=int(input("please enter your age:"))
print(type(a))
print(a)
if a>18:
    print("you are allowed to vote")
elif a==18:
    print("congratulations!! you are allowed to vote!")
else:
    b=18-a
    print("please come back after",b,"years")
day="friday"
temprature=27
raining=False

if day=="saturday" and temprature==27 or not raining:
    print("go out")
else:
    print("stay back")

parrot="norwegianblue"
letter=input("please enter the string:")
if len(letter)==0:
    letter=None

if letter is not None and letter.casefold() in parrot.casefold():
    print("it is")
    print(letter)
else:
    print("it is not")

