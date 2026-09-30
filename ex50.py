fat = int
num = int(input("Digite um numero inteiro: "))

fat = 1

for i in range(1, num + 1):
    fat = fat * i

    print(f"O fatorial de {num} e: {fat}")