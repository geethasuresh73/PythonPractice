
def fibonaciSeries(n):
    if n>=0 and n<=1:
        return n
    n_minus1,n_minus2=1,0
    result = None
    for i in range(n-1):
        result = n_minus1+n_minus2
        n_minus2=n_minus1
        n_minus1=result
    return result

for i in range(70):
    print(i,fibonaciSeries(i))

#input string is a palindrome

text=input("please input your text")


def palidrome(text):
    b = ""
    for i in range(1,len(text)+1):
        b=b+text[-i]
    return b
if (palidrome(text)==text):
    print("Text entered is a palidrome")
else:
    print("Text entered is not a palidrome")