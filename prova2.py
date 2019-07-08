import math
import numpy as np 
from numpy import linalg as lin

def dict_to_matrix(A, B):
    B.append(A)
    matrix = np.transpose(B)
    return matrix

def determinar_coordenadas(sistema):
    det_sistema = calcula_determinante(sistema, 3)
    b1 = calcula_determinante(sistema, 0)/det_sistema
    b2 = calcula_determinante(sistema, 1)/det_sistema
    b3 = calcula_determinante(sistema, 2)/det_sistema
    return b1,b2, b3

def calcula_determinante(matrix, index):
    matrix_aux = [['', '', ''], ['', '', ''], ['', '', '']]
    for i_index, i in enumerate(matrix):
        for j_index, j in enumerate(i):
            if(j_index == 3):
                continue
            elif(j_index == index):
                matrix_aux[i_index][j_index] = eval(matrix[i_index][3])
            else:
                matrix_aux[i_index][j_index] = eval(j)
    return np.linalg.det(np.array(matrix_aux))

def ler_entradas():
    A_aux = input('Insira aqui o vetor A, na forma (X;Y;Z): ').replace('(', '').replace(')', '').replace(' ', '')
    A = A_aux.split(';')
    B = []
    for i in range(3):
        vetor_aux = input(f'Insira o vetor B{i+1}, na forma(X;Y;Z): ').replace('(', '').replace(')', '').replace(' ', '')
        vetor_aux = vetor_aux.split(';')
        for index, element in enumerate(vetor_aux):
            vetor_aux[index] = f'{element}b{i+1}'
        B.append(vetor_aux)
        #print(vetor_aux)
    return(A, B)

def resolve_sistema():
    A, B = ler_entradas()
    #A, B = ['7', '8', '6'], [['2', '3', '7'],['18', '-1', '8'],['-5', '6', '9']]
    sistema = dict_to_matrix(A, B)
    b1, b2, b3 = determinar_coordenadas(sistema)
    #print(f'A[B] = [{b1} {b2} {b3}]')
    return b1, b2, b3

def getFuncoes():
    return [['Coordenadas do vetor', 'prova2.resolve_sistema()']]

if __name__ == "__main__":
    resolve_sistema()
