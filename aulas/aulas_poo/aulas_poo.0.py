#Programção orientada a objetos

'''Objetos funciona da seguinte forma em python: se eu defino um valor a 'x' e depois faço 
x = y o objeto de referencio na memória vai ser o mesmo logo se eu fizer x == y será 'True' 
ou verdade, mas se eu coloco x = x +1 eu vou ter outro objeto ligado a x ou seja a parti
 dai x == y 'False' ou falso'''

#Exemplo
x = 5
print(id(x))

y = x
print(id(y))

print(x == y)

x = x + 2
print(id(x))

print(x == y)
