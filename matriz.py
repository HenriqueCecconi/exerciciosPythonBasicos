linhas = int(input())
colunas = int(input())
matriz=[]

for i in range(linhas):
    linha=[]
    for j in range(colunas):
        linha.append(int(input()))
    matriz.append(linha)

for i in range(linhas):
    for j in range(colunas):
        if j%2 != 0:
            matriz[i][j] = (matriz[i][j])*3
            
for i in range(linhas):
    print(str(int(matriz[i][0])) + " " + str(int(matriz[i][1])) + " " + str(int(matriz[i][2])))
    