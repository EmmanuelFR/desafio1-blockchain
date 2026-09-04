**UNIFAA -** Centro Universitário de Valença

**Curso:** Engenharia de Software

**Disciplina:** Desrupt IR Specialist – Explorando os Novos Horizontes das Tecnologias – 2026/2

**Professor:** Weberson Rodrigues de Araujo de Oliveira

**Aluno:** Emmanuel de Freitas Ribeiro

**RA:** E33006

**Data:** 04/09/2026

*Valença/RJ*

# Relatório Técnico - Blockchain Educacional

## Resumo executivo

Este relatório apresenta uma aplicação acadêmica desenvolvida para simular os fundamentos de uma blockchain. A solução cria blocos encadeados por hashes SHA-256, mantém duas carteiras educacionais, registra transferências na unidade fictícia EDU e permite verificar a integridade da cadeia por meio de uma adulteração controlada.

Este projeto reúne a revisão do código, o bloqueio de novas transações quando a cadeia está inválida, o aprimoramento da tipagem das carteiras, a reorganização dos estilos da interface, a conversão visual do horário UTC para o horário de Brasília, melhorias de UX/UI, a atualização do README e a ampliação da suíte automatizada.

*Estado final verificado:* 21 testes automatizados aprovados; transações válidas registradas em novos blocos; adulteração detectada sem modificação retroativa dos saldos; novas transações bloqueadas enquanto a cadeia estiver inválida; reinício da demonstração restaura um bloco gênese, saldos de 100 EDU e integridade válida.

*Síntese do estado final do projeto*

| **Dimensão**             | **Resultado final**                                                      |
|--------------------------|--------------------------------------------------------------------------|
| **Estrutura blockchain** | Bloco gênese, SHA-256, encadeamento e verificação de integridade         |
| **Carteiras**            | Emmanuel Freitas e Weberson Rodrigues, com 100 EDU cada                  |
| **Transações**           | Validação, atualização de saldos, registro e bloqueio em cadeia inválida |
| **Adulteração**          | Modificação controlada de valor sem recálculo do hash                    |
| **Interface**            | Formulários, tema visual, horário de Brasília, indicadores e reinício    |
| **Qualidade**            | 21 testes automatizados aprovados                                        |
| **Documentação**         | README e relatório técnico                                               |

## Introdução

Blockchain é uma forma de registrar informações em blocos ligados entre si. Cada bloco armazena dados, uma referência criptográfica ao bloco anterior e o próprio hash. Quando os dados de um bloco são alterados, o hash recalculado deixa de coincidir com o valor que havia sido armazenado, permitindo identificar a quebra de integridade. Em sistemas completos, outros mecanismos - como distribuição entre participantes e consenso - ampliam a resistência a adulterações.

Esse projeto foi desenvolvido para demonstrar esse encadeamento de maneira acessível. A aplicação é local e centralizada, portanto não pretende reproduzir uma rede pública nem uma criptomoeda real. Seu foco é educacional: tornar visíveis a geração de hashes, a relação entre blocos, as regras de uma transferência e os efeitos de uma modificação indevida.

## Objetivo da solução

Construção de uma blockchain educacional com blocos, transações, hashes e validação da cadeia. A aplicação foi desenvolvida para:

- criar um bloco gênese que inaugura a cadeia;

- adicionar novos blocos com índice, data e hora, dados e hash anterior;

- calcular hashes SHA-256 a partir de uma representação determinística do conteúdo;

- validar hashes armazenados e ligações entre blocos;

- representar carteiras educacionais e seus saldos em EDU (moeda fictícia);

- validar e realizar transferências entre carteiras;

- registrar cada transação aceita em um novo bloco;

- alterar intencionalmente o valor de um bloco de transação sem recalcular seu hash;

- evidenciar visualmente a cadeia válida e a cadeia adulterada;

- reiniciar a demonstração e restaurar o estado inicial;

- exibir o estado da aplicação em uma interface Streamlit;

- impedir novas transações enquanto a cadeia estiver inválida;

