import math

num_elementos = 0
num_vetores = 0

def get_produto_interno():
    global num_elementos
    num_elementos = int(input("Quantos elementos existem nos vetores de A? "))
    A = []
    for i in range(2):
        A.append([])
        for j in range(num_elementos):
            A[i].append(float(eval(input("Digite o elemento "+str(j+1)+" do Vetor A"+str(i+1)+": "))))
        print("\n")
    return produto_interno(A[0],A[1])

def get_norma_de_A():
    global num_elementos
    num_elementos = int(input("Quantos elementos existem no vetor A? "))
    A = []
    for j in range(num_elementos):
        A.append(float(eval(input("Digite o elemento "+str(j+1)+" do Vetor A: "))))
    print("\n")
    return norma_de_A(A)


def produto_interno(a,b):
    global num_elementos
    B = 0.0
    for i in range(num_elementos):
        B = B +(a[i]*b[i])
    return B

def norma_de_A(a):
    return math.sqrt(produto_interno(a,a))

def calcular_Bx(c):
    global num_elementos
    B = []
    for i in range(num_elementos):
        B.append((1/norma_de_A(c))*c[i])
    return B

def calcular_Cx(a,b):
    C = []
    global num_elementos
    len_b = len(b)
    Baux = 0
    for i in range(num_elementos):
        for j in range(len_b):
            Baux = Baux + float(produto_interno(a[len_b],b[j])*b[j][i])
        Baux -= a[len_b][i]
        C.append(Baux)
        Baux = 0
    print("C"+str(len_b+1)+"= "+str(C))
    return C
        
def gram_schimidt():
    global num_vetores
    global num_elementos
    num_vetores = int(input("Quantos vetores existem no conjunto A? "))
    if num_vetores < 2:
        print("Conjunto muito curto")
    num_elementos = int(input("Quantos elementos existem nos vetores de A? "))
    A = []
    for i in range(num_vetores):
        A.append([])
        for j in range(num_elementos):
            A[i].append(float(eval(input("Digite o elemento "+str(j+1)+" do Vetor A"+str(i+1)+": "))))
        print("\n")
    B_output = []
    B_output.append(calcular_Bx(A[0]))
    for i in range(1,num_vetores):
        B_output.append(calcular_Bx(calcular_Cx(A,B_output)))
    print("\n")
    retorno = "B = {\n"
    for i in range(len(B_output)):
        retorno += "B"+str(i+1)+"= "+str(B_output[i])+",\n"
    retorno += "}"
    return retorno

def calcula_angulo():
    global num_elementos
    num_elementos = int(input("Quantos elementos existem nos vetores? "))
    A = []
    for i in range(2):
        A.append([])
        for j in range(num_elementos):
            A[i].append(float(eval(input("Digite o elemento "+str(j+1)+" do Vetor A"+str(i+1)+": "))))
        print("\n")
    cos = (produto_interno(A[0],A[1]))/(norma_de_A(A[0])*norma_de_A(A[1]))
    angulo = math.acos(cos)
    angulo = math.degrees(angulo)
    return angulo

def getFuncoes():
    return [["Produto interno","prova3.get_produto_interno()"],["Norma de A","prova3.get_norma_de_A()"],["Gram-Schimidt","prova3.gram_schimidt()"],["Angulo entre dois vetores","prova3.calcula_angulo()"]]