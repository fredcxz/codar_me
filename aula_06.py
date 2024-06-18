#Operadores Lógicos
# not
# and
# or

#Usando (not)
idade = 16
maior_de_idade = idade >= 18
menor_de_idade = not maior_de_idade
 
print("Idade da pessoa:", idade)
print("Maior de idade:", maior_de_idade)
print("Menor de idade:", menor_de_idade)

#Usando (and)
usuário_correto = True
senha_correta = True
login = usuário_correto and senha_correta
print("Login correto:", login)

#Usando (or)
com_atestado = True
com_identidade = False
consulta = com_atestado or com_identidade
print("Pode ir a consulta:", consulta)

