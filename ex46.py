tabu = int(input("Digite o numero da tabuada desejada: "))
i = int
if(tabu<10 and tabu>0):
    for num in range (0, 10):
        print(f"{num} x {i} = {tabu*num}")
else:
    print("Digite um numero entre 0 a 10")