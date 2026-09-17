n1 = int(input("escreva o primeiro numero: "))
n2 = int(input("Escreva o segundo numero: "))
operacao = float(input("escreva a operação: "))

if(operacao == "s"):
    print(n1 + n2)
elif(operacao == "su"):
    print(n1 - n2)
elif(operacao == "d"):
    print(n1 * n2)
elif(operacao == "m"):
    print(n1 / n2)