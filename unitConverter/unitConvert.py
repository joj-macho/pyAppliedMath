def main():
    print('\nUnit of Measurement Converter\n')

    # Display options
    print('1. Length: Kilometers to Miles')
    print('2. Length: Miles to Kilometers')
    print('3. Mass: Kilograms to Pounds')
    print('4. Mass: Pounds to Kilograms')
    print('5. Temperature: Celsius to Fahrenheit')
    print('6. Temperature: Fahrenheit to Celsius')

    # Do the conversion
    response = input('Select the option number of your choice.\n> ')

    if response == '1':
        kmToMiles()
    if response == '2':
        milesToKm()
    if response == '3':
        kgToPounds()
    if response == '4':
        poundsToKg()
    if response == '5':
        celsiusToFahren()
    if response == '6':
        fahrenToCelsius()


def kmToMiles():
    km = float(input('Enter distance in kilometers:\n> '))
    miles = km / 1.609
    print('Distance in miles: {0}'.format(miles))

def milesToKm():
    miles = float(input('Enter distance in miles:\n> '))
    km = miles * 1.609
    print('Distance in kilometers: {0}'.format(km))

def kgToPounds():
    kg = float(input('Enter weight in kilograms:\n> '))
    pounds = kg * 2.205
    print('Weight in pounds: {0}'.format(pounds))

def poundsToKg():
    pounds = float(input('Enter weight in pounds:\n> '))
    kg = pounds / 2.205
    print('Weight in kilograms: {0}'.format(kg))

def celsiusToFahren():
    celsius = float(input('Enter temperature in Celsius:\n> '))
    fahrenheit = celsius*(9 / 5) + 32
    print('Temperature in fahrenheit: {0}'.format(fahrenheit))

def fahrenToCelsius():
    fahrenheit = float(input('Enter temperature in Fahrenheit:\n> '))
    celsius = (fahrenheit - 32)*(5/9)
    print('Temperature in celsius: {0}'.format(celsius))


if __name__ == '__main__':
    main()
