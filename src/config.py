import json
import os
import pandas as pd

# Configurações do Ollama
OLLAMA_URL = 'http://localhost:11434/api/generate'
MODELO = 'llama3'

# Caminhos dos dados (utilizando caminhos relativos robustos)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Carrega os dados uma única vez ao importar o módulo
perfil = json.load(open(os.path.join(DATA_DIR, 'perfil_investidor.json'), encoding='utf-8'))
transacoes = pd.read_csv(os.path.join(DATA_DIR, 'transacoes.csv'))
historico = pd.read_csv(os.path.join(DATA_DIR, 'historico_atendimento.csv'))
produtos = json.load(open(os.path.join(DATA_DIR, 'produtos_financeiros.json'), encoding='utf-8'))

# Monta o bloco de contexto formatado
contexto = f""" 
    CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
    OBJETIVO: {perfil['objetivo_principal']}
    PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

    TRANSAÇÕES RECENTES:
    {transacoes.to_string(index=False)}

    ATENDIMENTOS ANTERIORES:
    {historico.to_string(index=False)}

    PRODUTOS DISPONÍVEIS:
    {json.dumps(produtos, indent=2, ensure_ascii=False)}
"""