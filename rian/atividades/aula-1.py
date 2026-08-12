import os
os.system('cls')

uni1 = float(input("Digite a 1° nota da unidade: "))
uni2 = float(input("Digite a 2° nota da unidade: "))
uni3 = float(input("Digite a 3° nota da unidade: "))

media = (uni1 + uni2 + uni3) / 3

if media >= 7:
    print(f"Aprovado!! Media: {media:.1F}")
elif media >=5 and media <=6.9:
    print(f"Recuperação!! Media: {media:.1F}")
else:
    print(f"Reprovado!! Media: {media:.1F}")