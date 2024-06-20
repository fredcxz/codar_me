#Condicionais
idade = input(print("Insira uma idade :"))
idade = int(idade)

if idade < 18:
    print("Menor de idade")

elif idade > 60:
    print("Idoso")

else:
    print ("Adulto")
