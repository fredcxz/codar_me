#Listas

notas = [7.5,9,7,5]
         #0 #1 #2

notas.append(8)#Adicionar elementos ao final da lsita

print(notas)
notas.sort()#Ordena a lista
#notas.sort(reverse=True) #-> Reverte a ordenação da lista
print(notas)

x = notas.pop()#-> remove o ultimo elemento da lista
print(notas)
print("x",x)

notas.insert(0,8)#-> Escolhe a posição pra inseri um elemento
print("Após a inserção")
print(notas)






