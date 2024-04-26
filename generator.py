import sys
import google.generativeai as genai
from key import key

genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-pro')


def g(comando):
  final=model.generate_content(comando)
  print(final.text)


def perguntas():
    nome=input('Entre o nome do personagem ')
    idade=input('Entre a idade do personagem: ')
    personalidade=input('Entre a personalidad do personagem: ')
    história=('Entre o tipo de história de fundo seu personagem terá: ')


    global comando
    comando=(f'Crie um personagem o mais bem feito possível, que tenha o nome {nome}, tenda {idade} anos, uma personalidade {personalidade}. Escreva para ele uma história de fundo que seja {história}')
    return comando


perguntas()
g(comando)