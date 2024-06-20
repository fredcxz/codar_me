#Dicionarios

# {key,value}
#Exemplol:
alice = {
    "nome" : "Alice",
    "endereço": {
        "rua": "Trinta e sete",
        "bairro": "Ipem",
        "casa": "02"
    }
}
print(alice["nome"])
print(alice["endereço"])
print(alice["endereço"],["rua"])