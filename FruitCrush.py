linhas, colunas, jogadaLinha, jogadaColuna = input().split()

linhas = int(linhas)
colunas = int(colunas)
jogadaLinha = int(jogadaLinha) - 1
jogadaColuna  = int(jogadaColuna) - 1
matriz = []
score = 1
aux = 1

for i in range(linhas):
    linha = input().split()
    matriz.append(linha)

fruta = matriz[jogadaLinha][jogadaColuna]

while (jogadaColuna + aux) < colunas:
    if matriz[jogadaLinha][jogadaColuna + aux] == fruta:
        matriz[jogadaLinha][jogadaColuna + aux] = "X"
        score += 1
        aux += 1
    else:
        aux = 100
aux = 1

while (jogadaLinha + aux) < linhas:
    if matriz[jogadaLinha + aux][jogadaColuna] == fruta:
        matriz[jogadaLinha + aux][jogadaColuna] = "X"
        score += 1
        aux += 1
    else:
        aux = 100
aux = 1

while (jogadaColuna - aux) >= 0:
    if matriz[jogadaLinha][jogadaColuna - aux] == fruta:
        matriz[jogadaLinha][jogadaColuna - aux] = "X"
        score += 1
        aux += 1
    else:
        aux = 100
aux = 1

while (jogadaLinha - aux) >= 0:
    if matriz[jogadaLinha - aux][jogadaColuna] == fruta:
        matriz[jogadaLinha - aux][jogadaColuna] = "X"
        score += 1
        aux += 1
    else:
        aux = 100
score = score*score
matriz[jogadaLinha][jogadaColuna] = "X"

print("=" * colunas)
print("Score: " + str(score))
print("=" * colunas)
for i in range(linhas):
    linha=""
    for j in range(colunas):
        linha = linha + str(matriz[i][j])
    print(linha)
print("=" * colunas)