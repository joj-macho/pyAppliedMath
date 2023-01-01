
def findFactors(n):
    '''This function finds the factors of a number'''
    factors = []
    for i in range(1, int(n) + 1):
        if n % i == 0:
            factors.append(i)
    
    return factors

if __name__ == '__main__':

    n = input('Enter An Integer to Factor.\n> ')
    n = float(n)
    if n > 0 and n.is_integer():
        print(f'Factors of {int(n)} are:')
        print(findFactors(n))
    else:
        print('Please Enter a Valid Positive Integer')