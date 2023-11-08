# python aula1/numero_aleatorio.py
import random

# Faz com que os números sejam gerados sempre iguais a cada execução
random.seed(42)
print('Calcula número aleatório\n')

#gera número maior que zero e menor que 1
print(random.random())

#gera número maior que 1 e menor que 5
print(random.randint(1, 5))