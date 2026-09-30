i = int
n1 = int(input("Digite o primeiro numero:"))
n2 = int(input("Digite o segundo numero: "))

inicio = min(n1, n2) + 1
fim = max(n1, n2)

for num in range(inicio, fim):
    print(num)