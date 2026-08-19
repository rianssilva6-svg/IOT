carrinho = []

while True:
    produto = float(input("Digite o valor do produto: "))
    if produto == 0:
        break
    else:
        carrinho.append(produto)

total = sum(carrinho)
print(f"O total da compra é de R${total:.2f}")