

def inverter (s):
    #String para guarda o valor
    invertida = ""
    
    #Inverte a String lendo do final para o inicio
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    
    return invertida


original = "  ESTÁ  AO  CONTRARIO  "
invertida = inverter (original)

print(f" String invertida: {invertida}")