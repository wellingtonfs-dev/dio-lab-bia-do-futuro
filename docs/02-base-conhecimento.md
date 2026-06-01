# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |


---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

No primeiro momento eu não modifiquei os dados

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para a versão atual do projeto (MVP), adotamos a estratégia de Injeção de Contexto Estático via Prompt Stuffing. O fluxo funciona da seguinte forma:

System Prompt (Fixo): Define as regras de negócio, a persona (Lume), as diretrizes anti-alucinação e os limites de segurança.

Contexto Base (Injetado): Antes de enviar a pergunta do usuário para o Ollama, o script em Python lê os arquivos CSV/JSON da pasta data/, converte essa base de conhecimento em texto (Markdown ou String estruturada) e a anexa diretamente no corpo da requisição.

User Prompt (Dinâmico): A pergunta real do cliente é concatenada logo após esse bloco de dados.

O prompt final estruturado que o LLM recebe se parece com isto:

```
[SYSTEM]: Você é o Lume, um assistente financeiro... 
[Regras de Comportamento]
[CONTEXTO]: Use apenas as seguintes informações para responder: 
---------------------------------------------
Regra 50/30/20: 50% necessidades, 30% desejos, 20% poupança.
CDB: Título de renda fixa privado emitido por bancos...
---------------------------------------------
[USER]: O que significa a regra dos 50/30/20 que você mencionou? 
``` 
---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
