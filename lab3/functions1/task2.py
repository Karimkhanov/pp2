
'''Read in a Fahrenheit temperature. 
Calculate and display the equivalent centigrade temperature.
The following formula is used for the conversion.'''

def fahrenheit_to_centigrade(fahrenheit_temperature):
    centigrade_temperature = (5 / 9) * (fahrenheit_temperature - 32)
    return centigrade_temperature
print(fahrenheit_to_centigrade(float(input())))         