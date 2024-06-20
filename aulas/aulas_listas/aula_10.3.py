#Exemplo de notas com média

notas = [8,8,6.5]

quantidade = len(notas)
i = 0
total = 0
while i < quantidade:
    total = total + notas[i]
    i = i + 1

print("O total das notas é:\n", total)

media = total / quantidade
print("A média das notas é:\n", media)