import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

IA = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

## Essa eh uma chave gratuita do gemini.
IA = OpenAI(api_key=api_key, base_url='https://generativelanguage.googleapis.com/v1beta/openai')

st.write('## ChatBot de IA') # markdown

#memoria do streamlit
if  not 'lista_mensagens'   in  st.session_state:
    st.session_state['lista_mensagens'] = []
    

# Exibir historico de mensagens
for mensagem  in  st.session_state['lista_mensagens']:
    sender =  mensagem['role']
    textMessage = mensagem['content']
    st.chat_message(sender).write(textMessage)

mensagemUsuario = st.chat_input('Escreva sua mensagem aqui')

if mensagemUsuario:
    st.chat_message('user').write(mensagemUsuario)
    userMessage = {'role': 'user', 'content': mensagemUsuario}
    st.session_state['lista_mensagens'].append(userMessage)
    
    # resposta IA
    resposta_modelo = IA.chat.completions.create( messages=st.session_state['lista_mensagens'],model='gemini-flash-lite-latest')
    resposta_ia = resposta_modelo.choices[0].message.content
    
    #Exibir resposta da IA na tela
    st.chat_message('assistant').write(resposta_ia)
    botMessage = {'role': 'assistant', "content": resposta_ia}
    st.session_state['lista_mensagens'].append(botMessage)
    
