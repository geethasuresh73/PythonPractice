letter="parrot"
for i in range(0,len(letter)):
    print(letter[i])


for i in letter:
    print(i)

a = 'GeethaSuresh'
b=''
for i in range(len(a)-1,-1,-1):
    b = b + a[i]
print(b)


for i in range(0,len(a)-1,2):
    print(a[i])

numbers='9,223;372:036 854,755;807'
b=''
c=''
for a in numbers:
    if not a.isnumeric():
       b=b+a
    else:
       c=c+a
print(b)
print(c)

for a in numbers:
    if not a.isnumeric():
       numbers=numbers.replace(a,'')

print(numbers)
