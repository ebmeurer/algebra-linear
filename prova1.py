import math
from math import sqrt
import numpy as np 
from numpy import linalg as lin

num_elementos = 0
num_vetores = 0

def calcula_determinante(a):
    a = np.array(a)
    try:
        determinante = lin.det(a)
    except:
        return "Erro! Matriz passada não é quadrada"
    return determinante

def resolve_sistema(a,b):
    a = np.array(a)
    b = np.array(b)
    return lin.solve(a,b)

def set_matriz():
    global num_vetores
    num_vetores = int(input("Quantas linhas/colunas existem na matriz A? "))
    A = []
    for i in range(num_vetores):
        A.append([])
        for j in range(num_vetores):
            A[i].append(float(input("Digite o elemento  da posição "+str(i+1)+"-"+str(j+1)+" da matriz""(em decimal): ")))
        print("\n")
    return calcula_determinante(A)

def set_sistema():
    global num_vetores
    num_vetores = int(input("Quantas linhas/colunas existem na matriz A? "))
    A = []
    B = []
    for i in range(num_vetores):
        A.append([])
        for j in range(num_vetores):
            A[i].append(float(input("Digite o elemento o x"+str(j+1)+" da equação "+str(i+1)+"(em decimal): ")))
        B.append(float(input("Digite o resultado da equação "+str(i+1)+": ")))
        print("\n")
    return resolve_sistema(A,B)


def getFuncoes():
    return [["Determinante de uma matriz","prova1.set_matriz()"],["Resolução de um sistema","prova1.set_sistema()"]]