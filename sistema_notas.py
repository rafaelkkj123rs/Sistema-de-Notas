# Sistema de nota

import time
import os

os.system("cls")
os.system("title Sistema de notas")

nota = float(input("Digite a nota do Aluno: "))

if nota >= 7:
        time.sleep(1)
        print("Aprovado")
        time.sleep(0.8)
        print("Parabéns ")
else:
        print("Reprovado! Estude mais")
