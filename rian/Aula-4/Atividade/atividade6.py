import time
import os
os.system('cls')

v_notas = []
mediaacima = []

print("===== Boletim =====")
for contador in range(8):
    nota = float(input(f"Digite a {contador+1}º nota do aluno: "))
    v_notas.append(nota)
    
media = sum(v_notas) / len(v_notas)

for nota in v_notas:
    if nota > media:
        mediaacima.append(nota)

print(f"Acima da média: {mediaacima:.1f}")

print(f"média: {media:.1f}")
