from os import system
from time import sleep
from usar_gemini import gerar_roadmap

system('cls')
print('Bem vindo(a) ao Mapa de carreiras!')
print('Descubra como se tornar um profissional em qualquer campo..')

print("""
[1] Escolher profissão específica 
[2] Descubra profissões que mais combinam com você com base no seu perfil
""")

opc = input('Qual a sua opção? [1] ou [2]: ')
while opc not in '12':
      print('Por favor selecione um valor válido.')
      opc = input('Qual a sua opção? [1] ou [2]: ')

if opc == '1':
      system('cls')
      print('Voce escolheu uma profissão específica.')
      print('O sistema irá criar um roadmap de como alcança-la.')
      profissao = input('Digite qual é a profissão: ')

      gerar_roadmap(profissao=profissao)

elif opc == '2':
      pass