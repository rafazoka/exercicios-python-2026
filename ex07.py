not1 = float (input("escreva a nota1: "))
not2 = float(input("escreva a nota2: "))
not3 = float(input("escreva a nota3: "))
not4 = float(input("escreva a nota4: "))
tarefa = input("escreva a disciplina")

calculo = (not1 + not2 + not3 + not4) / 4

if(calculo >= 7):
  print(f"voce passou de ano :) ")
else:
  print(f"voce nao passou de ano :( )")

print(f"em {tarefa} e sua media final: {calculo}")