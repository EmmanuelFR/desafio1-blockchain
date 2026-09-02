"""Testes automatizados da lógica principal da blockchain."""

from blockchain import Blockchain


def test_cria_bloco_genese() -> None:
    blockchain = Blockchain()
    bloco_genese = blockchain.cadeia[0]

    assert len(blockchain.cadeia) == 1
    assert bloco_genese.indice == 0
    assert bloco_genese.hash_anterior == "0"
    assert bloco_genese.hash == bloco_genese.calcular_hash()


def test_adiciona_bloco_encadeado() -> None:
    blockchain = Blockchain()
    bloco_anterior = blockchain.cadeia[-1]

    novo_bloco = blockchain.adicionar_bloco({"operacao": "teste"})

    assert len(blockchain.cadeia) == 2
    assert novo_bloco.indice == 1
    assert novo_bloco.hash_anterior == bloco_anterior.hash


def test_valida_cadeia_sem_alteracoes() -> None:
    blockchain = Blockchain()
    blockchain.adicionar_bloco({"operacao": "teste"})

    cadeia_valida, _ = blockchain.validar_cadeia()

    assert cadeia_valida is True


def test_detecta_alteracao_em_um_bloco() -> None:
    blockchain = Blockchain()
    blockchain.adicionar_bloco({"valor": 10})
    blockchain.cadeia[1].dados["valor"] = 999

    cadeia_valida, mensagem = blockchain.validar_cadeia()

    assert cadeia_valida is False
    assert "bloco 1" in mensagem


def test_cria_carteiras_iniciais() -> None:
    blockchain = Blockchain()

    assert blockchain.moeda == "EDU"
    assert len(blockchain.carteiras) == 2

    assert blockchain.carteiras["CARTEIRA-001"]["usuario"] == "Emmanuel Freitas"
    assert blockchain.carteiras["CARTEIRA-001"]["saldo"] == 100

    assert blockchain.carteiras["CARTEIRA-002"]["usuario"] == "Weberson Rodrigues"
    assert blockchain.carteiras["CARTEIRA-002"]["saldo"] == 100


def test_valida_transacao_com_saldo_suficiente() -> None:
    blockchain = Blockchain()

    transacao_valida, mensagem = blockchain.validar_transacao(
        "CARTEIRA-001",
        "CARTEIRA-002",
        25,
    )

    assert transacao_valida is True
    assert mensagem == "Transação válida."


def test_rejeita_transacao_com_saldo_insuficiente() -> None:
    blockchain = Blockchain()

    transacao_valida, mensagem = blockchain.validar_transacao(
        "CARTEIRA-001",
        "CARTEIRA-002",
        150,
    )

    assert transacao_valida is False
    assert mensagem == "Saldo insuficiente."


def test_rejeita_transacao_com_origem_inexistente() -> None:
    blockchain = Blockchain()

    transacao_valida, mensagem = blockchain.validar_transacao(
        "CARTEIRA-999",
        "CARTEIRA-002",
        25,
    )

    assert transacao_valida is False
    assert mensagem == "Carteira de origem não encontrada."


def test_rejeita_transacao_com_destino_inexistente() -> None:
    blockchain = Blockchain()

    transacao_valida, mensagem = blockchain.validar_transacao(
        "CARTEIRA-001",
        "CARTEIRA-999",
        25,
    )

    assert transacao_valida is False
    assert mensagem == "Carteira de destino não encontrada."


def test_rejeita_transacao_para_a_mesma_carteira() -> None:
    blockchain = Blockchain()

    transacao_valida, mensagem = blockchain.validar_transacao(
        "CARTEIRA-001",
        "CARTEIRA-001",
        25,
    )

    assert transacao_valida is False
    assert mensagem == "As carteiras de origem e destino devem ser diferentes."


def test_rejeita_transacao_com_valor_zero() -> None:
    blockchain = Blockchain()

    transacao_valida, mensagem = blockchain.validar_transacao(
        "CARTEIRA-001",
        "CARTEIRA-002",
        0,
    )

    assert transacao_valida is False
    assert mensagem == "O valor da transação deve ser maior que zero."


def test_realiza_transacao_e_atualiza_saldos() -> None:
    blockchain = Blockchain()

    transacao_realizada, mensagem = blockchain.realizar_transacao(
        "CARTEIRA-001",
        "CARTEIRA-002",
        25,
    )

    assert transacao_realizada is True
    assert mensagem == "Transação realizada com sucesso."
    assert blockchain.carteiras["CARTEIRA-001"]["saldo"] == 75
    assert blockchain.carteiras["CARTEIRA-002"]["saldo"] == 125


def test_transacao_realizada_cria_bloco_encadeado() -> None:
    blockchain = Blockchain()
    bloco_anterior = blockchain.cadeia[-1]

    transacao_realizada, _ = blockchain.realizar_transacao(
        "CARTEIRA-001",
        "CARTEIRA-002",
        25,
    )

    novo_bloco = blockchain.cadeia[-1]
    cadeia_valida, _ = blockchain.validar_cadeia()

    assert transacao_realizada is True
    assert len(blockchain.cadeia) == 2
    assert novo_bloco.hash_anterior == bloco_anterior.hash
    assert novo_bloco.dados == {
        "tipo": "transacao",
        "carteira_origem": "CARTEIRA-001",
        "usuario_origem": "Emmanuel Freitas",
        "carteira_destino": "CARTEIRA-002",
        "usuario_destino": "Weberson Rodrigues",
        "valor": 25,
        "moeda": "EDU",
    }
    assert cadeia_valida is True


