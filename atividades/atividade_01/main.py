
while True:
    
        gasolina = float(input("Informe o valor da gasolina: ").replace(",", "."))
        etanol = float(input("Informe o valor do etanol: ").replace(",", "."))

        if etanol / gasolina <= 0.7:
            print("Compensa abastecer com etanol.")
        else:
            print("Compensa abastecer com gasolina.")
        continuar = input("Deseja continuar? (s/n): ").strip()
        if continuar.lower() != 's':
            print("Programa encerrado.")
            continue
    
        