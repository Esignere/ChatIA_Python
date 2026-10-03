# 🤖 Chat com Gemini

Um chatbot desenvolvido em **Python** utilizando **Streamlit** para a interface e a **API do Google Gemini** para geração das respostas.

## 🚀 Tecnologias utilizadas

* Python
* Streamlit
* Google Gemini API
* OpenAI Python SDK
* python-dotenv

## 📌 Funcionalidades

* Conversação com inteligência artificial
* Histórico das mensagens durante a sessão
* Interface web desenvolvida com Streamlit
* Integração com a API do Google Gemini
* API key protegida através de variável de ambiente

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
cd NOME_DO_PROJETO
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual.

**Windows:**

```bash
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a API key

Crie um arquivo chamado `.env` na raiz do projeto:

```env
GEMINI_API_KEY=sua_api_key_aqui
```

A API key não deve ser adicionada ao GitHub. O arquivo `.env` já está incluído no `.gitignore`.

### 5. Execute o projeto

```bash
streamlit run App.py
```

O Streamlit abrirá o aplicativo no navegador.

## 🔐 Segurança

A API key é armazenada em uma variável de ambiente e não é incluída no repositório.

Para executar o projeto, cada usuário deve criar sua própria API key e configurar o arquivo `.env`.

## 📚 Objetivo

Este projeto foi desenvolvido como parte dos meus estudos em **Sistemas de Informação**, com o objetivo de praticar:

* Consumo de APIs
* Integração com modelos de inteligência artificial
* Variáveis de ambiente
* Desenvolvimento de aplicações web com Python
* Gerenciamento de dependências
* Versionamento com Git e GitHub
