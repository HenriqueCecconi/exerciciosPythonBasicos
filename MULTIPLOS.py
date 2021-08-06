linhas=int(input())
colunas=int(input())
matriz=[]

for i in range(linhas):
    linha=[]
    for j in range (colunas):
        num=int(input())
        linha.append(num)
    matriz.append(linha)

multiplos_de_10=0
for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j]%10==0:
            multiplos_de_10=multiplos_de_10+1

ordenadas = True
for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] < matriz[i][j-1]:
            ordenadas = False


if multiplos_de_10==linhas*colunas and ordenadas:
    print("SIM")
else:
    print("NAO")

        