# Q7. Ask the user for a temperature in Celsius(String input).Convert it to float, then calculate and print temperature in Fahrenheit
#Conversion Formula: FahrenheitTemp = (CelsiusTemp * (9/5))+32
celsius_str=input("Enter the temperature in Celsius: ")
celsius=float(celsius_str)
Fahrenheit = (celsius * (9/5))+32
print("Temperature in fahrenheit: ",Fahrenheit)