def test_transacao_rejeitada_nao_altera_saldos_nem_cria_bloco() -> None:
    blockchain = Blockchain()
    saldo_origem_inicial = blockchain.carteiras["CARTEIRA-001"]["saldo"]
    saldo_destino_inicial = blockchain.carteiras["CARTEIRA-002"]["saldo"]
    quantidade_blocos_inicial = len(blockchain.cadeia)

    transacao_realizada, mensagem = blockchain.realizar_transacao(
        "CARTEIRA-001",
        "CARTEIRA-002",
        150,
    )

    assert transacao_realizada is False
    assert mensagem == "Saldo insuficiente."
    assert blockchain.carteiras["CARTEIRA-001"]["saldo"] == saldo_origem_inicial
    assert blockchain.carteiras["CARTEIRA-002"]["saldo"] == saldo_destino_inicial
    assert len(blockchain.cadeia) == quantidade_blocos_inicial


def test_realiza_transacoes_nos_dois_sentidos() -> None:
    blockchain = Blockchain()

    primeira_transacao, _ = blockchain.realizar_transacao(
        "CARTEIRA-001",
        "CARTEIRA-002",
        25,
    )
    segunda_transacao, _ = blockchain.realizar_transacao(
        "CARTEIRA-002",
        "CARTEIRA-001",
        40,
    )

    saldo_total = sum(
        carteira["saldo"]
        for carteira in blockchain.carteiras.values()
    )
    cadeia_valida, _ = blockchain.validar_cadeia()

    assert primeira_transacao is True
    assert segunda_transacao is True
    assert blockchain.carteiras["CARTEIRA-001"]["saldo"] == 115
    assert blockchain.carteiras["CARTEIRA-002"]["saldo"] == 85
    assert saldo_total == 200
    assert len(blockchain.cadeia) == 3
    assert blockchain.cadeia[1].dados["carteira_origem"] == "CARTEIRA-001"
    assert blockchain.cadeia[2].dados["carteira_origem"] == "CARTEIRA-002"
    assert blockchain.cadeia[2].hash_anterior == blockchain.cadeia[1].hash
    assert cadeia_valida is True


def test_simula_adulteracao_e_invalida_cadeia() -> None:
    blockchain = Blockchain()
    blockchain.realizar_transacao(
        "CARTEIRA-001",
        "CARTEIRA-002",
        25,
    )
    hash_original = blockchain.cadeia[1].hash

    adulteracao_realizada, mensagem = blockchain.simular_adulteracao(
        1,
        999,
    )
    cadeia_valida, mensagem_validacao = blockchain.validar_cadeia()

    assert adulteracao_realizada is True
    assert mensagem == "Valor do bloco 1 alterado de 25 para 999 EDU."
    assert blockchain.cadeia[1].dados["valor"] == 999
    assert blockchain.cadeia[1].hash == hash_original
    assert blockchain.carteiras["CARTEIRA-001"]["saldo"] == 75
    assert blockchain.carteiras["CARTEIRA-002"]["saldo"] == 125
    assert cadeia_valida is False
    assert mensagem_validacao == "O conteúdo do bloco 1 foi alterado."


def test_rejeita_adulteracao_do_bloco_genese() -> None:
    blockchain = Blockchain()

    adulteracao_realizada, mensagem = blockchain.simular_adulteracao(
        0,
        999,
    )
    cadeia_valida, _ = blockchain.validar_cadeia()

    assert adulteracao_realizada is False
    assert mensagem == "Selecione um bloco de transação válido."
    assert cadeia_valida is True


def test_rejeita_adulteracao_com_valor_invalido() -> None:
    blockchain = Blockchain()
    blockchain.realizar_transacao(
        "CARTEIRA-001",
        "CARTEIRA-002",
        25,
    )

    adulteracao_realizada, mensagem = blockchain.simular_adulteracao(
        1,
        0,
    )
    cadeia_valida, _ = blockchain.validar_cadeia()

    assert adulteracao_realizada is False
    assert mensagem == "O novo valor deve ser maior que zero."
    assert blockchain.cadeia[1].dados["valor"] == 25
    assert cadeia_valida is True


def test_rejeita_adulteracao_sem_mudar_o_valor() -> None:
    blockchain = Blockchain()
    blockchain.realizar_transacao(
        "CARTEIRA-001",
        "CARTEIRA-002",
        25,
    )

    adulteracao_realizada, mensagem = blockchain.simular_adulteracao(
        1,
        25,
    )
    cadeia_valida, _ = blockchain.validar_cadeia()

    assert adulteracao_realizada is False
    assert mensagem == "O novo valor deve ser diferente do valor registrado."
    assert blockchain.cadeia[1].dados["valor"] == 25
    assert cadeia_valida is True
