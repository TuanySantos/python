# python aula1/funcoes.py

#Criar função
def soma():
    print('oi')

soma()    


# Soma com argumentos
def soma_com_argumentos(a, b):
    print(a + b)

soma_com_argumentos(2, 8)

# Soma com argumentos e retorno
def soma_argumentos_retorno(a, b):
    return a + b

resposta = soma_argumentos_retorno(3, 8)

print(resposta)


