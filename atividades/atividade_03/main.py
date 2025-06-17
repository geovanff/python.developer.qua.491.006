# TODO - atividade: Crie um programa com o seguinte menu:
# - Calcular área de um circulo
# - Calcular tamanho de uma circuferencia
# - Sair do programa
# NOTE - para cada loop, o programa deverá limpar o terminal


import math as m
import os


while True:
    os.system("cls")
print("1 - Calcular área do círculo: ")
print("2 - Calcular circuferência: ")
print("3 - Sair")

opcao = input("Escolha uma opção: ")

if opcao =="1":
    raio = float(input("Informe o raio: "))
    area = math.pi * raio **2
