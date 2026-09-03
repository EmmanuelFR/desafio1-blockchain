"""Interface da blockchain educacional construída com Streamlit."""

from datetime import datetime, timedelta, timezone

import streamlit as st

from blockchain import Blockchain

FUSO_HORARIO_BRASILIA = timezone(
    timedelta(hours=-3),
    name="BRT",
)


def formatar_data_hora_brasilia(data_hora_utc: str) -> str:
    """Converte uma data UTC para o formato brasileiro e horário de Brasília."""

    data_hora = datetime.fromisoformat(data_hora_utc)
    data_hora_brasilia = data_hora.astimezone(FUSO_HORARIO_BRASILIA)

    return data_hora_brasilia.strftime("%d/%m/%Y às %H:%M:%S")

st.set_page_config(
    page_title="Blockchain Educacional",
    page_icon="⛓️",
    layout="wide",
)

st.markdown(
    """
    <style>
    @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap");

    .stApp {
    font-family: "Roboto", sans-serif !important;
}

.stApp *:not([data-testid="stIconMaterial"]):not(.material-symbols-rounded) {
    font-family: "Roboto", sans-serif !important;
}

/* Mantém a fonte específica dos ícones */
[data-testid="stIconMaterial"],
.material-symbols-rounded {
    font-family: "Material Symbols Rounded" !important;
    font-style: normal !important;
    font-weight: normal !important;
    font-variation-settings:
        "FILL" 0,
        "wght" 400,
        "GRAD" 0,
        "opsz" 24;
}

    /* Rótulos dos campos */
[data-testid="stWidgetLabel"] p {
    color: #0F172A !important;
    font-weight: 500 !important;
}

    /* Contorno externo dos formulários */
    [data-testid="stForm"] {
        border: 1px solid #CBD5E1 !important;
    }

    /* Contornos dos campos de seleção e valor */
    [data-baseweb="select"] > div,
    [data-testid="stNumberInput"] [data-baseweb="input"] {
        border: 1px solid #64748B !important;
    }

    /* Realce do campo durante a interação */
    [data-baseweb="select"] > div:focus-within,
    [data-testid="stNumberInput"] [data-baseweb="input"]:focus-within {
        border-color: #2563EB !important;
        box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.20) !important;
    }

    /* Botão principal */
    [data-testid="stFormSubmitButton"] button {
        background-color: #2563EB !important;
        border-color: #2563EB !important;
        color: #FFFFFF !important;
        font-weight: 500 !important;
    }

    [data-testid="stFormSubmitButton"] button p {
        color: #FFFFFF !important;
    }

    /* Retorno visual ao posicionar o cursor */
    [data-testid="stFormSubmitButton"] button:hover {
        background-color: #1D4ED8 !important;
        border-color: #1D4ED8 !important;
        color: #FFFFFF !important;
    }

    /* Retorno visual ao usar teclado */
    [data-testid="stFormSubmitButton"] button:focus {
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.28) !important;
    }

    /* Retorno visual durante o clique */
    [data-testid="stFormSubmitButton"] button:active {
        background-color: #1E40AF !important;
        border-color: #1E40AF !important;
    }

    /* Texto das mensagens de alerta */
[data-testid="stAlert"] p {
    font-weight: 500 !important;
}

/* Botão secundário de reinício */
[data-testid="stButton"] button {
    background-color: #E2E8F0 !important;
    border: 1px solid #94A3B8 !important;
    color: #1E293B !important;
    font-weight: 500 !important;
}

[data-testid="stButton"] button p {
    color: #1E293B !important;
}

[data-testid="stButton"] button:hover {
    background-color: #CBD5E1 !important;
    border-color: #64748B !important;
    color: #0F172A !important;
}

[data-testid="stButton"] button:focus {
    border-color: #2563EB !important;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.22) !important;
}

[data-testid="stButton"] button:active {
    background-color: #94A3B8 !important;
}

/* Valores textuais exibidos nos dados JSON dos blocos */
[data-testid="stJson"] .string-value,
.string-value {
    color: #6D28D9 !important;
}
    </style>
    """,
    unsafe_allow_html=True,
)

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
        min_value=1,
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
            min_value=1,
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
