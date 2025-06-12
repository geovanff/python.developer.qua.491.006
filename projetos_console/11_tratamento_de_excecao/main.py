# tratamento de exceção
try:
    n = int(input("Informe um número inteiro: "))
    print(f"O número informado foi {n}.")
except Exception as e:
    print(f"Não foi possível exibir o número informado. {e}.")
finally:
    print("Programa encerrado com sucesso.")

