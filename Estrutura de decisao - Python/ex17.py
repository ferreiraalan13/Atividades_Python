time1 = input("Informe o primeiro time:")
time2 = input("Informe o segundo time: ")

gols_time1 = int(input(f"Quantos gols o {time1} marcou? "))
gols_time2 = int(input(f"Quantos gols o {time2} marcou? "))

if gols_time1 == gols_time2:
    print("O resultado do jogo foi EMPATE")
else:
    if gols_time1 > gols_time2:
        print(f"O vencedor do jogo foi: {time1} por {gols_time1} x {gols_time2}")
    else:
        print(f"O vencedor do jogo foi: {time2} por {gols_time2} x {gols_time1}")
