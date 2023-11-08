# python aula1/escolha_numero_aleatorio.py
import random
#Escolha um número aleatório
#Entre 1 e 5
#Recebe um chute
print('Jogo da sorte!\n')
numero_escolhido = int(input('Escolha um número aleatório de 1 a 5\n'))
numero_aleatorio = random.randint(1,5)

if(numero_aleatorio == numero_escolhido):
    print('Acertou!!\n')
else:
    print(f'O número secreto é: {numero_aleatorio}\n')    
#Se for igual ao numero aleatorio => acertou
#senao, quase, o número secreto era {numero_secreto}