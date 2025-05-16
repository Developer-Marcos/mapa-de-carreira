from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Defina GEMINI_API_KEY no seu .env")
    exit(1)

genai.configure(api_key=api_key)

modelo = genai.GenerativeModel(model_name='gemini-2.0-flash')

def gerar_roadmap(profissao: str):
      prompt = f"Você é um mentor experiente e direto ao ponto. Sua missão é ajudar pessoas a alcançarem seus objetivos profissionais com clareza e eficiência, sem termos muito técnicos. Crie um roadmap resumido e direto para a carreira de {profissao}. Liste os passos principais em tópicos claros e objetivos começando do item 1, sem explicações longas. Faça esse roadmap em formato de lista onde, sem comentarios e caracteres ou simbolos desnecessarios. Seja organizado. No final da lista, fale algumas dicas extras se possível."

      roadmap = modelo.generate_content(prompt)

      os.system('cls')
      print(f'Roadmap para se tornar {profissao}: \n')
      print(roadmap.text)


def definir_profissoes(perfil):
     buscar_profissoes = f"""Por favor, responda sem usar nenhuma formatação Markdown (como * por exemplo), como asteriscos, negrito ou itálico.
Descubra 3 profissões que mais se encaixam com o seguinte perfil, apenas traga o nome delas em tópicos e fale o porque de cada uma. Seja organizado, sem comentarios e caracteres ou simbolos desnecessarios e resuma em até 2 linhas, com o nome em cima e as caracteristicas em baixo, separe-os com '-' ao pular a linha para a profissão seguinte: 
     {perfil}
     """
     profissoes = modelo.generate_content(buscar_profissoes)
     
     os.system('cls')
     print('Aqui está 3 profissões que mais combinam com o seu perfil:')
     print(profissoes.text)

