# Desafio 1 — Blockchain Educacional

Aplicação acadêmica desenvolvida em Python e Streamlit para demonstrar, de
forma prática, a estrutura básica de uma blockchain, o registro de transações
e a detecção de alterações em blocos já encadeados.

O projeto utiliza uma moeda fictícia chamada **EDU**, criada exclusivamente
para representar transferências entre carteiras educacionais. Ela não possui
valor financeiro real e não representa uma criptomoeda comercial.

## Objetivos

O projeto permite compreender os seguintes conceitos:

- criação de blocos;
- geração de hashes com SHA-256;
- ligação de cada bloco ao hash do bloco anterior;
- criação automática do bloco gênese;
- validação da integridade da cadeia;
- carteiras e saldos educacionais;
- validação e realização de transações;
- registro de transações em novos blocos;
- detecção de adulteração no conteúdo de um bloco;
- persistência temporária do estado durante a sessão do Streamlit.

## Funcionalidades

### Blockchain e integridade

- criação automática do bloco gênese;
- registro interno de data e hora em UTC;
- conversão da data e hora para o horário de Brasília na interface;
- cálculo determinístico do hash de cada bloco;
- encadeamento por meio do campo `hash_anterior`;
- validação dos hashes armazenados;
- validação das ligações entre blocos;
- identificação do bloco cujo conteúdo foi alterado.

### Carteiras e transações

A aplicação inicia com duas carteiras:

| Identificador | Usuário | Saldo inicial |
|---|---|---:|
| `CARTEIRA-001` | Emmanuel Freitas | 100 EDU |
| `CARTEIRA-002` | Weberson Rodrigues | 100 EDU |

Antes de realizar uma transferência, a aplicação verifica:

- existência da carteira de origem;
- existência da carteira de destino;
- diferença entre origem e destino;
- valor maior que zero;
- saldo suficiente na carteira de origem;
- integridade da cadeia antes do registro de uma nova operação.

Uma transação válida atualiza os saldos e cria um novo bloco com os dados da
operação.

Uma transação recusada não altera os saldos e não modifica a cadeia.
Quando a cadeia está inválida, novas transações são bloqueadas até que a
demonstração seja reiniciada.

### Demonstração de adulteração

Depois da criação de um bloco de transação, a interface permite alterar
intencionalmente o valor registrado nesse bloco sem recalcular seu hash.

Na validação seguinte, o conteúdo atual produz um hash diferente daquele
armazenado originalmente. A cadeia passa a ser apresentada como inválida,
demonstrando o princípio de integridade dos registros encadeados.

A adulteração modifica somente o dado registrado no bloco selecionado. Os
saldos das carteiras permanecem inalterados, pois a operação tem finalidade
exclusivamente demonstrativa.

### Reinício da demonstração

O botão **Reiniciar demonstração** cria uma nova instância da blockchain e
restaura o estado inicial:

- um bloco gênese;
- 100 EDU em cada carteira;
- cadeia válida;
- nenhuma transação registrada.

## Tecnologias utilizadas

- Python 3.12;
- Streamlit;
- CSS para personalização visual da interface;
- pytest;
- SHA-256 por meio do módulo `hashlib`;
- Git e GitHub para controle de versão.

## Estrutura do projeto

```text
desafio1-blockchain/
├── .gitignore
├── .streamlit/
│   ├── config.toml
│   └── styles.css
├── app.py
├── blockchain.py
├── requirements.txt
├── README.md
├── docs/
│   ├── Relatorio_Tecnico_Desafio_1.docx
│   ├── Relatorio_Tecnico_Desafio_1_V2.docx
│   ├── Relatorio_Tecnico_Desafio_1_V3.docx
│   ├── relatorio_tecnico.md
│   ├── relatorio_tecnico_v2.md
│   └── relatorio_tecnico_v3.md
└── tests/
    └── test_blockchain.py
```

### Responsabilidade dos arquivos

- `blockchain.py`: contém as classes, regras de negócio, operações e validações;
- `app.py`: contém a interface e o gerenciamento da sessão no Streamlit;
- `tests/test_blockchain.py`: contém os testes automatizados;
- `requirements.txt`: registra as dependências do projeto;
- `docs/`: reúne as versões da documentação técnica;
- `.streamlit/config.toml`: define o tema e a paleta de cores da aplicação;
- `.streamlit/styles.css`: centraliza os estilos visuais da interface;
- `.gitignore`: impede o versionamento de arquivos locais e temporários.

## Preparação do ambiente no Windows 11

No terminal do VS Code, dentro da pasta do projeto, crie o ambiente virtual:

```powershell
python -m venv .venv
```

Ative o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

## Execução da aplicação

Com o ambiente virtual ativado, execute:

```powershell
python -m streamlit run app.py
```

O Streamlit apresentará o endereço local da aplicação, normalmente:

```text
http://localhost:8501
```

Para encerrar o servidor, volte ao terminal e pressione `Ctrl+C`.

Para sair do ambiente virtual:

```powershell
deactivate
```

## Roteiro básico de utilização

1. Execute a aplicação.
2. Escolha as carteiras de origem e destino.
3. Informe um valor válido.
4. Pressione **Realizar transação**.
5. Confira os saldos e o novo bloco.
6. Na demonstração de adulteração, selecione um bloco de transação.
7. Informe um valor diferente do originalmente registrado.
8. Pressione **Simular adulteração**.
9. Observe que a cadeia passa a ser considerada inválida.
10. Tente realizar uma nova transação e observe que a operação é bloqueada.
11. Pressione **Reiniciar demonstração** para restaurar o estado inicial.

## Testes automatizados

Execute:

```powershell
python -m pytest -v
```

O projeto possui **21 testes automatizados**, que verificam:

- criação do bloco gênese;
- criação e encadeamento de novos blocos;
- validação de uma cadeia íntegra;
- detecção de alteração em um bloco;
- detecção de ligações inválidas entre blocos;
- criação das carteiras iniciais;
- regras de validação das transações;
- atualização dos saldos;
- criação do bloco de transação;
- ausência de efeitos colaterais em operações recusadas;
- transferências nos dois sentidos;
- conservação do saldo total;
- simulação controlada de adulteração;
- rejeição de tentativas inválidas de adulteração;
- bloqueio de novas transações quando a cadeia está inválida.

Resultado esperado:

```text
21 passed
```

## Limitações e finalidade acadêmica

Esta implementação possui finalidade exclusivamente educacional. Ela não
reproduz todos os componentes de uma blockchain pública ou de uma solução
financeira real.

O projeto não possui:

- rede distribuída entre diferentes nós;
- mecanismo de consenso;
- mineração;
- assinatura digital das transações;
- autenticação de usuários;
- armazenamento permanente em banco de dados;
- criptomoeda com valor financeiro real.

A cadeia e os saldos são mantidos somente na memória durante a sessão da
aplicação.

## Documentação técnica

A pasta `docs` reúne as versões V1, V2 e V3 do relatório técnico em Markdown
e Word. A V3 documenta a evolução do projeto até a implementação da
demonstração de adulteração e do reinício controlado da aplicação.
