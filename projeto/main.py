from os import system
from time import sleep
from usar_gemini import gerar_roadmap, definir_profissoes
from outros import quiz

system('cls')
print('Bem vindo(a) ao Mapa de carreiras!')
print('Descubra como se tornar um profissional em qualquer campo.')

print("""
[1] Escolher profissão específica 
[2] Descubra profissões que mais combinam com você com base no seu perfil
___
[FIM] Digite fim para finalizar o programa em qualquer momento
""")

while True:
      opc = input('Qual a sua opção? [1] ou [2]: ').strip()
      if opc == "fim":
             exit()
      elif opc in ['1', '2']:
            break  
      print('Por favor selecione um valor válido.')


if opc == '1':
      system('cls')
      print('Voce escolheu uma profissão específica.')
      print('O sistema irá criar um roadmap de como alcança-la.')

      while True:
            profissao = input('Digite qual é a profissão: ').strip().lower()
            if profissao == 'fim':
                  exit()
            if profissao:
                  break
            print("Insira um valor válido por favor.")

      print('\nO sistema está criando o roadmap, aguarde por favor.')
      gerar_roadmap(profissao=profissao)

elif opc == '2':
      system('cls')
      print('Será feito um quiz para saber 3 profissões que combinam com o seu perfil.\n')
      sleep(2)
      
      perfil = quiz()
      print('Agora as profissões serão definidas, espere um momento por favor\n')
      definir_profissoes(perfil=perfil)

      print("\n")

      while True:
            profissao = input("Se interessou por alguma? Escreva o nome dela aqui: ").strip().lower()
            if profissao == 'fim':
                  exit()
            if profissao:
                  break
            print("Insira um valor válido por favor.")

      
      gerar_roadmap(profissao=profissao)
