temperature = int(input("Enter the temperature: "))
type = str(input("Do you want to convert it from Celsius to Fahrenheit or from Fahrenheit to Celsius? "))

if type == ("Celsius to Fahrenheit"):
    converted_temperature = (1.8 * temperature + 32)
    