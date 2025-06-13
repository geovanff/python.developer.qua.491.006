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
    
    nome = input("Digite seu nome: ")
    peso = float(input("Digite seu peso em kg: ").replace(",", "."))
    altura = float(input("Digite sua altura: ").replace(",", "."))
    calculo = peso / (altura ** 2)
    result =  "%.2f" % calculo
    imc = float(result)
    imc = round(imc, 2)  # Arredondar o IMC para 2 casas decimais
 
    
    print(f"{nome}, seu IMC é: {imc}")
    diagnostico = ""

    if imc < 18.5:
        diagnostico = "Abaixo do peso"
    elif 18.5 <= imc < 25:
        diagnostico = "Peso ideal"
    elif 25 <= imc < 30:
        diagnostico = "Acima do peso"
    elif 30 <= imc < 35:
        diagnostico = "Obeso"
    elif 35 <= imc < 40:
        diagnostico = "Obeso nível 2"
    else:
        diagnostico = "Obeso mórbido"
    
    print(f"Diagnóstico: {diagnostico}")
    # Pergunta se o usuário deseja refazer o cálculo

    opcao = input("Deseja refazer o cálculo? (s/n): ").lower().strip()
    match opcao:
        case 's':
            continue
        case 'n':
            break
        case _:
            print("Opção inválida.")
            continue

