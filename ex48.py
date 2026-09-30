par = int
impar = int
n1 = int(input("Escreva n1: "))
n2 = int(input("Escreva n2: "))
n3 = int(input("Escreva n3: "))
n4 = int(input("Escreva n4: "))
n5 = int(input("Escreva n5: "))
n6 = int(input("Escreva n6: "))
n7 = int(input("Escreva n7: "))
n8 = int(input("Escreva n8: "))
n9 = int(input("Escreva n9: "))
n10 = int(input("Ecsreva n10: "))

par = (1 - n1 % 2) + (1 - n2 % 2) + (1 - n3 % 2) + (1 - n4 % 2) + (1 - n5 % 2) + (1 - n6 % 2) + (1 - n7 % 2) + (1 - n8 % 2) + (1 - n9 % 2) + (1 - n10 % 2)
impar = 10 - par

print(f"Quantidade de numeroa pares {par}")
print(f"Quantidade de numeros imapares {impar}")