mRNA=list(input())
oligo=list(input())

for i in range(len(oligo)):
    if oligo[i]=="A":
        oligo[i]="U"
    elif oligo[i]=="U":
        oligo[i]="A"
    elif oligo[i]=="C":
        oligo[i]="G"
    else:
        oligo[i]="C"
        
tam = len(oligo) - 1
oligo_invertido = []
while (tam >= 0):
  oligo_invertido.append(oligo[tam])
  tam = tam - 1
print(oligo_invertido)

flag = False
for i in range(len(mRNA)):
    if mRNA[i:(i + len(oligo_invertido))] == oligo_invertido and not(flag):
        posicao = i
        flag = True

if flag == True:
    print("Silenciado em " + str(posicao))
else:
    print("Não silenciado")