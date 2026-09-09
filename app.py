"""Interface da blockchain educacional construída com Streamlit."""

from datetime import datetime, timedelta, timezone
from pathlib import Path

import streamlit as st

from blockchain import Blockchain

CAMINHO_ESTILOS = (
    Path(__file__).resolve().parent
    / ".streamlit"
    / "styles.css"
)

FUSO_HORARIO_BRASILIA = timezone(
    timedelta(hours=-3),
    name="BRT",
)

def carregar_estilos() -> None:
    """Carrega os estilos visuais da interface."""

    estilos = CAMINHO_ESTILOS.read_text(encoding="utf-8")
    st.markdown(
        f"<style>{estilos}</style>",
        unsafe_allow_html=True,
    )

def formatar_data_hora_brasilia(data_hora_utc: str) -> str:
    """Converte uma data UTC para o formato brasileiro e horário de Brasília."""

    data_hora = datetime.fromisoformat(data_hora_utc)
    data_hora_brasilia = data_hora.astimezone(FUSO_HORARIO_BRASILIA)

    return data_hora_brasilia.strftime("%d/%m/%Y às %H:%M:%S")

st.set_page_config(
    page_title="Blockchain Educacional",
    page_icon="🔗",
    layout="wide",
)

carregar_estilos()

if "blockchain" not in st.session_state:
    st.session_state.blockchain = Blockchain()

blockchain: Blockchain = st.session_state.blockchain

st.title("Blockchain Educacional")

rotulos_carteiras = {
    identificador: f"{carteira['usuario']} ({identificador})"
    for identificador, carteira in blockchain.carteiras.items()
}
identificadores_carteiras = list(rotulos_carteiras)

st.subheader("Nova transação")

with st.form("formulario_transacao"):
    origem = st.selectbox(
        "Carteira de origem",
        identificadores_carteiras,
        format_func=rotulos_carteiras.get,
    )
    destino = st.selectbox(
        "Carteira de destino",
        identificadores_carteiras,
        index=1,
        format_func=rotulos_carteiras.get,
    )
    valor = st.number_input(
        f"Valor ({blockchain.moeda})",
        value=1,
        step=1,
    )
    enviar_transacao = st.form_submit_button(
        "Realizar transação",
        type="primary",
    )

if enviar_transacao:
    transacao_realizada, mensagem_transacao = blockchain.realizar_transacao(
        origem,
        destino,
        valor,
    )
    if transacao_realizada:
        st.success(mensagem_transacao)
    else:
        st.error(mensagem_transacao)

st.subheader("Demonstração de adulteração")

blocos_transacao = [
    bloco
    for bloco in blockchain.cadeia
    if bloco.dados.get("tipo") == "transacao"
]

if blocos_transacao:
    indices_blocos = [bloco.indice for bloco in blocos_transacao]

    with st.form("formulario_adulteracao"):
        indice_adulterado = st.selectbox(
            "Bloco que será adulterado",
            indices_blocos,
            format_func=lambda indice: f"Bloco {indice}",
        )
        novo_valor_adulterado = st.number_input(
            f"Novo valor registrado ({blockchain.moeda})",
            value=999,
            step=1,
        )
        enviar_adulteracao = st.form_submit_button(
            "Simular adulteração",
        )

    if enviar_adulteracao:
        adulteracao_realizada, mensagem_adulteracao = (
            blockchain.simular_adulteracao(
                indice_adulterado,
                novo_valor_adulterado,
            )
        )
        if adulteracao_realizada:
            st.warning(mensagem_adulteracao)
        else:
            st.error(mensagem_adulteracao)
else:
    st.markdown("Disponível após o registro de uma transação.")

if st.button(
    "Reiniciar demonstração",
    help=(
        "Descarta os blocos e saldos atuais desta sessão e restaura "
        "o estado inicial."
    ),
):
    st.session_state.blockchain = Blockchain()
    st.rerun()

cadeia_valida, mensagem_validacao = blockchain.validar_cadeia()

coluna_blocos, coluna_status = st.columns(2)
with coluna_blocos:
    st.metric("Quantidade de blocos", len(blockchain.cadeia))
with coluna_status:
    st.metric("Integridade da cadeia", "Válida" if cadeia_valida else "Inválida")

if not cadeia_valida:
    st.error(mensagem_validacao)

st.subheader("Carteiras educacionais")

colunas_carteiras = st.columns(
    len(blockchain.carteiras),
    gap="medium",
)

for coluna, (identificador, carteira) in zip(
    colunas_carteiras,
    blockchain.carteiras.items(),
):
    with coluna.container(border=True):
        st.markdown(f"**{carteira['usuario']}**")
        st.markdown(f"Carteira: `{identificador}`")
        st.metric(
            "Saldo disponível",
            f"{carteira['saldo']} {blockchain.moeda}",
        )

st.subheader("Blocos registrados")

quantidade_blocos = len(blockchain.cadeia)

for bloco in blockchain.cadeia:
    tipo_bloco = (
        "Gênese"
        if bloco.indice == 0
        else "Transação"
    )
    bloco_mais_recente = bloco.indice == quantidade_blocos - 1
    titulo_bloco = f"Bloco {bloco.indice} - {tipo_bloco}"

    with st.expander(
        titulo_bloco,
        expanded=bloco_mais_recente,
    ):
        data_hora_formatada = formatar_data_hora_brasilia(
            bloco.data_hora
        )

        st.markdown(
            f"**Data e hora (Brasília):** {data_hora_formatada}"
        )

        st.markdown("**Hash anterior**")
        st.code(
            bloco.hash_anterior,
            language=None,
        )

        st.markdown("**Hash do bloco**")
        st.code(
            bloco.hash,
            language=None,
        )

        st.markdown("**Dados armazenados**")
        st.json(bloco.dados)
