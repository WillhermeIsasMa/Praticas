#Faturamentos estaduais 
f_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calculo do valor total 
tt_mensal = sum(f_estados.values())

# Calculo do persentual estadual
perc = {estado: (valor / tt_mensal) * 100 for estado, valor in f_estados.items()}

print(f"Os Percentuais estaduais são: ")

for estado, percentual in perc.items():
    print(f"{estado}: {percentual:.2f}%")
