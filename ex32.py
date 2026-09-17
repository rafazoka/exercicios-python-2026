Fahrenheit = float(0)
Kelvin = float(0)
Graus = float(input("Escreva a temperatura em graus celsius: "))

Fahrenheit = (Graus * 9 / 5) + 32
Kelvin = Graus + 273.15

print("Resultado da conversão\n")
print(f"\nTemperatura em Fahrenheit: {Fahrenheit}, °F")
print(f"\nTemperatura em Kelvin: {Kelvin}, K\n")