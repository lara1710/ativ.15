# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.

numero1 = int(input("digite seu valor:"))
numero2 = int(input("digite seu valor:"))

resultado = 0

operacao = input("digite sua operação aqui:")

if operacao == "soma":
    resultado = numero1 + numero2
    print(F"{resultado}")

elif operacao == "subtração":
    resultado = numero1 - numero2
    print(F"{resultado}")

elif operacao == "multiplicação":
    resultado = numero1 * numero2
    print(F"{resultado}")

elif operacao == "divisão":
    resultado = numero1 / numero2
    print(F"{resultado}")