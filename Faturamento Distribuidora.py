faturamento_mensal_sp = 67836.43
faturamento_mensal_rj = 36678.66
faturamento_mensal_mg = 29229.88
faturamento_mensal_es = 27165.48
faturamento_mensal_outros = 19849.53
faturamento_mensal_total = faturamento_mensal_outros + faturamento_mensal_es + faturamento_mensal_mg + faturamento_mensal_rj + faturamento_mensal_sp

def porcentual (parte, total):
    porcentual = 100 * float(parte)/float(total)
    return float(porcentual)

print("1-São Paulo | 2-Rio de Janeiro | 3- Minas Gerais | 4-Espirito Santos | 5- Outros")
escolha = input("Informe o estado que deseja saber o porcentual de faturamento mensal:")

if escolha == "1":
    print(round(porcentual(faturamento_mensal_sp, faturamento_mensal_total),2))
elif escolha == "2":
    print(round(porcentual(faturamento_mensal_rj, faturamento_mensal_total),2))
elif escolha == "3":
    print(round(porcentual(faturamento_mensal_mg, faturamento_mensal_total),2))
elif escolha == "4":
    print(round(porcentual(faturamento_mensal_es, faturamento_mensal_total),2))
elif escolha == "5":
    print(round(porcentual(faturamento_mensal_outros, faturamento_mensal_total),2))
else:
    print("A opção escolhida não existe")
