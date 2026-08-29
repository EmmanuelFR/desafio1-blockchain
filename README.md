# Desafio 1 — Blockchain Educacional

Aplicação acadêmica desenvolvida em Python 3 e Streamlit para demonstrar os
conceitos básicos de blocos, hashes, encadeamento e validação de integridade.

## Versão atual

A versão 0.1 contém:

- criação automática do bloco gênese;
- cálculo de hash com SHA-256;
- ligação de um bloco ao hash do anterior;
- validação da integridade da cadeia;
- interface mínima em Streamlit;
- testes automatizados da lógica principal.

Usuários, saldos, transações e simulação visual de adulteração serão incluídos
nas próximas etapas.

## Estrutura

```text
desafio1-blockchain/
├── app.py
├── blockchain.py
├── requirements.txt
├── README.md
├── docs/
│   ├── relatorio_tecnico.md
│   └── Relatorio_Tecnico_Desafio_1.docx
└── tests/
    └── test_blockchain.py
```

## Como executar no Windows 11

No terminal do VS Code, dentro da pasta do projeto:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

O navegador abrirá a aplicação em `http://localhost:8501`.

Para encerrar o servidor, volte ao terminal e pressione `Ctrl+C`.

## Como executar os testes

```powershell
python -m pytest -v
```
