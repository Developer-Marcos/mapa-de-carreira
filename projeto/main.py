from os import system
from time import sleep
from usar_gemini import gerar_roadmap, definir_profissoes
from outros import quiz

system('cls')
print('Bem vindo(a) ao Mapa de carreiras!')
print('Descubra como se tornar um profissional em qualquer campo..')

print("""
[1] Escolher profissão específica 
[2] Descubra profissões que mais combinam com você com base no seu perfil
""")

opc = input('Qual a sua opção? [1] ou [2]: ').strip()
while opc not in ['1', '2']:
      print('Por favor selecione um valor válido.')
      opc = input('Qual a sua opção? [1] ou [2]: ').strip()

if opc == '1':
      system('cls')
      print('Voce escolheu uma profissão específica.')
      print('O sistema irá criar um roadmap de como alcança-la.')

      profissao = input('Digite qual é a profissão: ').strip()
      while not profissao:
            print("Insira um valor válido por favor.")
            profissao = input('Digite qual é a profissão: ').strip()    

      gerar_roadmap(profissao=profissao)

elif opc == '2':
      system('cls')
      print('Será feito um quiz para saber 3 profissões que combinam com o seu perfil.\n')
      sleep(2)
      
      perfil = quiz()
      print('Agora as profissões serão definidas, espere um momento por favor\n')
      definir_profissoes(perfil=perfil)
