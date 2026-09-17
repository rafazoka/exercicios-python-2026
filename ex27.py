ano = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = int(0)

idade =  ano_atual - ano
print(f"idade em anos  {idade}")
print(f"Idade em meses  {idade * 12}")
print(f"Idade em dias {idade * 365}")
print(f"Idade em semanas {idade * 365 / 7}")
print(f"Idade em 2019 {2019 - ano}")