# Converting Units of Measurement

## Description

- This program is a unit conversion program that will do the following conversions:  
    - Units of length; kilometers to miles, and vice-versa.
    - Units of mass; kilograms to pounds, and vice-versa.
    - Units of temperature Celsius to Fahrenheit, and vice-versa.

## How it Works

- The `main()` function is called, which prints a list of conversion choices to select from. If the choice is entered as 1 (kilometers to miles), the function `kmToMiles()` is called. If the choice is entered as 2 (miles to kilometers), the function `milesToKm()` is called, and so on.
- In all of these functions, the user is first asked to enter a distance in the unit chosen for conversion (kilometers for kmkmToMiles_miles() and miles for milesToKm()). The program then performs the conversion using the corresponding formula and displays the result.

## Program Input & Output

When you run the program `unitConvert.py`, the output will look like this;
```
Unit of Measurement Converter

1. Length: Kilometers to Miles
2. Length: Miles to Kilometers
3. Mass: Kilograms to Pounds
4. Mass: Pounds to Kilograms
5. Temperature: Celsius to Fahrenheit
6. Temperature: Fahrenheit to Celsius
Select the option number of your choice.
> 2
Enter distance in miles:
> 100
Distance in kilometers: 160.9
```