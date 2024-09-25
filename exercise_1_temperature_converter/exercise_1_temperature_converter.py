temperature = int(input("Enter the temperature: "))
type = str(input("Do you want to convert it from Celsius to Fahrenheit or from Fahrenheit to Celsius? "))

if type == ("Celsius to Fahrenheit"):
    converted_temperature = (1.8 * temperature + 32)
    print(f"Your temperature from Celsius to Fahrenheit is {converted_temperature}° Fahrenheit")

elif type == ("Fahrenheit to Celsius"):
    converted_temperature = (temperature - 32) * 5 / 9
    print(f"Your temperature from Farenheit to Celsius is {converted_temperature}° Celsius")

else:
    print("Invalid conversion type. Please try again")