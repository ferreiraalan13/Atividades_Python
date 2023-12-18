valor_compra = 0
parcelas = 0

valor_compra = float(input("Insira o valor total da compra: "))

parcelas = valor_compra / 5

print()

print(f"A compra será dividida em 5 parcelas igual de : R$ {parcelas:.2f}")
