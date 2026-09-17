n1 = int(input("escreva um n1: "))
n2 = int(input("escreva o n2: "))
op = input("escreva a operacao desejada SOMA ou SUBTRACAO: ")


if(op == "soma"):
  print(n1 + n2)
elif(op == "subtracao"):
  print(n1 - n2)
else:
  print("codigo invalido")

