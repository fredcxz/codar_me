#Connjuntos
usuarios = {"fred", "thiago"}
usuarios2 = set(["Christian","Giulio"])

##e_igual = usuarios.union(usuarios2) == usuarios2 | usuarios
##print(e_igual)

##e_igual = usuarios.intersection(usuarios2) == usuarios2 & usuarios
##print(e_igual)

e_igual = usuarios.difference(usuarios2) == usuarios - usuarios2
print(e_igual)