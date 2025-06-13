# Laço de repetição
while True:
# tratamento de exceção
    try:
        # entrada de dados
        gasolina = float(input("Informe o valor da gasolina: ").replace(",", "."))
        etanol = float(input("Informe o valor do etanol: ").replace(",", "."))
        calculo = (etanol/gasolina)*100
        result = "gasolina" if calculo > 70 else "etanol"
        
        print(f"Resultado = {calculo:.2f}%. Compensa abastecer com {result}.")

        opcao = input("Deseja refazer o cálculo? (s/n): ").lower().strip()
        match opcao:
            case 's':
                continue
            case 'n':
                break
            case _:
                print("Opção inválida.")
                continue
    except Exception as e:
        print(f"Não foi possível executar operação. {e}.")
        continue
    
        