**UNIFAA - Centro Universitário de Valença**

Curso de Engenharia de Software

**RELATÓRIO TÉCNICO \| DESAFIO 1**

**Blockchain Educacional**

Estrutura, integridade, carteiras, saldos e transações

**VERSÃO 2 \| DOCUMENTO INTERMEDIÁRIO \| PROJETO v0.2**

| **Curso:**      | Engenharia de Software                                                          |
|-----------------|---------------------------------------------------------------------------------|
| **Disciplina:** | DESRUPT IR SPECIALIST – EXPLORANDO OS NOVOS HORIZONTES DAS TECNOLOGIAS – 2026/2 |
| **Professor:**  | WEBERSON RODRIGUES DE ARAUJO DE OLIVEIRA                                        |
| **Aluno:**      | Emmanuel de Freitas Ribeiro                                                     |
| **RA:**         | E33006                                                                          |
| **Data:**       |                                                                                 |

Valença - RJ

# Resumo executivo

Este relatório apresenta a Versão 2 do Desafio 1, uma aplicação acadêmica que simula os fundamentos de uma blockchain. A solução cria blocos encadeados por hashes SHA-256, verifica a integridade dos registros e, nesta etapa, incorpora duas carteiras educacionais, saldos em uma unidade fictícia chamada EDU e transferências registradas em novos blocos.

O documento corresponde ao estado intermediário do projeto v0.2. Ele consolida a estrutura técnica e as funcionalidades já verificadas, sem antecipar como concluídas as etapas futuras de demonstração visual de adulteração, refinamento final da documentação e preparação do roteiro de apresentação em vídeo.

| **Estado verificado:** 15 testes automatizados aprovados; duas carteiras com 100 EDU iniciais; transações válidas atualizam saldos e criam blocos; transações inválidas não alteram o estado; a cadeia permanece válida após operações nos dois sentidos. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Tabela 1 - Síntese do estado da versão 0.2

| **Dimensão**             | **Resultado atual**                                                | **Situação** |
|--------------------------|--------------------------------------------------------------------|--------------|
| **Estrutura blockchain** | Bloco gênese, SHA-256, encadeamento e verificação de integridade   | Implementado |
| **Carteiras**            | Emmanuel Freitas e Weberson Rodrigues, com 100 EDU cada            | Implementado |
| **Transações**           | Validação, atualização de saldos e registro em novo bloco          | Implementado |
| **Interface**            | Exibição de carteiras, formulário de transação, mensagens e blocos | Implementado |
| **Qualidade**            | 15 testes automatizados aprovados                                  | Verificado   |
| **Próximos ciclos**      | Demonstração de adulteração, relatório final e roteiro de vídeo    | Pendente     |

# Introdução

Blockchain é uma forma de registrar informações em blocos ligados entre si. Cada bloco armazena dados, uma referência criptográfica ao bloco anterior e o próprio hash. Quando os dados de um bloco são alterados, o hash recalculado deixa de coincidir com o valor que havia sido armazenado, permitindo identificar a quebra de integridade. Em sistemas completos, outros mecanismos - como distribuição entre participantes e consenso - ampliam a resistência a adulterações \[1\].

O projeto foi desenvolvido para demonstrar esse encadeamento de maneira acessível. A aplicação é local e centralizada, portanto não pretende reproduzir uma rede pública nem uma criptomoeda real. Seu foco é pedagógico: tornar visíveis a geração de hashes, a relação entre blocos, as regras de uma transferência e os efeitos de uma modificação indevida.

# Objetivo e escopo

O objetivo geral é construir uma aplicação capaz de:

- criar um bloco gênese que inaugura a cadeia;

- adicionar novos blocos com índice, data e hora, dados e hash anterior;

- calcular hashes SHA-256 a partir de uma representação determinística do conteúdo;

- validar hashes armazenados e ligações entre blocos;

- representar carteiras educacionais e seus saldos em EDU;

- validar e realizar transferências entre carteiras;

- registrar cada transação aceita em um novo bloco;

- exibir o estado da aplicação em uma interface Streamlit; e

- verificar o comportamento com testes automatizados.

| **Escopo desta V2:** A versão documenta o núcleo da blockchain e a etapa de usuários, carteiras, saldos e transações. A demonstração visual de adulteração e a consolidação final do projeto ainda serão incorporadas em versões posteriores. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# Tecnologias e decisões de projeto

