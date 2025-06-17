# Importar Biblioteca
import math as m

# exibe nº do pi
print(f"Número do pi: {m.pi}.")

# Raiz quadrada
try:
    n = int(input("Informe um número inteiro: "))
    print(f"A raiz quadrada de {n} é {m.sqrt(n):.2f}.")
except Exception as e:
    print(f"Não foi possível calcular a raiz quadrada. {e}.")
