import prova1
import prova2
import prova3

funcoes = []

funcoes += prova1.getFuncoes()
funcoes += prova2.getFuncoes()
funcoes += prova3.getFuncoes()

print("Escolha o metodo a ser calculado")
for i in range(len(funcoes)):
    print(str(i+1) + "- "+ str(funcoes[i][0]))
choice = int(input())-1
print(eval(funcoes[choice][1]))

