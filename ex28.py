n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

if(n1>n2 and n1>n3):
    print(f"O maior numero e {n1}")
elif(n2>n1 and n1>n3):
    print(f"O maior numero e {n2}")
else:
    print(f"O maior numero e {n3}")