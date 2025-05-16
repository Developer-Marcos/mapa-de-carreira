from os import system
from time import sleep

system('cls')
print('Bem vindo(a) ao Mapa de carreiras!')
print('Descubra como se tornar um profissional em algum campo específico.')

print("""
[1] Escolher profissão específica 
[2] Descubra profissões que mais combinam com você
""")

opc = input('Qual a sua opção? [1] ou [2]: ')
while opc not in '12':
      print('Por favor selecione um valor válido.')
      opc = input('Qual a sua opção? [1] ou [2]: ')

if opc == 1:
      pass
elif opc == 2:
      pass