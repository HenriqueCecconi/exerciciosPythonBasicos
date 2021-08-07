linhas=int(input())
colunas=int(input())
matriz=[]
for i in range(linhas):
    linha=[]
    for j in range(colunas):
        notas=int(input())
        linha.append(notas)
    matriz.append(linha)
produto=[]
for i in range(linhas):
    soma=0
    for j in range(colunas):
        soma=soma+matriz[i][j]
    print(soma/len(matriz[0]))
    matriz[i].append(soma/colunas)
for i in range(linhas):
    for j in range(colunas + 1):
        matriz[i][j] = "%.2f" % matriz[i][j]

print(matriz)
        



    
        
            
    
    

