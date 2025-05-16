from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Defina GEMINI_API_KEY no seu .env")
    exit(1)

genai.configure(api_key=api_key)

def gerar_roadmap(profissao: str):
      modelo = genai.GenerativeModel(model_name='gemini-2.0-flash')

      prompt = f"Você é um mentor experiente e direto ao ponto. Sua missão é ajudar pessoas a alcançarem seus objetivos profissionais com clareza e eficiência, sem termos muito técnicos. Crie um roadmap resumido e direto para a carreira de {profissao}. Liste os passos principais em tópicos claros e objetivos, sem explicações longas. faca esse roadmap em formato de lista onde, sem comentarios e carcateres ou simbolos desnecessarios. Seja organizado. No final da lista, fale algumas dicas extras se possível."

      roadmap = modelo.generate_content(prompt)

      os.system('cls')
      print(f'Roadmap para se tornar {profissao}: \n')
      print(roadmap.text)

