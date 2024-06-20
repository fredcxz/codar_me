#Funções 02
def calcular_conta(consumo, taxa_servico, desconto_fidelidade):
    if taxa_servico == 0 and desconto_fidelidade == 0:
        return consumo
    servico = consumo * taxa_servico
    desconto = consumo * desconto_fidelidade
    valor = consumo + servico
    valor = valor - desconto

    print("O valor a ser pago é:", valor)
calcular_conta(consumo=600, taxa_servico=0.1, desconto_fidelidade=0.5)

'''
consumo = 100
servico = consumo * taxa_servico # 10 
desconto = consumo * desconto_fidelidade # 5

valor = consumo + servico # 100 + 10 =110
valor = valor - desconto # 110 - 5
=> 105
'''