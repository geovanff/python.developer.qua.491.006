# TODO - atividade: crie um programa que receba do usuario, o nome, o peso em kg, e a altura em metros, e calcule o valor do IMC (Indice de Massa Corporal). 
# O programa deve mostrar o valor do IMC arredondado para 2 casas decimais, e mostrar o diagnostico do usuario com base nos seguintes valores:
# - Caso o IMC seja menor que 18.5 = abaixo do peso.
# - Caso o IMC seja maior ou igual 18.5 e menor que 25 = peso ideal.
# - Caso o IMC seja maior ou igual a 25 e menor que 30 = acima do peso.
# - Caso o IMC seja maior ou igual a 30 e menor que 35 = obeso.
# - Caso o IMC seja maior ou igual a 35 e menor que 40 = obeso nivel 2.
#  - Caso o IMC seja maior ou igual a 40 = obeso morbida.
# NOTE - O usuario deverá informar o encerramento do programa, ou seja, ele poderá repetir o calculo quantas vezes quiser.
"""""" 

while True:

    try:
        nome = input("Digite seu nome: ").title().strip()
        peso = float(input("Digite seu peso em kg: ").replace(",", "."))
        altura = float(input("Digite sua altura: ").replace(",", "."))
        imc = peso / altura **2

        print(f" Ovalor do IMC é: {imc:.2f}.")
    
        if imc < 18.5:
            print("{nome} Abaixo do peso.")
        elif imc < 25:
            print(f"{nome} Peso ideal.")
        elif imc < 30:
            print(f"{nome} Acima do peso.")
        elif imc < 35:
            print(f"{nome} Obeso.")
        elif imc < 40:
            print(f"{nome} Obesidade nível 2.")
        else:
            print(f"{nome} Obesidade mórbida.")

        while True:
            prosseguir = input("Deseja refazer? (s/n)").lower().strip()
            if prosseguir == "s" or prosseguir == "n":
                break
            else:
                print("Opção inválida.")
                continue

        match prosseguir:
            case "s":
                continue
            case "n":
                break

    except Exception as e:
        print(f"Não foi possível calcular o IMC. {e}")
        continue




