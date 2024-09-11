import json


#Carregando os dados
with open('faturamento.json') as file:
    dados = json.load(file)

# Extrandindo os valores sem nulos
f_diario = [ valor for valor in dados.values() if valor is not None]

# Validando dados para analise
if f_diario:
    
    # Calcular o menor e maior faturamento
    f_menor = min(f_diario)
    f_maior = max(f_diario)

    # Calcular a média mensal
    media = sum(f_diario) / len(f_diario)

    # Contador de dias > que a media
    s_media = sum(1 for valor in f_diario if valor > media)

    print(f"Menor faturamento é: {f_menor}")
    print(f"Maior faturamento é: {f_maior}")
    print(f"Dias com faturamento acima da média: {s_media}")
else:
    print("Não a dados mensais validos")