Tabela 2 - Tecnologias utilizadas

| **Tecnologia**         | **Papel no projeto**                         | **Justificativa**                                        |
|------------------------|----------------------------------------------|----------------------------------------------------------|
| **Python 3.12.10**     | Lógica de blocos, hashes, carteiras e testes | Sintaxe legível e bibliotecas padrão adequadas ao escopo |
| **Streamlit 1.62.0**   | Interface web interativa                     | Permite demonstrar o projeto usando apenas Python        |
| **pytest 9.1.1**       | Testes automatizados                         | Validação objetiva de regras e prevenção de regressões   |
| **Git**                | Controle de versão                           | Histórico incremental e rastreável das mudanças          |
| **Visual Studio Code** | Edição e execução                            | Ambiente integrado para código, terminal e extensões     |

## Justificativa para Python e Streamlit

A adoção de Python 3 e Streamlit foi uma decisão do projeto, e não uma exigência expressa do professor. Python foi escolhido por favorecer clareza de leitura e por disponibilizar, na biblioteca padrão, recursos diretamente úteis para o trabalho: hashlib para SHA-256 \[2\], json para serialização determinística \[3\], dataclasses para a estrutura do bloco \[4\] e datetime para os registros temporais.

Streamlit foi selecionado porque transforma funções Python em uma interface web com pouco código adicional. O framework oferece formulários para agrupar entradas e processá-las em um único envio \[5\], além de Session State para manter objetos entre as reexecuções de uma sessão \[6\]. Isso reduz a complexidade de front-end e concentra o aprendizado nos conceitos de blockchain, validação e testes.

# Arquitetura da solução

A aplicação separa a regra de negócio da apresentação. Essa divisão torna o código mais compreensível, permite testar o núcleo sem abrir a interface e facilita a evolução das próximas etapas.

Tabela 3 - Responsabilidade dos principais arquivos

