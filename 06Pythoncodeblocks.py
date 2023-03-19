print ('Hello')
print('World')
a='the number is even'
b='the number is odd'
try:
    for i in range(0,100):
        if (i%2==0):
            print('after the first for loop' + a)
            for j in range (1,3):
                print('after the second for loop' + a)
        else:
            print(b)
    print ('*'*80)
except:
    print('there is an error in the program')