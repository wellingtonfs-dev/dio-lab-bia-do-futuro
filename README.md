# 🤖 Agente Financeiro Inteligente com IA Generativa

# Lume — Educador Financeiro com IA 💡

> Agente de educação financeira pessoal, empático e anti-alucinação, desenvolvido como solução para o lab **Bia do Futuro** da [DIO](https://www.dio.me/).

---

## O que é o Lume?

O Lume é um mentor financeiro inteligente que desmistifica finanças pessoais sem usar "financês". Ele analisa o perfil e as transações do usuário para responder dúvidas de forma contextualizada, educativa e sem recomendar ativos específicos — priorizando sempre a autonomia financeira de quem o usa.

---

## Arquitetura

```
Cliente → Streamlit (app.py) → Agente (agente.py) → Ollama / LLM local
                                       ↑
                               Contexto injetado via config.py
                               (perfil, transações, histórico, produtos)
```

| Componente | Tecnologia |
|---|---|
| Interface | Streamlit |
| LLM | Ollama (`llama3`) rodando localmente |
| Base de conhecimento | JSON e CSV na pasta `data/` |
| Orquestração | Python (`requests`, `pandas`) |

---

## Estrutura do Projeto

```
.
├── src/
│   ├── agente.py        # System prompt do Lume + chamada ao Ollama
│   ├── app.py           # Interface Streamlit
│   ├── config.py        # Carrega dados e monta contexto para o prompt
│   └── requirements.txt
├── data/
│   ├── perfil_investidor.json       # Perfil e metas do cliente
│   ├── produtos_financeiros.json    # Catálogo de produtos disponíveis
│   ├── transacoes.csv               # Histórico de gastos
│   └── historico_atendimento.csv    # Atendimentos anteriores
└── docs/
    ├── 01-documentacao-agente.md    # Persona, arquitetura e segurança
    ├── 02-base-conhecimento.md      # Estratégia de injeção de contexto
    ├── 03-prompts.md                # System prompt e edge cases
    ├── 04-metricas.md               # Cenários de teste e resultados
    └── 05-pitch.md                  # Roteiro de apresentação
```

---

## Como executar

**Pré-requisitos:** Python 3.14+, [Ollama](https://ollama.com) instalado e rodando.

```bash
# 1. Instale o modelo local
ollama pull llama3

# 2. Clone o repositório e instale as dependências
pip install -r src/requirements.txt

# 3. Execute a aplicação
streamlit run src/app.py
```

Acesse `http://localhost:8501` no navegador.

---

## Comportamento do Agente

- Responde **apenas com base nos dados fornecidos** em `data/` — nunca alucina
- **Não faz recomendações** de ativos específicos (ações, tickers, fundos)
- Admite quando não sabe e redireciona para o conceito correto
- **Dados 100% locais** — nenhuma informação sai da máquina do usuário

---

## Documentação

A pasta `docs/` contém toda a documentação do projeto: definição de persona, estratégia de prompts, base de conhecimento, métricas de avaliação e pitch de apresentação.

---

## Lab

Desenvolvido como solução para o **Lab Bia do Futuro** — [Digital Innovation One (DIO)](https://www.dio.me/).