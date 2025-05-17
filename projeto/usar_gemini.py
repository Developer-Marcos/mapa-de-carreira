from dotenv import load_dotenv # biblioteca que permite o python usar a API KEY no .env
import google.generativeai as genai
import os
import re
from outros import limpar_tela


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Defina GEMINI_API_KEY no seu .env")
    exit(1)

genai.configure(api_key=api_key)

modelo = genai.GenerativeModel(model_name='gemini-2.0-flash')

def gerar_roadmap(profissao: str) -> str:
     prompt = f"Você é um mentor experiente e direto ao ponto. Sua missão é ajudar pessoas a alcançarem seus objetivos profissionais com clareza e eficiência, sem termos muito técnicos. Crie um roadmap resumido e direto para a carreira de {profissao}. Liste os passos principais em tópicos claros e objetivos começando do item 1, sem explicações longas. Faça esse roadmap em formato de lista onde, sem comentarios e caracteres ou simbolos desnecessarios. Seja organizado. No final da lista, fale algumas dicas extras se possível."

     try:
          roadmap = modelo.generate_content(prompt)
     except Exception as e:
          print("Erro ao gerar roadmap:", e)
          return

     limpar_tela()

     texto_roadmap = limpar_texto(roadmap.text)

     materiais = f"""Liste materiais úteis (livros, cursos, sites, canais) para aprender sobre a profissão "{profissao}".
Use no máximo 5 linhas. Seja direto, cite os nomes e inclua links se souber. Não explique, só recomende."""
     
     try:
        gerar_materiais = modelo.generate_content(materiais)
     except Exception as e:
        print("Erro ao gerar materiais recomendados:", e)
        return

     texto_materiais = limpar_texto(gerar_materiais.text)

     return f'Roadmap para se tornar {profissao}:\n\n{texto_roadmap}\n\nMateriais recomendados:\n\n{texto_materiais}'

def definir_profissoes(perfil):
     buscar_profissoes = f"""Por favor, responda sem usar nenhuma formatação Markdown (como * por exemplo), como asteriscos, negrito ou itálico.
Descubra 3 profissões que mais se encaixam com o seguinte perfil, apenas traga o nome delas em tópicos e fale o porque de cada uma. Seja organizado, sem comentarios e caracteres ou simbolos desnecessarios e resuma em até 2 linhas, com o nome em cima e as caracteristicas em baixo, separe-os com '-' ao pular a linha para a profissão seguinte e diversifique as areas, por exemplo, se vier alguma de tecnologia, nao recomende outra de tecnologia (programador e engenheiro de software). No final de cada profissão, explique o que ela faz em duas linhas no maximo: 
     {perfil}
     """

     try:
          profissoes = modelo.generate_content(buscar_profissoes)
     except Exception as e:
          print("Erro ao gerar profissões:", e)
          return
     
     limpar_tela()
     print('Aqui está 3 profissões que mais combinam com o seu perfil:')
     print(limpar_texto(profissoes.text))

def limpar_texto(texto):
    return re.sub(r'[*_~`]', '', texto)
