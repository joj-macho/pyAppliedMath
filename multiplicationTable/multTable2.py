
def main():
    print('\nMultiplication Table Generator\n')
    # Accept only numerical values.
    try:
        a = float(input('Enter a number:\n> '))
        n = float(input('Enter the number of multiples:\n> '))
        
        if not n.is_integer() or n < 0:
            print('The number of multiples should be a positive integer!')
        else:
            multiTable(a, int(n))
    except ValueError:
        print('You entered an invalid input')


def multiTable(a, n):
    '''This function prints the result of a*n '''
    for i in range(1, n+1):
        print('{0} x {1} = {2}'.format(a, i, a*i))

if __name__ == '__main__':
    main()