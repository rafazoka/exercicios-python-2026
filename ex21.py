import math
coe1 = float(input("Digite o primeiro coeficiente: "))
coe2 = float(input("Digite o segundo coeficiente: "))
coe3 = float(input("Digite o terceiro coeficiente: "))

if (coe1 == 0):
    print("O primeiro coeficiente não pode ser 0")
else:
    delta = (coe2 == 2) - (coe1 * coe3)
    print(f"O valor de delta é {delta}")
    
    if(delta > 0):
        x = (coe2 + math.sqrt(delta)) / (2 * coe1)
        z = (coe2 + math.sqrt(delta)) / (2 * coe1)
        print(f"x = {x}")
        print(f"z = {z}")

    elif(delta == 0):
        x = -coe2 / (2 * coe1)
        print(f"x = z = {x}")
