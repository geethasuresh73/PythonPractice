n=[1,23,53,5,45,75,464]
print (n[2:])
#incorrect way of replacing or assignment in a list
n[2:]="1000"
print(n)
#correct way of replacing or assignment in a list
n[2:]=[100]
print(n)
#to delete last 2 elements from the list
n[1:]=[]
print(n)
n=[1,23,53,5,45,75,464]
#another way to delete last 2 elements in the list
del n[0:2]
print(n)