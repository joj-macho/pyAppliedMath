import matplotlib.pyplot as plt

def main():
    print('''Find The Roots of a Quadratic Equation f(x) = y = ax^2 + bx + c and Visualize them.\n''')
    a = input('Enter Value for a:\n> ')
    b = input('Enter Value for b:\n> ')
    c = input('Enter Value for c:\n> ')

    # Find the roots
    x1, x2 = findRoots(float(a), float(b), float(c))
    print(f'/nThe roots of the Quadratic Function y = {a}x^2 + {b}x + {c} are: ')
    print(f'x1 = {x1}\nx2 = {x2}')

    # Visualize the Roots
    # assume values of x
    a, b, c = float(a), float(b), float(c)
    xVal = range(-100, 101, 20)
    yVal = []
    for x in xVal:
        yVal.append((a)*(x**2) + (b)*(x) + c)
    
    plt.plot(xVal, yVal)
    plt.xlabel('$x$ values')
    plt.ylabel('$y$ values')
    plt.title(f'Graph of $f(x) = {a}x^2 + {b}x + {c}$')
    plt.show()

def findRoots(a, b, c):
    '''This function calculates the roots of a quadratic equation'''
    D = (b*b - 4*a*c)**0.5
    x1 = (-b + D)/(2*a)
    x2 = (-b - D)/(2*a)

    return x1, x2


if __name__ == '__main__':
    main()



