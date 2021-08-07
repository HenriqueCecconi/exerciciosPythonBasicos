linhas=int(input())
colunas=int(input())
matriz=[]

for i in range(linhas):
    linha=[]
    for j in range (colunas):
        num=int(input())
        linha.append(num)
    matriz.append(linha)

multiplos_de_10 = True
for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j]%10 != 0:
            multiplos_de_10 = False

ordenadas = True
for i in range(linhas):
    if (matriz[i][0] < matriz[i][1]):
        for j in range(colunas):
            if (matriz[i][j] < matriz[i][j-1]) and (not(i==0 or j==0)):
                ordenadas = False
    elif (matriz[i][0] > matriz[i][1]):
        for j in range(colunas):
            if (matriz[i][j] > matriz[i][j-1]) and (not(i==0 or j==0)):
                ordenadas = False


if multiplos_de_10 and ordenadas:
    print("SIM")
else:
    print("NAO")

        