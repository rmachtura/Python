#Calculadora Python

def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

def inicia_Calculadora(operacao):
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    
    if operacao == 1:
        print("O resultado da soma é: ", somar(num1, num2))
    elif operacao == 2:
        print("O resultado da subtração é: ", subtrair(num1, num2))
    elif operacao == 3:
        print("O resultado da multiplicação é: ", multiplicar(num1, num2))
    else:
        print("O resultado da divisão é: ", dividir(num1, num2))

print("**--Calculadora Python--** \n")
print("Selecione o número da operação desejada: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n")
operacao = int(input("Digite sua opção: "))

if operacao > 4 or operacao < 1:
    print("Opção inválida!")
else:
    inicia_Calculadora(operacao)