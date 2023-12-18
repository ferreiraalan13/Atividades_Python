categoria = 0
nome = input("Digite o nome do cliente: ")
idade = int(input("Digite a idade do cliente: "))
grupo_risco = input("Digite o grupo de risco: (Baixo | Medio | Alto)")

if idade < 17 or idade > 70:
    print("Faixa de idade fora dos requisitos.")

else:
    if idade >= 17 and idade <= 20:
        if grupo_risco.upper() == "BAIXO":
            categoria = 1
        else:
            if grupo_risco.upper() == "MEDIO":
                categoria = 2
            else:
                if grupo_risco.upper() == "MEDIO":
                    categoria = 3

    else:
        if idade >= 21 and idade <= 24:
            if grupo_risco.upper() == "BAIXO":
                categoria = 2
            else:
                if grupo_risco.upper() == "MEDIO":
                    categoria = 3
                else:
                    if grupo_risco.upper() == "MEDIO":
                        categoria = 4

        else:
            if idade >= 25 and idade <= 34:
                if grupo_risco.upper() == "BAIXO":
                    categoria = 3
                else:
                    if grupo_risco.upper() == "MEDIO":
                        categoria = 4
                    else:
                        if grupo_risco.upper() == "MEDIO":
                            categoria = 5

            else:
                if idade >= 35 and idade <= 64:
                    if grupo_risco.upper() == "BAIXO":
                        categoria = 4
                    else:
                        if grupo_risco.upper() == "MEDIO":
                            categoria = 5
                        else:
                            if grupo_risco.upper() == "MEDIO":
                                categoria = 6

                else:
                    if idade >= 65 and idade <= 70:
                        if grupo_risco.upper() == "BAIXO":
                            categoria = 7
                        else:
                            if grupo_risco.upper() == "MEDIO":
                                categoria = 8
                            else:
                                if grupo_risco.upper() == "MEDIO":
                                    categoria = 9

print(categoria)