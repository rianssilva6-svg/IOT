import os
os.system('cls')

temperatura = []

for count in range(5):
    temp = float(input(f"Digite a {count+1}° temperatura: "))
    temperatura.append(temp)
    
media = sum(temperatura) / len(temperatura)
menor = min(temperatura)
maior = max(temperatura)

print("\n")
print("===== Resultado =====")
print(f"A maior temperatura do dia: {maior} °C")
print(f"A menor temperatura: {menor} °C")
print(f"A media temperatura: {media:.1f} °C")