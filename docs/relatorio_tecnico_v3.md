**UNIFAA - Centro Universitário de Valença**

Curso de Engenharia de Software

**RELATÓRIO TÉCNICO \| DESAFIO 1**

**Blockchain Educacional**

Estrutura, transações, adulteração controlada e verificação de integridade

**VERSÃO 3 \| DOCUMENTO INTERMEDIÁRIO \| PROJETO v0.3**

| **Curso:**      | Engenharia de Software                                                          |
|-----------------|---------------------------------------------------------------------------------|
| **Disciplina:** | DESRUPT IR SPECIALIST – EXPLORANDO OS NOVOS HORIZONTES DAS TECNOLOGIAS – 2026/2 |
| **Professor:**  | WEBERSON RODRIGUES DE ARAUJO DE OLIVEIRA                                        |
| **Aluno:**      | Emmanuel de Freitas Ribeiro                                                     |
| **RA:**         | E33006                                                                          |
| **Data:**       |                                                                                 |

Valença - RJ

# Resumo executivo

Este relatório apresenta a Versão 3 do Desafio 1, uma aplicação acadêmica que simula os fundamentos de uma blockchain. Além da criação de blocos encadeados por hashes SHA-256, da verificação de integridade, das carteiras educacionais e das transferências em EDU, esta versão documenta a Etapa 3: uma demonstração controlada de adulteração, sua detecção visual e o reinício do cenário.

O documento corresponde ao estado intermediário do projeto v0.3. A adulteração modifica intencionalmente o valor registrado em um bloco de transação sem recalcular seu hash. Como consequência, a validação identifica a divergência entre o conteúdo atual e o hash armazenado, enquanto saldos e quantidade de blocos permanecem inalterados. A consolidação final do README, do relatório e do roteiro de apresentação permanece reservada para a Etapa 4.

| **Estado verificado:** 19 testes automatizados aprovados; simulação de adulteração restrita a blocos de transação; hash armazenado preservado durante a modificação; cadeia invalidada de forma detectável; reinício da demonstração restaura um bloco gênese, saldos de 100 EDU e integridade válida. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Tabela 1 - Síntese do estado da versão 0.3

| **Dimensão**             | **Resultado atual**                                                | **Situação** |
|--------------------------|--------------------------------------------------------------------|--------------|
| **Estrutura blockchain** | Bloco gênese, SHA-256, encadeamento e verificação de integridade   | Implementado |
| **Carteiras**            | Emmanuel Freitas e Weberson Rodrigues, com 100 EDU cada            | Implementado |
| **Transações**           | Validação, atualização de saldos e registro em novo bloco          | Implementado |
| **Adulteração**          | Modificação controlada de valor sem recálculo do hash              | Implementado |
| **Interface**            | Transação, adulteração, resposta visual, indicadores e reinício    | Implementado |
| **Qualidade**            | 19 testes automatizados aprovados                                  | Verificado   |
| **Próximo ciclo**        | Revisão geral, relatório final, README e roteiro de vídeo          | Pendente     |

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

- alterar intencionalmente o valor de um bloco de transação sem recalcular seu hash;

- evidenciar visualmente a cadeia válida e a cadeia adulterada;

- reiniciar a demonstração e restaurar o estado inicial;

- exibir o estado da aplicação em uma interface Streamlit; e

- verificar o comportamento com testes automatizados.

