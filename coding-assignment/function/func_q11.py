# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_celsius = float(input("Enter the temperature in Celsius: "))
print(f"The temperature in Fahrenheit is {celsius_to_fahrenheit(temp_celsius):.2f}°F.")
