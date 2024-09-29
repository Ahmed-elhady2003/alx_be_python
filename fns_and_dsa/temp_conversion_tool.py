FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    result = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit-32)
    return result
def convert_to_fahrenheit(celsius):
    result = CELSIUS_TO_FAHRENHEIT_FACTOR * celsius -32

tem = float(input("Enter the temperature to convert: "))
typ = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if typ == "F":
   temp = convert_to_celsius(tem)
   print(f"{tem}°F is {temp}°C")
elif typ == "C":
   temp = convert_to_fahrenheit(tep)  
     print(f"{tem}°C is {temp}°F")
