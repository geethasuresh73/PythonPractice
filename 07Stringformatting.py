for i in range(1,13):
    print ('number is',str(i),'squared is',str(i**2),'cube is',str(i**3))
    print (f'number is {i},squared is {i**2},cube is {i**3}')
    print('number is {0},squared is {1},cube is {2}'.format(i,i**2,i**3))
    print('number is {1},squared is {0},cube is {0}'.format(i, i ** 2, i ** 3))