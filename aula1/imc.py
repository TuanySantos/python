# python aula1/imc.py

print('IMC\n')

#peso / altura * altura

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc = round(peso/(altura**2), 2)

print(f'\nO IMC é: {imc}')
