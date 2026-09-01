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
