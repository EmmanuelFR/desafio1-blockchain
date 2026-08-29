# Relatório Técnico — Desafio 1: Blockchain Educacional

**Disciplina:** Desrupt IR  
**Aluno:** [preencher nome completo]  
**Versão do projeto:** 0.1 — estrutura inicial e aplicação mínima  
**Data:** [preencher data de entrega]

## Introdução

Este relatório apresenta o desenvolvimento de uma aplicação educacional que
simula os elementos básicos de uma blockchain. O projeto busca demonstrar, de
forma prática e visual, como blocos são criados, identificados por hashes e
ligados ao bloco anterior. A solução também permitirá registrar transações e
verificar se a cadeia sofreu alguma alteração. Por ter finalidade acadêmica, a
aplicação simplifica vários elementos existentes em redes blockchain reais.

## Objetivo da solução

O objetivo é desenvolver uma aplicação interativa capaz de simular uma
blockchain com, no mínimo, dois usuários realizando operações com uma moeda
fictícia. Cada transação deverá gerar um novo bloco contendo identificador,
data e hora, dados da operação, hash próprio e hash do bloco anterior. A
aplicação também deverá validar a integridade da cadeia e indicar quando algum
registro tiver sido alterado.

Na versão 0.1, foi criada a base da solução: o bloco gênese, o cálculo de hash
SHA-256, o encadeamento de blocos, a validação da cadeia e uma interface mínima
para visualizar essas informações.

## Tecnologias utilizadas

- **Python 3.12.10:** linguagem utilizada para implementar as regras da
  blockchain e organizar as estruturas do projeto.
- **Streamlit 1.62.0:** framework utilizado para criar a interface web
  interativa diretamente em Python.
- **hashlib:** módulo da biblioteca padrão do Python utilizado para gerar os
  hashes SHA-256 dos blocos.
- **dataclasses, datetime e json:** recursos da biblioteca padrão utilizados
  para modelar os blocos, registrar data e hora e padronizar os dados antes do
  cálculo do hash.
- **pytest 9.1.1:** ferramenta de testes automatizados utilizada para verificar
  a criação dos blocos, o encadeamento e a detecção de alterações.
- **Git:** sistema de controle de versão utilizado para registrar a evolução
  do código e do documento técnico.
- **Visual Studio Code:** ambiente utilizado para editar e executar o projeto.

## Arquitetura da aplicação

A aplicação foi organizada em partes com responsabilidades separadas:

- **`blockchain.py`:** contém a lógica principal. A classe `Bloco` representa
  cada registro, enquanto a classe `Blockchain` mantém a cadeia, adiciona
  blocos e verifica sua integridade.
- **`app.py`:** contém a interface Streamlit. Nesta versão, mostra a quantidade
  de blocos, o estado de validação e os dados do bloco gênese.
- **`tests/test_blockchain.py`:** reúne testes automatizados da lógica da cadeia.
- **`docs/`:** mantém o relatório técnico atualizado durante o desenvolvimento.

O fluxo básico começa na interface. A interface consulta o objeto `Blockchain`,
que mantém uma lista ordenada de objetos `Bloco`. Cada novo bloco recebe o hash
do bloco anterior, formando o encadeamento. Quando a validação é solicitada, a
aplicação recalcula os hashes e confere todas as ligações da cadeia.

## Conceitos de Blockchain aplicados

- **Bloco:** estrutura que reúne identificador, data e hora, dados, hash próprio
  e hash anterior.
- **Bloco gênese:** primeiro bloco da cadeia. Como não existe bloco anterior,
  ele utiliza o valor `0` no campo de hash anterior.
- **Hash:** resumo digital calculado a partir do conteúdo do bloco. Foi usado o
  algoritmo SHA-256. Uma pequena mudança nos dados produz um resultado
  diferente. O hash não é uma criptografia reversível.
- **Encadeamento:** cada bloco armazena o hash do bloco anterior. Essa ligação
  permite verificar a sequência dos registros.
- **Integridade:** a validação recalcula o hash de cada bloco e compara o
  resultado com o hash armazenado. Também confere se o hash anterior aponta
  corretamente para o bloco precedente.
- **Registro distribuído e ausência de autoridade única:** serão representados
  conceitualmente na versão final. A aplicação local simula o registro da
  cadeia, mas não implementa uma rede real de computadores independentes.

## Limitações da implementação

A solução é uma simulação educacional e não deve ser utilizada para operações
financeiras reais. Na versão atual, a cadeia funciona apenas na memória do
programa e é reiniciada quando a sessão é encerrada. Ainda não existem cadastro
de usuários, saldos, formulário de transações ou demonstração visual de
adulteração; esses recursos serão adicionados nas próximas etapas.

A aplicação também não implementa rede ponto a ponto, consenso entre nós,
mineração, prova de trabalho, prova de participação, carteiras criptográficas,
assinaturas digitais ou armazenamento permanente. Portanto, ela demonstra os
princípios de blocos, hashes e integridade, mas não possui o mesmo nível de
descentralização, segurança e disponibilidade de uma blockchain real.

## Referências técnicas consultadas

- Python Software Foundation. *hashlib — Secure hashes and message digests*.
  Disponível em: https://docs.python.org/3/library/hashlib.html
- Streamlit. *Streamlit API reference*. Disponível em:
  https://docs.streamlit.io/develop/api-reference