| **Arquivo**                  | **Responsabilidade**     | **Elementos principais**                                                                      |
|------------------------------|--------------------------|-----------------------------------------------------------------------------------------------|
| **blockchain.py**            | Domínio e regras         | Bloco, Blockchain, hashes, cadeia, carteiras, validação e realização de transações            |
| **app.py**                   | Interface Streamlit      | Session State, indicadores, cartões de saldo, formulário, mensagens e visualização dos blocos |
| **tests/test_blockchain.py** | Verificação automatizada | 15 testes para criação, integridade, regras de transação e conservação de saldos              |
| **docs/**                    | Documentação             | Relatórios técnicos e materiais de apoio                                                      |

## Fluxo de execução

1.  A interface recupera a instância de Blockchain mantida na sessão.

2.  O usuário escolhe as carteiras de origem e destino e informa um valor inteiro em EDU.

3.  O método validar_transacao verifica a existência das carteiras, a diferença entre elas, o valor positivo e o saldo disponível.

4.  Se a operação for rejeitada, a mensagem de erro é devolvida e nenhum saldo ou bloco é alterado.

5.  Se a operação for aceita, os saldos são atualizados e os dados da transferência são enviados a adicionar_bloco.

6.  A interface recalcula a situação da cadeia e apresenta os novos saldos, a quantidade de blocos e o registro criado.

# Implementação da blockchain

## Estrutura do bloco

A classe Bloco é definida como uma dataclass e reúne os campos índice, data e hora, dados, hash anterior e hash. O uso de uma estrutura explícita facilita a inspeção dos registros e reduz a necessidade de código repetitivo para inicialização \[4\].

Para calcular o hash, o projeto reúne os campos que identificam o conteúdo do bloco, serializa os dados em JSON com chaves ordenadas e separadores consistentes, codifica o texto em UTF-8 e aplica SHA-256. O campo hash não participa da entrada, pois ele é o resultado do próprio cálculo.

```python
conteudo = indice + data_hora + dados + hash_anterior
serializado = json.dumps(conteudo, ensure_ascii=False, sort_keys=True)
hash_bloco = hashlib.sha256(serializado.encode("utf-8")).hexdigest()
```

## Bloco gênese e encadeamento

A cadeia começa com o bloco de índice 0. Seu hash anterior recebe o valor textual "0" e seus dados indicam o início da blockchain educacional. Cada novo bloco usa o hash do último bloco como hash_anterior. Assim, a referência registrada no bloco seguinte cria a dependência entre os elementos da cadeia.

## Verificação de integridade

O método validar_cadeia percorre os blocos e realiza duas verificações: recalcula o hash de cada bloco para compará-lo com o valor armazenado e, a partir do segundo bloco, confirma se hash_anterior coincide com o hash do bloco precedente. Se qualquer comparação falhar, a aplicação identifica o índice envolvido e informa que a cadeia é inválida.

| **Interpretação correta:** O projeto detecta inconsistências; ele não impede fisicamente que alguém com acesso ao processo altere os objetos em memória. Em uma blockchain distribuída, cópias independentes, consenso e controles criptográficos adicionais aumentariam a resistência à adulteração \[1\]. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# Carteiras e a moeda fictícia EDU

Tabela 4 - Estado inicial das carteiras educacionais

| **Identificador** | **Usuário**        | **Saldo inicial** |
|-------------------|--------------------|-------------------|
| **CARTEIRA-001**  | Emmanuel Freitas   | 100 EDU           |
| **CARTEIRA-002**  | Weberson Rodrigues | 100 EDU           |

## Justificativa da moeda fictícia

EDU é uma unidade exclusivamente fictícia, sem valor monetário, cotação, conversão, rede de pagamento ou possibilidade de uso financeiro. Sua criação é uma decisão pedagógica do projeto. Ela permite representar, de forma simples e segura, os elementos essenciais de uma transferência - origem, destino, valor, saldo e registro em bloco - sem sugerir que a aplicação emite uma criptomoeda real.

A sigla EDU reforça o caráter educacional. Os valores são inteiros, o que evita discussões paralelas sobre precisão de números de ponto flutuante e mantém o foco na conservação do saldo total. Essa mesma justificativa deverá ser retomada na explicação em vídeo: a moeda existe para tornar o fluxo demonstrável, e não para simular um ativo financeiro completo.

## Saldos iniciais e simplificação adotada

Os saldos iniciais são definidos no estado das carteiras quando a classe Blockchain é criada. Eles não são emitidos pelo bloco gênese. Essa escolha reduz a complexidade nesta versão, porém significa que a cadeia, isoladamente, não contém todos os dados necessários para reconstruir o estado inicial das carteiras. A limitação é documentada e pode orientar uma evolução futura, como registrar a distribuição inicial em um bloco específico.

# Validação e realização de transações

Antes de movimentar qualquer saldo, a aplicação executa todas as regras de validação. Essa ordem evita estados parciais: uma transação rejeitada termina antes de qualquer modificação nas carteiras ou na cadeia.

Tabela 5 - Regras de validação de uma transação

| **Regra**                | **Condição de rejeição**          | **Mensagem**                                           |
|--------------------------|-----------------------------------|--------------------------------------------------------|
| **Origem existente**     | Identificador não localizado      | Carteira de origem não encontrada.                     |
| **Destino existente**    | Identificador não localizado      | Carteira de destino não encontrada.                    |
| **Carteiras diferentes** | Origem igual ao destino           | As carteiras de origem e destino devem ser diferentes. |
| **Valor positivo**       | Valor menor ou igual a zero       | O valor da transação deve ser maior que zero.          |
| **Saldo suficiente**     | Saldo da origem menor que o valor | Saldo insuficiente.                                    |

## Registro da transferência

Quando todas as regras são satisfeitas, o método realizar_transacao debita a carteira de origem, credita a carteira de destino e cria um dicionário com os dados abaixo. Em seguida, esse conjunto é registrado em um novo bloco encadeado.

Tabela 6 - Dados gravados no bloco de transação

| **Campo**            | **Descrição**                        |
|----------------------|--------------------------------------|
| **tipo**             | Identifica o registro como transação |
| **carteira_origem**  | Identificador da carteira debitada   |
| **usuario_origem**   | Nome associado à carteira de origem  |
| **carteira_destino** | Identificador da carteira creditada  |
| **usuario_destino**  | Nome associado à carteira de destino |
| **valor**            | Quantidade inteira transferida       |
| **moeda**            | Unidade fictícia EDU                 |

# Interface com Streamlit

A interface apresenta o título do projeto, uma explicação resumida, o formulário de nova transação, indicadores de quantidade de blocos e integridade, as duas carteiras com seus saldos e os dados de cada bloco em componentes expansíveis.

A instância de Blockchain é mantida em st.session_state. Essa escolha é necessária porque o Streamlit reexecuta o script quando há interação. O estado da sessão permite que saldos e blocos permaneçam disponíveis durante o uso da página \[6\]. O formulário agrupa origem, destino e valor e só envia os dados quando o botão é acionado \[5\].

| **Persistência:** Session State mantém o estado apenas durante a sessão ativa. Reiniciar o processo, limpar a sessão ou recarregar em determinadas condições recria a blockchain com os saldos iniciais. Não há banco de dados nem arquivo de persistência nesta versão. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# Testes e evidências de funcionamento

A suíte automatizada contém 15 testes aprovados. O pytest descobre funções nomeadas como test\_\* e relata cada caso de forma independente \[7\]. Os testes foram mantidos separados do código de interface, concentrando a verificação no comportamento do domínio.

Tabela 7 - Cobertura funcional dos 15 testes

| **Grupo**              | **Quantidade** | **Comportamentos verificados**                                                                 |
|------------------------|----------------|------------------------------------------------------------------------------------------------|
| **Estrutura básica**   | 4              | Bloco gênese, encadeamento, cadeia válida e detecção de alteração                              |
| **Carteiras iniciais** | 1              | Moeda, usuários, identificadores e saldos                                                      |
| **Validação**          | 6              | Saldo suficiente, saldo insuficiente, origem/destino inexistentes, mesma carteira e valor zero |
| **Realização**         | 3              | Atualização de saldos, criação de bloco e ausência de efeitos em rejeição                      |
| **Fluxo bidirecional** | 1              | Duas transferências, conservação de 200 EDU, três blocos e cadeia válida                       |

## Cenário integrado verificado

O teste integrado parte de 100 EDU em cada carteira. A primeira transação transfere 25 EDU de Emmanuel para Weberson; a segunda transfere 40 EDU de Weberson para Emmanuel. O saldo final é 115 EDU e 85 EDU, respectivamente. O total permanece em 200 EDU, a cadeia passa a conter três blocos e o hash anterior do último bloco coincide com o hash do bloco de transação precedente.

```text
python -m pytest -v
collected 15 items
15 passed in 0.06s
Saldo final: CARTEIRA-001 = 115 EDU | CARTEIRA-002 = 85 EDU
Quantidade de blocos = 3 | Integridade = Válida
```

# Rastreabilidade entre requisitos e evidências

Tabela 8 - Relação entre funcionalidade e evidência

| **Funcionalidade** | **Implementação**                 | **Evidência**                                    |
|--------------------|-----------------------------------|--------------------------------------------------|
| **Encadeamento**   | adicionar_bloco                   | Hash anterior conferido em teste                 |
| **Integridade**    | validar_cadeia                    | Cadeia válida e alteração detectada              |
| **Carteiras**      | Blockchain.carteiras              | Usuários e saldos iniciais testados              |
| **Regras**         | validar_transacao                 | Seis cenários de aceitação/rejeição              |
| **Movimentação**   | realizar_transacao                | Saldos atualizados e total conservado            |
| **Registro**       | dados_transacao + adicionar_bloco | Novo bloco com sete campos                       |
| **Interface**      | app.py                            | Formulário, mensagens, cartões e lista de blocos |

# Conceitos aplicados

- **Hash criptográfico:** Resumo determinístico de tamanho fixo usado para identificar o conteúdo do bloco.

- **Encadeamento:** Referência ao hash anterior, que estabelece dependência entre blocos consecutivos.

- **Integridade:** Capacidade de identificar divergências entre conteúdo atual e hash armazenado.

- **Bloco gênese:** Primeiro bloco, criado sem um predecessor real.

- **Determinismo:** Uso de serialização estável para que os mesmos dados produzam a mesma entrada de hash.

- **Validação antes da mutação:** Regras executadas antes de alterar saldos ou criar registros.

- **Conservação de saldo:** Transferências apenas redistribuem EDU entre carteiras; não criam nem eliminam unidades.

- **Teste de regressão:** Casos automatizados que protegem comportamentos já implementados durante novas mudanças.

# Descentralização: conceito e limite desta aplicação

Uma blockchain completa costuma envolver um registro distribuído entre participantes. Cada nó pode manter uma cópia do histórico, e um protocolo de consenso define como novas informações são aceitas. Essa combinação dificulta que uma única parte altere o passado sem ser identificada pelos demais participantes \[1\].

A aplicação deste desafio não implementa rede ponto a ponto, múltiplos nós, mineração, Proof of Work, Proof of Stake, chaves privadas, assinaturas digitais ou consenso. Existe uma única instância local em memória. Portanto, o termo blockchain educacional descreve os conceitos simulados - bloco, hash, encadeamento e verificação de integridade - e não uma infraestrutura descentralizada pronta para produção.

# Limitações conhecidas

- execução local e centralizada, sem cópias distribuídas;

- estado mantido apenas durante a sessão do Streamlit;

- ausência de banco de dados e persistência em arquivo;

- carteiras sem chaves públicas, chaves privadas ou assinaturas digitais;

- saldos iniciais definidos fora da cadeia;

- identificadores fixos e apenas dois usuários;

- moeda EDU sem valor ou função financeira real;

- valores inteiros, sem casas decimais;

- ausência de consenso, mineração e taxa de transação; e

- detecção de adulteração restrita ao estado observado pela instância local.

# Status atual e próximos passos

Tabela 9 - Plano de evolução após a V2

| **Etapa**   | **Conteúdo**                                                   | **Situação** |
|-------------|----------------------------------------------------------------|--------------|
| **Base**    | Blocos, hashes, encadeamento, validação e interface inicial    | Concluída    |
| **Etapa 2** | Usuários, carteiras, saldos, transações, interface e 15 testes | Concluída    |
| **Etapa 3** | Demonstração controlada de adulteração e resposta visual       | Próxima      |
| **Etapa 4** | Revisão geral, relatório final, README e preparação do vídeo   | Pendente     |

Esta V2 deve ser preservada como marco intermediário. Depois das próximas etapas, o relatório poderá receber uma nova versão com evidências adicionais, capturas finais da interface e a descrição da demonstração de integridade.

# Conclusão

A versão 0.2 transforma a demonstração inicial de encadeamento em uma aplicação interativa com regras de negócio verificáveis. O projeto mantém o foco nos fundamentos: dados serializados de modo estável, hashes SHA-256, ligação entre blocos e verificação de integridade. Ao mesmo tempo, introduz carteiras e transferências sem confundir a simulação com um sistema financeiro real.

Os 15 testes aprovados demonstram que transações válidas atualizam os saldos e criam blocos, enquanto operações inválidas preservam o estado. A conservação das 200 unidades EDU no cenário bidirecional reforça a consistência da lógica. As limitações permanecem explícitas, permitindo que o trabalho seja apresentado de forma tecnicamente honesta e evolua de maneira incremental nas etapas seguintes.

# Referências

[1] NIST. Blockchain Technology Overview. NISTIR 8202, 2018. Disponível em: [https://doi.org/10.6028/NIST.IR.8202](https://doi.org/10.6028/NIST.IR.8202). Acesso em: 1 set. 2026.

[2] PYTHON SOFTWARE FOUNDATION. hashlib - Secure hashes and message digests. Disponível em: [https://docs.python.org/3/library/hashlib.html](https://docs.python.org/3/library/hashlib.html). Acesso em: 1 set. 2026.

[3] PYTHON SOFTWARE FOUNDATION. json - JSON encoder and decoder. Disponível em: [https://docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html). Acesso em: 1 set. 2026.

[4] PYTHON SOFTWARE FOUNDATION. dataclasses - Data classes. Disponível em: [https://docs.python.org/3/library/dataclasses.html](https://docs.python.org/3/library/dataclasses.html). Acesso em: 1 set. 2026.

[5] STREAMLIT. st.form. Disponível em: [https://docs.streamlit.io/develop/api-reference/execution-flow/st.form](https://docs.streamlit.io/develop/api-reference/execution-flow/st.form). Acesso em: 1 set. 2026.

[6] STREAMLIT. Session State. Disponível em: [https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state). Acesso em: 1 set. 2026.

[7] PYTEST. Get started. Disponível em: [https://docs.pytest.org/en/stable/getting-started.html](https://docs.pytest.org/en/stable/getting-started.html). Acesso em: 1 set. 2026.

## Registro de versão

| **Documento**            | **Projeto** | **Abrangência**                           | **Data** |
|--------------------------|-------------|-------------------------------------------|----------|
| **Relatório Técnico V2** | v0.2        | Estrutura, carteiras, saldos e transações |          |
