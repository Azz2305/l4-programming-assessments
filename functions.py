def convert_temperature():
    temp = float(input("Enter temperature: "))
    if input("Convert to (C)elsius or (F)ahrenheit? ").upper() == 'C':
        print(f"{(temp - 32) * 5/9:.2f}°C")
    else:
        print(f"{(temp * 9/5) + 32:.2f}°F")
convert_temperature()