b=["keyboard","cpu","mouse","headset","monitor"]
print(b)
separator=","
result=separator.join(b)
print(result)

numbers="9,223;372:036 854,755;807"
separators =""
delimitors=numbers[1::4]
print(delimitors)
result=separators.join(char if char not in delimitors else " " for char in numbers)
print(result)

for char in numbers:
    if char not in delimitors:
        print (char)
    else:
        print(" ")