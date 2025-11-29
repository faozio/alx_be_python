fahrenheit_to_celsius_factor = 5/9
celsius_to_fahrenheit_factor = 9/5

def convert_to_fahrenheit(celsius):
    return celsius * celsius_to_fahrenheit_factor + 32  

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * fahrenheit_to_celsius_factor

prompt_temperature = float(input("Enter the temperature to convert: "))
prompt_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

if prompt_unit == "c":
    celsius = prompt_temperature
    fahrenheit = convert_to_fahrenheit(celsius)
    print(f"{celsius}°C is {fahrenheit}°F")
elif prompt_unit == "f":
    fahrenheit = prompt_temperature
    celsius = convert_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is {celsius}°C")
else:
    print("Invalid unit. Please enter C or F.")