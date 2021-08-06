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
if multiplos_de_10==linhas*colunas:
    print("SIM")
else:
    print("NAO")

        