- apresentar datas e horários no padrão brasileiro e no horário de Brasília;

- verificar o comportamento com testes automatizados.

## Tecnologias utilizadas

*Aplicação e justificativa das tecnologias no projeto*

| **Tecnologia**         | **Papel no projeto**                         | **Justificativa**                                         |
|------------------------|----------------------------------------------|-----------------------------------------------------------|
| **Python 3.12.10**     | Lógica de blocos, hashes, carteiras e testes | Sintaxe legível e bibliotecas padrão adequadas ao escopo  |
| **Streamlit 1.62.0**   | Interface web interativa                     | Permite demonstrar o projeto usando apenas Python         |
| **CSS**                | Identidade visual e acessibilidade           | Centraliza tipografia, cores, foco e estados de interação |
| **pytest 9.1.1**       | Testes automatizados                         | Validação objetiva de regras e prevenção de regressões    |
| **Git**                | Controle de versão                           | Histórico incremental e rastreável das mudanças           |
| **Visual Studio Code** | Edição e execução                            | Ambiente integrado para código, terminal e extensões      |

### Justificativa para Python e Streamlit

Python foi escolhido por favorecer clareza de leitura e por disponibilizar, na biblioteca padrão, recursos diretamente úteis para o trabalho: hashlib para SHA-256, json para serialização determinística, dataclasses para a estrutura do bloco e datetime para os registros temporais.

Streamlit foi selecionado porque transforma funções Python em uma interface web com pouco código adicional. O framework oferece formulários para agrupar entradas e processá-las em um único envio, além de Session State para manter objetos entre as reexecuções de uma sessão. Isso reduz a complexidade de front-end e concentra a construção nos conceitos de blockchain, validação e testes.

## Arquitetura da aplicação

A aplicação separa a regra de negócio da apresentação, tornando o código mais compreensível, permitindo testar o núcleo sem abrir a interface e facilitando a evolução das próximas etapas.

*Responsabilidade dos principais arquivos*

