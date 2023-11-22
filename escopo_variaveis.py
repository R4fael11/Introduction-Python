"""escopo de variaveis"""

""""

as variaveis globais
as variaveis locais

"""

x = 5

def funcao():
    x = 3 
    print("O valor de x na variavel local é: ", x)
    
funcao()
print("O valor de x na variavel global é: ", x)