| **Escopo desta V3:** A versão documenta o núcleo da blockchain, as carteiras e transações da Etapa 2 e toda a Etapa 3: adulteração controlada, detecção da inconsistência na interface e reinício da demonstração. A Etapa 4 permanece pendente. |
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
| **blockchain.py**            | Domínio e regras         | Blocos, hashes, cadeia, carteiras, transações, validação e adulteração controlada              |
| **app.py**                   | Interface Streamlit      | Session State, formulários, indicadores, saldos, adulteração, reinício e blocos                |
| **tests/test_blockchain.py** | Verificação automatizada | 19 testes para estrutura, transações, conservação de saldos e adulteração                      |
| **docs/**                    | Documentação             | Relatórios técnicos e materiais de apoio                                                      |

## Fluxo de execução

1.  A interface recupera a instância de Blockchain mantida na sessão.

2.  O usuário escolhe as carteiras de origem e destino e informa um valor inteiro em EDU.

3.  O método validar_transacao verifica a existência das carteiras, a diferença entre elas, o valor positivo e o saldo disponível.

4.  Se a operação for rejeitada, a mensagem de erro é devolvida e nenhum saldo ou bloco é alterado.

5.  Se a operação for aceita, os saldos são atualizados e os dados da transferência são enviados a adicionar_bloco.

6.  A interface recalcula a situação da cadeia e apresenta os novos saldos, a quantidade de blocos e o registro criado.

7.  Na demonstração de adulteração, o usuário escolhe um bloco de transação e informa um novo valor.

8.  O método simular_adulteracao altera apenas o valor armazenado, sem recalcular o hash e sem movimentar saldos.

9.  A validação passa a indicar a cadeia como inválida; o botão de reinício cria uma nova instância de Blockchain e reexecuta a página.

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

# Demonstração controlada de adulteração

A Etapa 3 acrescenta o método simular_adulteracao à classe Blockchain. Seu objetivo é produzir uma inconsistência observável e segura para fins didáticos: o método altera o campo valor de um bloco de transação já existente, mas não recalcula o hash do bloco. Desse modo, a cadeia conserva a evidência do valor criptográfico originalmente calculado e a verificação posterior consegue identificar que o conteúdo foi modificado.

A operação não representa uma nova transação. Por isso, ela não debita ou credita carteiras, não cria um bloco adicional e não atualiza o hash armazenado. A separação entre o estado das carteiras e os dados adulterados permite mostrar que a detecção de integridade atua sobre o registro da cadeia, sem reprocessar retroativamente os saldos desta simulação.

Tabela 7 - Regras da adulteração controlada

| **Regra**            | **Condição de rejeição**                  | **Mensagem**                                               |
|----------------------|-------------------------------------------|------------------------------------------------------------|
| **Bloco selecionável** | Índice zero, negativo ou fora da cadeia | Selecione um bloco de transação válido.                     |
| **Tipo do bloco**    | Bloco sem dados de transação               | O bloco selecionado não contém uma transação.               |
| **Valor positivo**   | Novo valor menor ou igual a zero           | O novo valor deve ser maior que zero.                       |
| **Valor diferente**  | Novo valor igual ao registrado             | O novo valor deve ser diferente do valor registrado.        |

## Efeito sobre o hash e a validação

```python
valor_original = bloco.dados["valor"]
bloco.dados["valor"] = novo_valor
# O hash armazenado não é recalculado.
cadeia_valida, mensagem = blockchain.validar_cadeia()
# Resultado: False, "O conteúdo do bloco 1 foi alterado."
```

Quando validar_cadeia recalcula o hash a partir do conteúdo adulterado, o resultado já não coincide com o hash original armazenado. A interface altera o indicador de integridade para **Inválida** e apresenta a mensagem que identifica o bloco afetado. Essa resposta visual conecta diretamente a ação do usuário ao conceito de imutabilidade verificável.

## Interface e reinício da demonstração

A interface lista somente blocos cujo tipo é transacao, excluindo o bloco gênese da seleção. O formulário permite escolher o bloco e informar um novo valor inteiro, com 999 EDU como valor inicial de conveniência. Após a confirmação, uma mensagem de aviso descreve o valor original e o novo valor, e o painel de integridade exibe a inconsistência.

O botão **Reiniciar demonstração** substitui o objeto guardado em st.session_state por uma nova instância de Blockchain e executa st.rerun \[8\]. O estado do domínio volta a conter apenas o bloco gênese, as duas carteiras retornam a 100 EDU e a cadeia volta a ser válida. Os valores visuais mantidos por widgets podem permanecer preenchidos, como o campo de uma transação anterior; isso não altera o fato de que blocos, saldos e integridade foram restaurados.

| **Resultado observado:** Após uma transação de 25 EDU, a cadeia contém dois blocos e os saldos são 75 EDU e 125 EDU. A adulteração do bloco 1 para 999 EDU mantém esses saldos e os dois blocos, mas torna a cadeia inválida. O reinício restaura um bloco, 100 EDU em cada carteira e integridade válida. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Checkpoints da Etapa 3

A implementação foi registrada em três checkpoints independentes. Essa divisão separa a regra de domínio, sua apresentação na interface e o mecanismo de reinício, facilitando a rastreabilidade das decisões e a revisão incremental.

Quadro 1 - Histórico de implementação da Etapa 3

| **Commit** | **Entrega**                                      | **Evidência principal**                                   |
|------------|--------------------------------------------------|-----------------------------------------------------------|
| **64d00a9** | Simulação controlada de adulteração             | Método de domínio e quatro novos testes                    |
| **07ff8a7** | Demonstração de adulteração na interface        | Cadeia válida antes e inválida após a alteração            |
| **7e1c952** | Botão de reinício da demonstração               | Restauração do bloco gênese, saldos e integridade          |

# Testes e evidências de funcionamento

A suíte automatizada contém 19 testes aprovados. O pytest descobre funções nomeadas como test\_\* e relata cada caso de forma independente \[7\]. Os testes foram mantidos separados do código de interface, concentrando a verificação no comportamento do domínio e protegendo as funcionalidades das etapas anteriores contra regressões.

Tabela 8 - Cobertura funcional dos 19 testes

| **Grupo**              | **Quantidade** | **Comportamentos verificados**                                                                 |
|------------------------|----------------|------------------------------------------------------------------------------------------------|
| **Estrutura básica**   | 4              | Bloco gênese, encadeamento, cadeia válida e detecção de alteração                              |
| **Carteiras iniciais** | 1              | Moeda, usuários, identificadores e saldos                                                      |
| **Validação**          | 6              | Saldo suficiente, saldo insuficiente, origem/destino inexistentes, mesma carteira e valor zero |
| **Realização**         | 3              | Atualização de saldos, criação de bloco e ausência de efeitos em rejeição                      |
| **Fluxo bidirecional** | 1              | Duas transferências, conservação de 200 EDU, três blocos e cadeia válida                       |
| **Adulteração controlada** | 4          | Invalidação da cadeia e rejeição de bloco gênese, valor inválido e valor idêntico               |

## Cenário integrado verificado

O cenário da Etapa 3 parte de 100 EDU em cada carteira e registra uma transação de 25 EDU de Emmanuel para Weberson. Os saldos passam a 75 EDU e 125 EDU e a cadeia contém dois blocos. Em seguida, o valor do bloco 1 é alterado para 999 EDU sem recalcular seu hash. A quantidade de blocos e os saldos permanecem iguais, porém validar_cadeia retorna False e informa que o conteúdo do bloco 1 foi alterado.

```text
python -m pytest -v
collected 19 items
19 passed in 0.12s
Antes: bloco 1 = 25 EDU | hash armazenado = hash original
Depois: bloco 1 = 999 EDU | hash armazenado = hash original
Saldos = 75/125 EDU | blocos = 2 | Integridade = Inválida
```

# Rastreabilidade entre requisitos e evidências

Tabela 9 - Relação entre funcionalidade e evidência

| **Funcionalidade** | **Implementação**                 | **Evidência**                                    |
|--------------------|-----------------------------------|--------------------------------------------------|
| **Encadeamento**   | adicionar_bloco                   | Hash anterior conferido em teste                 |
| **Integridade**    | validar_cadeia                    | Cadeia válida e alteração detectada              |
| **Carteiras**      | Blockchain.carteiras              | Usuários e saldos iniciais testados              |
| **Regras**         | validar_transacao                 | Seis cenários de aceitação/rejeição              |
| **Movimentação**   | realizar_transacao                | Saldos atualizados e total conservado            |
| **Registro**       | dados_transacao + adicionar_bloco | Novo bloco com sete campos                       |
| **Adulteração**    | simular_adulteracao               | Valor alterado sem recálculo do hash             |
| **Resposta visual**| app.py                            | Seleção de bloco, aviso e indicador Inválida     |
| **Reinício**       | Blockchain() + st.rerun           | Bloco gênese, saldos e integridade restaurados   |
| **Interface**      | app.py                            | Formulários, mensagens, cartões e blocos         |

# Conceitos aplicados

- **Hash criptográfico:** Resumo determinístico de tamanho fixo usado para identificar o conteúdo do bloco.

- **Encadeamento:** Referência ao hash anterior, que estabelece dependência entre blocos consecutivos.

- **Integridade:** Capacidade de identificar divergências entre conteúdo atual e hash armazenado.

- **Bloco gênese:** Primeiro bloco, criado sem um predecessor real.

- **Determinismo:** Uso de serialização estável para que os mesmos dados produzam a mesma entrada de hash.

- **Validação antes da mutação:** Regras executadas antes de alterar saldos ou criar registros.

- **Conservação de saldo:** Transferências apenas redistribuem EDU entre carteiras; não criam nem eliminam unidades.

- **Adulteração controlada:** Mudança intencional em um registro existente para demonstrar a detecção de inconsistência.

- **Hash armazenado versus recalculado:** A divergência entre os dois valores revela que o conteúdo do bloco foi modificado.

- **Reinício de estado:** Criação de uma nova instância do domínio para restaurar o cenário inicial da sessão.

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

- ausência de consenso, mineração e taxa de transação;

- adulteração restrita ao campo valor de blocos de transação e ao estado observado pela instância local;

- reinício sem persistência: o histórico da sessão é descartado ao criar a nova instância; e

- estado visual de alguns widgets pode permanecer preenchido após o reinício do domínio.

# Status atual e próximos passos

Tabela 10 - Plano de evolução após a V3

| **Etapa**   | **Conteúdo**                                                   | **Situação** |
|-------------|----------------------------------------------------------------|--------------|
| **Base**    | Blocos, hashes, encadeamento, validação e interface inicial    | Concluída    |
| **Etapa 2** | Usuários, carteiras, saldos, transações, interface e 15 testes | Concluída    |
| **Etapa 3** | Adulteração controlada, resposta visual, reinício e 19 testes  | Concluída    |
| **Etapa 4** | Revisão geral, relatório final, README e preparação do vídeo   | Pendente     |

Esta V3 deve ser preservada como marco intermediário da Etapa 3. A próxima versão poderá consolidar a revisão geral do projeto, atualizar o README, incorporar as evidências finais selecionadas e apoiar a preparação do vídeo de apresentação.

# Conclusão

A versão 0.3 consolida uma aplicação interativa capaz de criar blocos, movimentar a unidade fictícia EDU, validar regras de negócio e demonstrar visualmente a detecção de adulteração. O projeto mantém o foco nos fundamentos: dados serializados de modo estável, hashes SHA-256, ligação entre blocos e comparação entre o hash armazenado e o hash recalculado.

Os 19 testes aprovados demonstram que as funcionalidades das etapas anteriores continuam válidas e que a adulteração controlada opera dentro dos limites definidos. A mudança de 25 para 999 EDU no bloco de transação preserva o hash original, não altera saldos nem cria blocos e torna a cadeia inválida de forma verificável. O reinício completa o ciclo didático ao restaurar o estado inicial para uma nova demonstração.

# Referências

[1] NIST. Blockchain Technology Overview. NISTIR 8202, 2018. Disponível em: [https://doi.org/10.6028/NIST.IR.8202](https://doi.org/10.6028/NIST.IR.8202). Acesso em: 1 set. 2026.

[2] PYTHON SOFTWARE FOUNDATION. hashlib - Secure hashes and message digests. Disponível em: [https://docs.python.org/3/library/hashlib.html](https://docs.python.org/3/library/hashlib.html). Acesso em: 1 set. 2026.

[3] PYTHON SOFTWARE FOUNDATION. json - JSON encoder and decoder. Disponível em: [https://docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html). Acesso em: 1 set. 2026.

[4] PYTHON SOFTWARE FOUNDATION. dataclasses - Data classes. Disponível em: [https://docs.python.org/3/library/dataclasses.html](https://docs.python.org/3/library/dataclasses.html). Acesso em: 1 set. 2026.

[5] STREAMLIT. st.form. Disponível em: [https://docs.streamlit.io/develop/api-reference/execution-flow/st.form](https://docs.streamlit.io/develop/api-reference/execution-flow/st.form). Acesso em: 1 set. 2026.

[6] STREAMLIT. Session State. Disponível em: [https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state). Acesso em: 1 set. 2026.

[7] PYTEST. Get started. Disponível em: [https://docs.pytest.org/en/stable/getting-started.html](https://docs.pytest.org/en/stable/getting-started.html). Acesso em: 1 set. 2026.

[8] STREAMLIT. st.rerun. Disponível em: [https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun](https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun). Acesso em: 2 set. 2026.

## Registro de versão

| **Documento**            | **Projeto** | **Abrangência**                           | **Data** |
|--------------------------|-------------|-------------------------------------------|----------|
| **Relatório Técnico V3** | v0.3        | Etapas 1 a 3, incluindo adulteração e reinício |       |
