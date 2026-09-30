centenas = int(0)
dezenas = int(0)
unidades = int(0)
num = int(input("Escreva um numero menor de 1000: "))
if(num >= 1000 or num < 0):
    print("numero invalido. Escolha outro numero menor que 1000: ")
else:
    centenas = num / 100
    dezenas = (num % 100) / 10
    unidades = num % 10

    print(f"{num} :")

    if(centenas > 0):
        if(centenas == 1):
            print(f"{centenas} centenas")
        else:
            print(f"{centenas} centenas")
        if(dezenas > 0 and unidades > 0):
            print(" ")
        elif(dezenas > 0):
            print(" e ")
if(dezenas > 0):
    if(dezenas == 1):
        print(f"{unidades} unidades")
    else:
        print(f"{unidades} unidades")
    if(unidades > 0 and unidades > 0):
        print(" ")
    else:
        print(" e ")
if(unidades > 0):
    if(dezenas > 1):
        print(f"{unidades} unidades")
    else:
        print(f"{unidades} unidades")
if(centenas == 0 and dezenas == 0 and unidades == 0):
    print("0 unidades")
