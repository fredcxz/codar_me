#Loops

#                                       Sistema de Compras
continuar = "t" 
total = 0
while continuar == "t":
    valor = int(input("Digite o valor da sua compra:\n"))
    total = total + valor
    continuar = input("Deseja continuar? (t/f)")

print("Valor total da compra:\n", total)