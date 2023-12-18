preco_custo = float(input("Informe o preco de custo do produto: "))
percentual = float(input("Informe o acrescimo em % do produto: "))

valor_venda = ((preco_custo * percentual) / 100) + preco_custo

print()

print(f"O valor de venda do produto é: R$ {valor_venda}")