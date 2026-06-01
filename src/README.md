# Lume - Mentor Financeiro Educativo 🤖💰

O **Lume** é um assistente virtual e educador financeiro desenvolvido com **Streamlit** e **Ollama (Llama 3)**. O objetivo do app é atuar como um mentor consultivo e empático, desmistificando o universo das finanças pessoais e investimentos sem o uso de jargões complexos ("financês"). 

O modelo consome dados locais estruturados (perfil, transações e histórico) para gerar respostas personalizadas e contextuais para o usuário, respeitando regras rígidas de compliance e anti-alucinação.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **Streamlit**: Para a interface de chat responsiva.
* **Ollama (Modelo `llama3`)**: Para processamento de linguagem natural local.
* **Pandas**: Para manipulação e formatação dos dados de transações e histórico.

---

## Estrutura 

```
src/
├── app.py              # Aplicação principal (Streamlit/Gradio)
├── agente.py           # Lógica do agente
├── config.py           # Configurações (API keys, etc.)
└── requirements.txt    # Dependências
```

## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

#Abra o primeiro terminal e baixe o modelo Llama 3
ollama pull llama3

#Inicie o servidor local do Ollama (este terminal deve permanecer aberto durante todo o uso do app):
ollama serve

# Rodar a aplicação
streamlit run app.py
```
