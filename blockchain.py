"""Lógica principal da blockchain educacional.

Esta implementação foi criada para fins acadêmicos. Ela demonstra blocos,
hashes, encadeamento e validação de integridade, sem tentar reproduzir toda a
infraestrutura de uma blockchain pública real.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib
import json
from typing import Any


@dataclass
class Bloco:
    """Representa um registro individual da cadeia."""

    indice: int
    data_hora: str
    dados: dict[str, Any]
    hash_anterior: str
    hash: str = ""

    @classmethod
    def criar(
        cls,
        indice: int,
        dados: dict[str, Any],
        hash_anterior: str,
    ) -> "Bloco":
        """Cria um bloco e calcula seu hash inicial."""

        bloco = cls(
            indice=indice,
            data_hora=datetime.now(timezone.utc).isoformat(),
            dados=dados,
            hash_anterior=hash_anterior,
        )
        bloco.hash = bloco.calcular_hash()
        return bloco

    def calcular_hash(self) -> str:
        """Calcula o SHA-256 do conteúdo que identifica o bloco."""

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

    def para_dicionario(self) -> dict[str, Any]:
        """Converte o bloco em dicionário para exibição na interface."""

        return asdict(self)


class Blockchain:
    """Mantém a cadeia de blocos e verifica sua integridade."""

    def __init__(self) -> None:
        self.cadeia: list[Bloco] = [self._criar_bloco_genese()]
        self.moeda = "EDU"
        self.carteiras: dict[str, dict[str, str | int]] = {
            "CARTEIRA-001": {
                "usuario": "Emmanuel Freitas",
                "saldo": 100,
            },
            "CARTEIRA-002": {
                "usuario": "Weberson Rodrigues",
                "saldo": 100,
            },
        }

    @staticmethod
    def _criar_bloco_genese() -> Bloco:
        """Cria o primeiro bloco da cadeia, chamado bloco gênese."""

        return Bloco.criar(
            indice=0,
            dados={"mensagem": "Início da blockchain educacional"},
            hash_anterior="0",
        )

    def adicionar_bloco(self, dados: dict[str, Any]) -> Bloco:
        """Adiciona um bloco ligado ao hash do bloco anterior."""

        bloco_anterior = self.cadeia[-1]
        novo_bloco = Bloco.criar(
            indice=len(self.cadeia),
            dados=dados,
            hash_anterior=bloco_anterior.hash,
        )
        self.cadeia.append(novo_bloco)
        return novo_bloco

    def validar_transacao(
        self,
        origem: str,
        destino: str,
        valor: int,
    ) -> tuple[bool, str]:
        """Verifica se uma transação pode ser realizada."""

        if origem not in self.carteiras:
            return False, "Carteira de origem não encontrada."

        if destino not in self.carteiras:
            return False, "Carteira de destino não encontrada."

        if origem == destino:
            return False, "As carteiras de origem e destino devem ser diferentes."

        if valor <= 0:
            return False, "O valor da transação deve ser maior que zero."

        saldo_origem = self.carteiras[origem]["saldo"]
        if saldo_origem < valor:
            return False, "Saldo insuficiente."

        return True, "Transação válida."

    def realizar_transacao(
        self,
        origem: str,
        destino: str,
        valor: int,
    ) -> tuple[bool, str]:
        """Valida a operação e transfere EDU entre duas carteiras."""

        transacao_valida, mensagem = self.validar_transacao(
            origem,
            destino,
            valor,
        )
        if not transacao_valida:
            return False, mensagem

        self.carteiras[origem]["saldo"] -= valor
        self.carteiras[destino]["saldo"] += valor

        dados_transacao = {
            "tipo": "transacao",
            "carteira_origem": origem,
            "usuario_origem": self.carteiras[origem]["usuario"],
            "carteira_destino": destino,
            "usuario_destino": self.carteiras[destino]["usuario"],
            "valor": valor,
            "moeda": self.moeda,
        }
        self.adicionar_bloco(dados_transacao)

        return True, "Transação realizada com sucesso."

    def simular_adulteracao(
        self,
        indice: int,
        novo_valor: int,
    ) -> tuple[bool, str]:
        """Altera um valor registrado sem recalcular o hash do bloco."""

        if indice <= 0 or indice >= len(self.cadeia):
            return False, "Selecione um bloco de transação válido."

        bloco = self.cadeia[indice]
        if bloco.dados.get("tipo") != "transacao":
            return False, "O bloco selecionado não contém uma transação."

        if novo_valor <= 0:
            return False, "O novo valor deve ser maior que zero."

        valor_original = bloco.dados["valor"]
        if novo_valor == valor_original:
            return False, "O novo valor deve ser diferente do valor registrado."

        bloco.dados["valor"] = novo_valor

        return True, (
            f"Valor do bloco {indice} alterado de {valor_original} "
            f"para {novo_valor} {self.moeda}."
        )

    def validar_cadeia(self) -> tuple[bool, str]:
        """Valida os hashes armazenados e as ligações entre os blocos."""

        for posicao, bloco in enumerate(self.cadeia):
            if bloco.hash != bloco.calcular_hash():
                return False, f"O conteúdo do bloco {bloco.indice} foi alterado."

            if posicao > 0:
                bloco_anterior = self.cadeia[posicao - 1]
                if bloco.hash_anterior != bloco_anterior.hash:
                    return False, f"A ligação do bloco {bloco.indice} está inválida."

        return True, "Todos os hashes e encadeamentos estão válidos."

    def para_lista(self) -> list[dict[str, Any]]:
        """Retorna todos os blocos em formato adequado para apresentação."""

        return [bloco.para_dicionario() for bloco in self.cadeia]
