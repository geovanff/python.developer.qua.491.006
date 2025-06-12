# Declaração de variaveis
x = float(input("Informe o valor de x: ").replace(",", "."))
y = float(input("Informe o valor de y: ").replace(",", "."))

# menu
print(f"{'-'*20} ESCOLHA A OPERAÇÃO {'-'*20}\n")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")

# usuário escolhe a operação desejada
operador = input("Informe a operação desejada: ").strip()

# match case
match operador:
    case "1":
        print(f"A soma dos valores é {x+y}.")
    case "2":
        print(f"A subtração dos valores é {x-y}.")
    case "3":
        print(f"A multiplicação dos valores é {x*y}.")
    case "4":
        print(f"A divisão dos valores é {x/y}.")
    case _:  # default
        print("Operação inválida.")
    
    