# Finding the Roots of a Quadratic Equation + Plot

## Description

This function finds the roots of a quadratic equation using the quadratic formula.

## How it Works

- The quadratic equation for calculating roots is given by the formula: $$x_1=\frac{-b + \sqrt{b^2 - 4ac}}{2a},  x_2=\frac{b + \sqrt{b^2 - 4ac}}{2a}$$
Where $x_1$ and $x_2$ are the roots of the quadratic equation.
    - The function takes the the input of the function constants, a, b, and c.
    - Calculate the discriminent $D=\sqrt{b^2-4ac}$
    - Then calculate $x_1=\frac{-b + D}{2a}$ and $x_2=\frac{-b - D}{2a}$

- Finally visualize the function over a range using matplotlib.

## Program Input & Output

When you run the program `quad.py`, the output will look like this;

```
Find The Roots of a Quadratic Equation f(x) = y = ax^2 + bx + c and Visualize them.

Enter Value for a:
> 1
Enter Value for b:
> 2 
Enter Value for c:
> 1

The roots of the Quadratic Function y = 1x^2 + 2x + 1 are: 
x1 = -1.0
x2 = -1.0
```