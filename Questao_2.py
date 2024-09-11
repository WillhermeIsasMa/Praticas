#Crinado a Função de Fibonacci
def fibo(n):
    
    #Imprimindo Casos dos dois primeiros numeros
    if n <= 0:
        return "Número deve ser maior que zero."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    #Calculando do 3 em diante 
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Recebe um numero para calcular função
num = int(input("Digite um número: "))
resul = fibo (num)
print(f"O número na sequência de Fibonacci é: {resul}")
