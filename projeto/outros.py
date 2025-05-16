from os import system

def aprendizado():
      print("Como você prefere aprender algo novo?")
      print("[1] Na prática, colocando a mão na massa")
      print("[2] Estudando teorias e entendendo o contexto\n")

      opc = input('Qual a sua opção? [1] ou [2]: ').strip()
      while opc not in ['1', '2']:
            print('Por favor selecione um valor válido.')
            opc = input('Qual a sua opção? [1] ou [2]: ').strip()

      print('\n')

      if opc == '1':
            return 'Prefere aprender na prática'
      elif opc == '2':
            return 'Prefere aprender com teorias e contexto'
      
def motivacao():
      print("O que mais te motiva a trabalhar?")
      print("[1] Ganhar dinheiro")
      print("[2] Ajudar pessoas")
      print("[3] Ter reconhecimento dos outros")
      print("[4] Criar coisas novas")
      print("[5] Fazer descobertas\n")

      opc = input('Qual a sua opção? [1], [2], [3], [4], [5]: ').strip()
      while opc not in ['1', '2', '3', '4', '5']:
            print('Por favor selecione um valor válido.')
            opc = input('Qual a sua opção? [1], [2], [3], [4], [5]: ').strip()

      print('\n')

      if opc == '1':
            return 'Trabalha por dinheiro, quer crescer financeiramente'
      elif opc == '2':
            return 'Trabalha para ajudar as pessoas, quer ter impacto social'
      elif opc == '3':
            return 'Trabalha para ter reconhecimento, quer ser respeitado'
      elif opc == '4':
            return 'Trabalha com a missão de inovar, quer criar novas coisas'
      elif opc == '5':
            return 'Trabalha a fim das descobertas, quer entender sobre a realidade'

def volatilidade():
      print('Que tipo de trabalho é melhor pra você?')
      print('[1] Trabalhos estáveis, onde cada dia é previsivel')
      print('[2] Trabalhos dinamicos, todo dia é um novo desafio\n')

      opc = input('Qual a sua opção? [1] ou [2]: ').strip()
      while opc not in ['1', '2']:
            print('Por favor selecione um valor válido.')
            opc = input('Qual a sua opção? [1] ou [2]: ').strip()
      
      print('\n')

      if opc == '1':
            return 'Gosta de trabalhar com ambientes previsiveis e estáveis'
      elif opc == '2':
            return 'Gosta de trabalhar com ambientes dinamicos e que mudam'
      
def atividade():
      print('Quais atividades você prefere executar?')
      print('[1] Atividades criativas, que exigem reflexão e originalidade')
      print('[2] Atividades técnicas, com processos claros e estruturados\n')

      opc = input('Qual a sua opção? [1] ou [2]: ').strip()
      while opc not in ['1', '2']:
            print('Por favor selecione um valor válido.')
            opc = input('Qual a sua opção? [1] ou [2]: ').strip()
      
      print('\n')      

      if opc == '1':
        return "Prefere atividades criativas e analíticas"
      elif opc == '2':
        return "Prefere atividades técnicas e estruturadas"

def preferencia_social():
      print('Qual a sua preferência social no trabalho? ')
      print('[1] Um lugar com muitas pessoas, uma equipe talvez')
      print('[2] Gosto de trabalhar sozinho e por minha autonomia\n')

      opc = input('Qual a sua opção? [1] ou [2]: ').strip()
      while opc not in ['1', '2']:
            print('Por favor selecione um valor válido.')
            opc = input('Qual a sua opção? [1] ou [2]: ').strip()

      print('\n')

      if opc == '1':
        return "Prefere um lugar colaborativo com equipes"
      elif opc == '2':
        return "Prefere um lugar solitário, com autonomia"

def ambiente():
      print('Qual ambiente de trabalho você acredita que combina mais com você?')
      print('[1] Em um escritório, com estrutura organizada e foco total nas tarefas')
      print('[2] Em casa, com conforto, flexibilidade e autonomia para gerenciar meu tempo')
      print('[3] Ao ar livre, em contato direto com ambientes naturais, pessoas ou objetos físicos')

      opc = input('Qual a sua opção? [1], [2] ou [3]: ').strip()
      while opc not in ['1', '2', '3']:
            print('Por favor selecione um valor válido.')
            opc = input('Qual a sua opção? [1], [2] ou [3]: ').strip()

      if opc == '1':
            return 'Prefere ambientes organizados e profissionais, como escritórios'
      elif opc == '2':
            return 'Prefere trabalhar remotamente, com conforto e autonomia'
      elif opc == '3':
            return 'Prefere estar em movimento, em contato direto com o mundo físico'


def quiz():
      perfil = {
            'estilo_de_aprendizado' : '',
            'motivacao' : '',
            'tipo_de_volatidade': '',
            'tipo_de_atividade': '',
            'preferencia_social': '',
            'ambiente_trabalho': ''
            }
            
      perfil['estilo_de_aprendizado'] = aprendizado()
      system('cls')
      perfil['motivacao'] = motivacao()
      system('cls')
      perfil['tipo_de_volatilidade'] = volatilidade()
      system('cls')
      perfil['tipo_de_atividade'] = atividade()
      system('cls')
      perfil['preferencia_social'] = preferencia_social()
      system('cls')
      perfil['ambiente_trabalho'] = ambiente()
      system('cls')

      descricao_perfil = f"""
Perfil do usuário:
- Estilo de aprendizado: {perfil['estilo_de_aprendizado']}.
- Motivação principal: {perfil['motivacao']}.
- Preferência por estabilidade ou mudanças: {perfil['tipo_de_volatilidade']}.
- Tipo de atividade preferida: {perfil['tipo_de_atividade']}.
- Preferência social: {perfil['preferencia_social']}.
- Ambiente de trabalho ideal: {perfil['ambiente_trabalho']}.
    """

      return descricao_perfil

      