| **Arquivo**                  | **Responsabilidade**     | **Elementos principais**                                                                   |
|------------------------------|--------------------------|--------------------------------------------------------------------------------------------|
| **blockchain.py**            | Domínio e regras         | Blocos, hashes, cadeia, carteiras, transações, validação e adulteração controlada          |
| **app.py**                   | Interface Streamlit      | Session State, formulários, indicadores, horário local, reinício e apresentação dos blocos |
| **.streamlit/config.toml**   | Tema                     | Paleta principal e cores semânticas de sucesso, aviso e erro                               |
| **.streamlit/styles.css**    | Estilos visuais          | Roboto, campos, foco, botões, alertas, dados JSON e tradução da instrução dos formulários  |
| **tests/test_blockchain.py** | Verificação automatizada | 21 testes para estrutura, transações, integridade, encadeamento e adulteração              |
| **docs/**                    | Documentação             | Relatório técnico em Markdown                                                              |

### Fluxo de execução

1. A interface recupera a instância de `Blockchain` mantida na sessão.
2. O usuário escolhe as carteiras de origem e destino e informa um valor inteiro em EDU.
3. O método `realizar_transacao` verifica primeiro a integridade da cadeia e, em seguida, `validar_transacao` confere a existência das carteiras, a diferença entre elas, o valor positivo e o saldo disponível.
4. Se a operação for rejeitada, a mensagem de erro é devolvida e nenhum saldo ou bloco é alterado.
5. Se a operação for aceita, os saldos são atualizados e os dados da transferência são enviados a `adicionar_bloco`.
6. A interface recalcula a situação da cadeia e apresenta os novos saldos, a quantidade de blocos e o registro criado.
7. Na demonstração de adulteração, o usuário escolhe um bloco de transação e informa um novo valor.
8. O método `simular_adulteracao` altera apenas o valor armazenado, sem recalcular o hash e sem movimentar saldos.
9. A validação passa a indicar a cadeia como inválida e novas transações são recusadas.
10. O botão de reinício cria uma nova instância de `Blockchain` e reexecuta a página, restaurando o cenário inicial.

### Estado e apresentação

A instância de `Blockchain` permanece em `st.session_state` durante a sessão. Os registros temporais são armazenados internamente em UTC, preservando um padrão inequívoco para o cálculo dos hashes. Somente a apresentação converte esses valores para UTC-3 e utiliza o formato brasileiro *dd/mm/aaaa às hh:mm:ss*.

A interface e os estilos ficam separados: `app.py` organiza componentes e interações, `config.toml` define o tema e `styles.css` concentra os ajustes visuais. Essa divisão reduz a quantidade de CSS incorporado ao código Python e facilita futuras manutenções.

A estrutura `DadosCarteira`, declarada com `TypedDict`, descreve explicitamente que cada carteira possui um campo `usuario` textual e um campo `saldo` inteiro. Isso torna a tipagem mais precisa para editores e analisadores estáticos, sem alterar o comportamento da aplicação em tempo de execução.

## Conceitos de Blockchain aplicados

### Estrutura do bloco

A classe Bloco é definida como uma dataclass e reúne os campos índice, data e hora, dados, hash anterior e hash. O uso de uma estrutura explícita facilita a inspeção dos registros e reduz a necessidade de código repetitivo para inicialização.

Para calcular o hash, o projeto reúne os campos que identificam o conteúdo do bloco, serializa os dados em JSON com chaves ordenadas e separadores consistentes, codifica o texto em UTF-8 e aplica SHA-256. O campo hash não participa da entrada, pois ele é o resultado do próprio cálculo.

```python
conteudo = {
    "indice": self.indice,
    "data_hora": self.data_hora,
    "dados": self.dados,
    "hash_anterior": self.hash_anterior,
}
conteudo_serializado = json.dumps(
    conteudo,
    ensure_ascii=False,
    sort_keys=True,
    separators=(",", ":"),
)
return hashlib.sha256(conteudo_serializado.encode("utf-8")).hexdigest()
```

### Bloco gênese e encadeamento

A cadeia começa com o bloco de índice 0. Seu hash anterior recebe o valor textual "0" e seus dados indicam o início da blockchain educacional. Cada novo bloco usa o hash do último bloco como `hash_anterior`. Assim, a referência registrada no bloco seguinte cria a dependência entre os elementos da cadeia.

### Verificação de integridade

O método `validar_cadeia` percorre os blocos e realiza duas verificações: recalcula o hash de cada bloco para compará-lo com o valor armazenado e, a partir do segundo bloco, confirma se `hash_anterior` coincide com o hash do bloco precedente. Se qualquer comparação falhar, a aplicação identifica o índice envolvido e informa que a cadeia é inválida.

### Descentralização conceitual

A aplicação executa localmente e mantém uma única cópia da cadeia em memória. Portanto, não implementa uma rede descentralizada real, múltiplos nós ou um mecanismo de consenso. O requisito de descentralização está atendido no nível conceitual, com a distinção explícita entre os fundamentos demonstrados e os componentes ausentes.

- **Ausência de uma autoridade única:** em uma blockchain completa, diferentes participantes aplicariam regras comuns de validação sem depender exclusivamente da decisão manual de uma entidade central. Neste protótipo, as regras são verificáveis pelo código, mas executadas em uma única instância.

- **Registro distribuído:** em uma rede real, cada nó poderia manter uma cópia do histórico e comparar sua versão com as demais. A aplicação possui apenas uma cadeia local e não simula a comunicação ou a sincronização entre cópias.

- **Confiança baseada em tecnologia:** SHA-256, serialização determinística e encadeamento permitem recalcular os hashes e identificar alterações. A confiança demonstrada decorre da verificação técnica da integridade, e não da ocultação dos dados ou da decisão de um operador.

A solução representa os fundamentos técnicos que sustentam uma blockchain, enquanto distribuição e consenso permanecem como conceitos documentados, compatíveis com o escopo acadêmico simplificado.

## Carteiras e a moeda fictícia EDU

*Estado inicial das carteiras educacionais*

| **Identificador** | **Usuário**        | **Saldo inicial** |
|-------------------|--------------------|-------------------|
| **CARTEIRA-001**  | Emmanuel Freitas   | 100 EDU           |
| **CARTEIRA-002**  | Weberson Rodrigues | 100 EDU           |

### Justificativa da moeda fictícia

EDU é uma unidade exclusivamente fictícia, sem valor monetário, cotação, conversão, rede de pagamento ou possibilidade de uso financeiro. Sua criação é uma decisão pedagógica do projeto. Ela permite representar, de forma simples e segura, os elementos essenciais de uma transferência - origem, destino, valor, saldo e registro em bloco - sem sugerir que a aplicação emite uma criptomoeda real.

A sigla EDU reforça o caráter educacional. Os valores são inteiros, o que evita discussões paralelas sobre precisão de números de ponto flutuante e mantém o foco na conservação do saldo total. Essa moeda existe para tornar o fluxo demonstrável, e não para simular um ativo financeiro completo.

### Saldos iniciais e simplificação adotada

Os saldos iniciais são definidos no estado das carteiras quando a classe Blockchain é criada. Eles não são emitidos pelo bloco gênese. Essa escolha reduz a complexidade nesta versão, porém significa que a cadeia, isoladamente, não contém todos os dados necessários para reconstruir o estado inicial das carteiras.

## Validação e realização de transações

Antes de movimentar qualquer saldo, a aplicação verifica a integridade da cadeia e executa todas as regras da transação. Essa ordem evita estados parciais: uma operação rejeitada termina antes de qualquer modificação nas carteiras ou na cadeia.

*Regras de validação de uma transação*

| **Regra**                | **Condição de rejeição**          | **Mensagem**                                                           |
|--------------------------|-----------------------------------|------------------------------------------------------------------------|
| **Origem existente**     | Identificador não localizado      | Carteira de origem não encontrada.                                     |
| **Destino existente**    | Identificador não localizado      | Carteira de destino não encontrada.                                    |
| **Carteiras diferentes** | Origem igual ao destino           | As carteiras de origem e destino devem ser diferentes.                 |
| **Valor positivo**       | Valor menor ou igual a zero       | O valor da transação deve ser maior que zero.                          |
| **Saldo suficiente**     | Saldo da origem menor que o valor | Saldo insuficiente.                                                    |
| **Cadeia íntegra**       | Hash ou ligação inválida          | Não é possível realizar transações enquanto a cadeia estiver inválida. |

### Bloqueio após adulteração

O método `realizar_transacao` consulta `validar_cadeia` antes de atualizar os saldos. Quando a cadeia está inválida, a operação é encerrada, nenhum saldo é alterado e nenhum bloco é criado. Essa regra impede que a demonstração continue acumulando transações sobre um histórico cuja integridade já foi comprometida.

```python
cadeia_valida, _ = self.validar_cadeia()
if not cadeia_valida:
    return False, (
        "Não é possível realizar transações enquanto a cadeia "
        "estiver inválida."
    )
```

### Registro da transferência

Quando todas as regras são satisfeitas, o método `realizar_transacao` debita a carteira de origem, credita a carteira de destino e cria um dicionário com os dados abaixo. Em seguida, esse conjunto é registrado em um novo bloco encadeado.

*Dados gravados no bloco de transação*

| **Campo**            | **Descrição**                        |
|----------------------|--------------------------------------|
| **tipo**             | Identifica o registro como transação |
| **carteira_origem**  | Identificador da carteira debitada   |
| **usuario_origem**   | Nome associado à carteira de origem  |
| **carteira_destino** | Identificador da carteira creditada  |
| **usuario_destino**  | Nome associado à carteira de destino |
| **valor**            | Quantidade inteira transferida       |
| **moeda**            | EDU (Unidade fictícia)               |

## Interface com Streamlit

A interface apresenta o título do projeto, o formulário de nova transação, a demonstração de adulteração, os indicadores de quantidade de blocos e integridade, as duas carteiras com seus saldos e os dados de cada bloco em componentes expansíveis. O bloco mais recente permanece aberto por padrão, enquanto os anteriores podem ser consultados sob demanda.

A instância de `Blockchain` é mantida em `st.session_state`. Essa escolha é necessária porque o Streamlit reexecuta o script quando há interação. O estado da sessão permite que saldos e blocos permaneçam disponíveis durante o uso da página. O formulário agrupa origem, destino e valor e só envia os dados quando o botão é acionado.

*Persistência:* Session State mantém o estado apenas durante a sessão ativa. Reiniciar o processo, limpar a sessão ou recarregar em determinadas condições recria a blockchain com os saldos iniciais. Não há banco de dados nem arquivo de persistência.

### Consolidação visual e de usabilidade

Foi aplicada a fonte Roboto, uma paleta azul para ações principais, cores semânticas para sucesso, aviso e erro, contornos visíveis nos campos e estados de foco compatíveis com navegação por teclado. O botão de reinício utiliza tratamento secundário para não competir visualmente com as ações de transação e adulteração.

Essas decisões também consideram princípios de usabilidade aplicáveis ao desenho de interfaces, como visibilidade do estado do sistema, correspondência entre a linguagem da aplicação e a linguagem do usuário, consistência, prevenção de erros e feedback compreensível.

Os estilos foram transferidos do código Python para `.streamlit/styles.css`. O arquivo `.streamlit/config.toml` concentra a configuração do tema. A instrução automática dos formulários foi traduzida para “Pressione Enter para enviar.”, mantendo o comportamento de envio por teclado.

### Data e hora na interface

Os blocos armazenam a data e a hora em UTC, e esse valor está incluído no cálculo do hash. Para facilitar a leitura, `app.py` converte apenas a apresentação para o horário de Brasília e exibe o formato *dd/mm/aaaa às hh:mm:ss*. Dessa forma, a localização visual não modifica o conteúdo criptograficamente identificado.

## Demonstração controlada de adulteração

O objetivo do método `simular_adulteracao` na classe `Blockchain` é produzir uma inconsistência observável e segura para fins didáticos: o método altera o campo valor de um bloco de transação já existente, mas não recalcula o hash do bloco. Desse modo, a cadeia conserva a evidência do valor criptográfico originalmente calculado e a verificação posterior consegue identificar que o conteúdo foi modificado.

A operação não representa uma nova transação. Por isso, ela não debita ou credita carteiras, não cria um bloco adicional e não atualiza o hash armazenado. A separação entre o estado das carteiras e os dados adulterados permite mostrar que a detecção de integridade atua sobre o registro da cadeia, sem reprocessar retroativamente os saldos desta simulação.

*Regras da adulteração controlada*

| **Regra**              | **Condição de rejeição**                | **Mensagem**                                         |
|------------------------|-----------------------------------------|------------------------------------------------------|
| **Bloco selecionável** | Índice zero, negativo ou fora da cadeia | Selecione um bloco de transação válido.              |
| **Tipo do bloco**      | Bloco sem dados de transação            | O bloco selecionado não contém uma transação.        |
| **Valor positivo**     | Novo valor menor ou igual a zero        | O novo valor deve ser maior que zero.                |
| **Valor diferente**    | Novo valor igual ao registrado          | O novo valor deve ser diferente do valor registrado. |

### Efeito sobre o hash e a validação

```python
valor_original = bloco.dados["valor"]
bloco.dados["valor"] = novo_valor
# O hash armazenado não é recalculado.
cadeia_valida, mensagem = blockchain.validar_cadeia()
# Resultado: False, "O conteúdo do bloco 1 foi alterado."
```

Quando `validar_cadeia` recalcula o hash a partir do conteúdo adulterado, o resultado já não coincide com o hash original armazenado. A interface altera o indicador de integridade para *Inválida* e apresenta a mensagem que identifica o bloco afetado, conectando diretamente a ação do usuário ao conceito de imutabilidade verificável.

### Interface e reinício da demonstração

A interface lista somente blocos cujo tipo é `transacao`, excluindo o bloco gênese da seleção. O formulário permite escolher o bloco e informar um novo valor inteiro, com 999 EDU como valor inicial de conveniência. Após a confirmação, uma mensagem de aviso descreve o valor original e o novo valor, e o painel de integridade exibe a inconsistência.

O botão *Reiniciar demonstração* substitui o objeto guardado em `st.session_state` por uma nova instância de `Blockchain` e executa `st.rerun`. O estado do domínio volta a conter apenas o bloco gênese, as duas carteiras retornam a 100 EDU e a cadeia volta a ser válida. Os valores visuais mantidos por widgets podem permanecer preenchidos, como o campo de uma transação anterior; isso não altera o fato de que blocos, saldos e integridade foram restaurados.

*Resultado observado:* Após uma transação de 25 EDU, a cadeia contém dois blocos e os saldos são 75 EDU e 125 EDU. A adulteração do bloco 1 para 999 EDU mantém esses saldos e os dois blocos, mas torna a cadeia inválida. O reinício restaura um bloco, 100 EDU em cada carteira e integridade válida.

## Checkpoints do desenvolvimento

### Checkpoint da Etapa 1

Estabeleceu a base funcional da blockchain educacional e criou o ponto inicial do histórico versionado.

*Implementação da Etapa 1*

| **Commit**  | **Entrega**                              | **Evidência principal**                                 |
|-------------|------------------------------------------|---------------------------------------------------------|
| **b61d914** | Versão inicial da blockchain educacional | Estrutura inicial de blocos, hashes, cadeia e validação |

### Checkpoints da Etapa 2

Acrescenta os usuários, as carteiras, as regras de transação, o registro das transferências e os componentes correspondentes da interface. Os testes acompanham a ampliação do comportamento do domínio.

*Implementação da Etapa 2*

| **Commit**  | **Entrega**                              | **Evidência principal**                                       |
|-------------|------------------------------------------|---------------------------------------------------------------|
| **434192e** | Carteiras educacionais e testes iniciais | Dois usuários, saldos iniciais e verificações correspondentes |
| **c93657d** | Validação de transações educacionais     | Regras para origem, destino, valor e saldo                    |
| **894721a** | Transferências e registro em blocos      | Atualização de saldos e criação do bloco de transação         |
| **dd49bbe** | Carteiras e saldos na interface          | Apresentação visual das duas carteiras                        |
| **c52b373** | Formulário de transações na interface    | Entradas de origem, destino e valor                           |
| **ecf55a0** | Teste de transações nos dois sentidos    | Fluxo bidirecional e conservação do saldo total               |

### Checkpoints da Etapa 3

Incorpora a adulteração controlada, sua demonstração na interface e o reinício do estado. A etapa também consolida arquivos auxiliares.

*Implementação da Etapa 3*

| **Commit**  | **Entrega**                              | **Evidência principal**                                    |
|-------------|------------------------------------------|------------------------------------------------------------|
| **64d00a9** | Simulação controlada de adulteração      | Método de domínio e quatro novos testes                    |
| **07ff8a7** | Demonstração de adulteração na interface | Cadeia válida antes e inválida após a alteração            |
| **76e1952** | Botão de reinício da demonstração        | Restauração do bloco gênese, saldos e integridade          |
| **1fa8273** | Atualização do arquivo .gitignore        | Exclusão de arquivos locais e temporários do versionamento |
| **4cb45e7** | Relatório técnico provisório V3          | Registro documental provisório da Etapa 3                  |

### Checkpoints da Etapa final

Distribuída em checkpoints de documentação, interface, integridade, tipagem, organização e testes. O histórico preserva a finalidade de cada mudança e permite revisar a evolução sem concentrar todas as decisões em um único commit.

*Consolidação da Etapa final*

| **Commit**  | **Entrega**                               | **Evidência principal**                                       |
|-------------|-------------------------------------------|---------------------------------------------------------------|
| **94f6d57** | Atualização inicial do README             | Funcionalidades e instruções de execução revisadas            |
| **b4722cb** | Identidade visual e usabilidade           | Roboto, paleta, campos, botões, cartões e horário de Brasília |
| **4d87641** | Bloqueio de transações em cadeia inválida | Regra de domínio e teste de ausência de efeitos colaterais    |
| **080001c** | Tipagem das carteiras                     | DadosCarteira definido com TypedDict                          |
| **5c04f1d** | Separação dos estilos visuais             | CSS removido de app.py e centralizado em arquivo próprio      |
| **b961709** | Consolidação do README e .gitignore       | Documentação atualizada e padrão redundante removido          |
| **5a17a33** | Teste de ligação inválida                 | Verificação direta do vínculo entre blocos                    |
| **dead5a0** | Tradução da instrução dos formulários     | Texto de apoio apresentado em português                       |

## Testes e evidências de funcionamento

A suíte automatizada contém 21 testes aprovados. O pytest descobre funções nomeadas como *test\_\** e relata cada caso de forma independente. Os testes estão separados do código de interface, concentrando a verificação no comportamento do domínio e protegendo as funcionalidades das etapas anteriores contra regressões.

*Cobertura funcional dos 21 testes*

| **Grupo**                   | **Quantidade** | **Comportamentos verificados**                                                                 |
|-----------------------------|----------------|------------------------------------------------------------------------------------------------|
| **Estrutura e integridade** | 5              | Bloco gênese, encadeamento, cadeia válida, alteração de conteúdo e ligação inválida            |
| **Carteiras iniciais**      | 1              | Moeda, usuários, identificadores e saldos                                                      |
| **Validação**               | 6              | Saldo suficiente, saldo insuficiente, origem/destino inexistentes, mesma carteira e valor zero |
| **Realização**              | 3              | Atualização de saldos, criação de bloco e ausência de efeitos em rejeição                      |
| **Fluxo bidirecional**      | 1              | Duas transferências, conservação de 200 EDU, três blocos e cadeia válida                       |
| **Adulteração controlada**  | 4              | Invalidação da cadeia e rejeição de bloco gênese, valor inválido e valor idêntico              |
| **Cadeia inválida**         | 1              | Bloqueio de nova transação sem modificar saldos ou quantidade de blocos                        |

### Cenário integrado verificado

O cenário integrado parte de 100 EDU em cada carteira e registra uma transação de 25 EDU de Emmanuel para Weberson. Os saldos passam a 75 EDU e 125 EDU e a cadeia contém dois blocos. Em seguida, o valor do bloco 1 é alterado para 999 EDU sem recalcular seu hash. A quantidade de blocos e os saldos permanecem iguais, `validar_cadeia` retorna `False` e uma tentativa posterior de transação é recusada.

```text
python -m pytest -v
collected 21 items
21 passed
Antes: bloco 1 = 25 EDU | hash armazenado = hash original
Depois: bloco 1 = 999 EDU | hash armazenado = hash original
Saldos = 75/125 EDU | blocos = 2 | Integridade = Inválida
Nova transação = recusada | saldos e blocos permanecem inalterados
```

## Atendimento aos requisitos mínimos do desafio

*Rastreabilidade entre requisitos e evidências*

| **Requisito**                   | **Implementação e evidência**                                                                                        |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Estrutura de Blockchain**     | Bloco com índice, data e hora, dados, hash anterior e hash; criação e validação testadas                             |
| **Simulação de usuários**       | Duas carteiras com usuários, identificadores e 100 EDU; transferências nos dois sentidos                             |
| **Registro das transações**     | Cada operação aceita cria um novo bloco com origem, destino, valor, usuários e moeda                                 |
| **Validação da cadeia**         | Hashes e ligações são verificados; adulterações e vínculos inválidos são detectados                                  |
| **Descentralização conceitual** | Ausência de autoridade única, registro distribuído e confiança tecnológica são explicados; a rede não é implementada |

## Consolidação da Etapa final

*Etapas do projeto*

| **Etapa**       | **Conteúdo**                                                       |
|-----------------|--------------------------------------------------------------------|
| **Etapa 1**     | Blocos, hashes, encadeamento, validação e interface inicial        |
| **Etapa 2**     | Usuários, carteiras, saldos, transações, interface e 15 testes     |
| **Etapa 3**     | Adulteração controlada, resposta visual, reinício e 19 testes      |
| **Etapa final** | Revisão técnica, UX/UI, tipagem, estilos, documentação e 21 testes |

## Limitações da implementação

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

- reinício sem persistência: o histórico da sessão é descartado ao criar a nova instância;

- estado visual de alguns widgets pode permanecer preenchido após o reinício do domínio;

- a fonte Roboto é solicitada por recurso externo na interface; sem conexão, o navegador utiliza uma fonte sans-serif alternativa;

- seletores CSS vinculados à estrutura interna do Streamlit podem exigir revisão após uma atualização do framework.

## Conclusão

O desenvolvimento deste desafio consolida uma aplicação interativa capaz de criar blocos, movimentar a unidade fictícia EDU, validar regras de negócio e demonstrar visualmente a detecção de adulteração. O projeto mantém o foco nos fundamentos: dados serializados de modo estável, hashes SHA-256, ligação entre blocos e comparação entre o hash armazenado e o hash recalculado.

Os 21 testes aprovados demonstram que as funcionalidades permanecem válidas e que a adulteração controlada opera dentro dos limites definidos. A mudança de 25 para 999 EDU no bloco de transação preserva o hash original, não altera saldos nem cria blocos e torna a cadeia inválida de forma verificável. A partir desse estado, novas transferências são bloqueadas. O reinício completa o ciclo didático ao restaurar o cenário inicial para uma nova demonstração.

## Síntese dos conceitos técnicos

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

## Referências

### Documentação técnica e fontes institucionais

[1] NIST. Blockchain Technology Overview. NISTIR 8202, 2018. Disponível em: [https://doi.org/10.6028/NIST.IR.8202](https://doi.org/10.6028/NIST.IR.8202). Acesso em: 1 set. 2026.

[2] PYTHON SOFTWARE FOUNDATION. hashlib - Secure hashes and message digests. Disponível em: [https://docs.python.org/3/library/hashlib.html](https://docs.python.org/3/library/hashlib.html). Acesso em: 1 set. 2026.

[3] PYTHON SOFTWARE FOUNDATION. json - JSON encoder and decoder. Disponível em: [https://docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html). Acesso em: 1 set. 2026.

[4] PYTHON SOFTWARE FOUNDATION. dataclasses - Data classes. Disponível em: [https://docs.python.org/3/library/dataclasses.html](https://docs.python.org/3/library/dataclasses.html). Acesso em: 1 set. 2026.

[5] STREAMLIT. st.form. Disponível em: [https://docs.streamlit.io/develop/api-reference/execution-flow/st.form](https://docs.streamlit.io/develop/api-reference/execution-flow/st.form). Acesso em: 1 set. 2026.

[6] STREAMLIT. Session State. Disponível em: [https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state). Acesso em: 1 set. 2026.

[7] PYTEST. Get started. Disponível em: [https://docs.pytest.org/en/stable/getting-started.html](https://docs.pytest.org/en/stable/getting-started.html). Acesso em: 1 set. 2026.

[8] STREAMLIT. st.rerun. Disponível em: [https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun](https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun). Acesso em: 2 set. 2026.

### UX/UI e usabilidade

[9] INTERACTION DESIGN FOUNDATION. *What are heuristics?* [S. l.]: IxDF, 2026. Disponível em: [https://ixdf.org/literature/topics/heuristics](https://ixdf.org/literature/topics/heuristics). Acesso em: 4 set. 2026.

### Material didático da disciplina

[10] UNIFAA - CENTRO UNIVERSITÁRIO DE VALENÇA. Blockchain e Contratos Inteligentes: a revolução da confiança, segurança e descentralização digital. Apresentação de slides da Unidade 4 da disciplina Desrupt IR Specialist - Explorando os Novos Horizontes das Tecnologias. Valença, 2026. 7 slides. Material disponibilizado em aula.

**Emmanuel de Freitas Ribeiro**
