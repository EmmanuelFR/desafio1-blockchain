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
