characters = []

for i in range(1,4):
    name = input()
    attack = int(input())
    defense = int(input())

    characters.append([name, (attack, defense)])

highAttack=0
highdefense=0

#Código para mostrar todos os dados do characters 1 por linha, mas depois o professor explicou que apenas queria que fossem imprimidos o array com um tuplo e o ataque e defesa maior
for i in range(3):
    for j in range(2):
        if(j==1):
            for k in range(2):
                #print(characters[i][j][k])
                valor = characters[i][j][k] #Guarda os valores do ataque e defesa para depois serem comparados
                if(k==0 and highAttack<valor):#Verifica se o valor do ataque é o maior se for guarda o valor e o nome do jogador
                    highAttack=characters[i][j][k]
                    nameAttack=characters[i][0]
                if(k==1 and highdefense<valor):#Verifica se o valor da defesa é o maior se for guarda o valor e o nome do jogador
                    highdefense=characters[i][j][k]
                    nameDefense=characters[i][0]

        #else:
           #print(characters[i][j])

print(characters)

print("Ataque "+str(nameAttack)+" "+str(highAttack))
print("Defesa "+str(nameDefense)+" "+str(highdefense))
