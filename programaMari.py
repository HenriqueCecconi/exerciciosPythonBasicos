equipamentos, seqOperacoes, limCorrente = input().split()

equipamentos = int(equipamentos)
seqOperacoes = int(seqOperacoes)
limCorrente = int(limCorrente)

estado = [0] * equipamentos
consumo = []
operacoes = []
atualCorrente = 0
maxCorrente = 0
disjuntor = False

for i in range(equipamentos):
    entrada = int(input())
    consumo.append(entrada)

for j in range(seqOperacoes):
    entrada = int(input())
    operacoes.append(entrada)

for q in range(len(operacoes)):
    maquina = operacoes[q] - 1
    if estado[maquina] == 0:
        atualCorrente = atualCorrente + consumo[maquina] 
        estado[maquina] = 1
    else:
        atualCorrente =  atualCorrente - consumo[maquina]
        estado[maquina] = 0

    if atualCorrente > maxCorrente and not(disjuntor):
        maxCorrente = atualCorrente

    if atualCorrente > limCorrente and not(disjuntor):
        disjuntor = True
        maquinaQueda = operacoes[q]
        numOperacao = q + 1

if disjuntor == True:
    print("Oh no! O disjuntor sobrecarregou na operação (" + str(maquinaQueda) + ", " + str(numOperacao) + ").")
else:
    print("Bazinga! O maior consumo foi " + str(maxCorrente) + ".")
