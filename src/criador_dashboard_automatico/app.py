import streamlit as st
import pandas as pd
import tempfile
import os

from criador_dashboard_automatico.main import run  # ajuste se necessário

from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Criador Automático de Dashboards", layout="wide")
st.title("📊 Criador Automático de Dashboard com IA")

st.markdown("Faça upload de um arquivo `.csv` ou `.xlsx`, e a IA vai gerar insights, sugestões de visualização e o código de um dashboard interativo usando Streamlit.")

uploaded_file = st.file_uploader("📁 Upload do arquivo", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        # Mostrar preview do DataFrame
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Formato não suportado. Envie um arquivo CSV ou XLSX.")
            st.stop()

        st.subheader("👀 Prévia dos Dados")
        st.dataframe(df.head())

        # Salvar arquivo temporariamente
        with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name[-5:]) as tmp_file:
            tmp_file.write(uploaded_file.read())
            file_path = tmp_file.name

        # Botão para gerar código com CrewAI
        if st.button("🚀 Gerar Dashboard com IA"):
            with st.spinner("Executando pipeline com agentes..."):
                result = run(file_path)

            st.subheader("📄 Código Python Gerado")
            if isinstance(result, str):
                st.code(result, language="python")

                # Botão de execução protegida
                if st.button("▶️ Executar o Dashboard Gerado"):
                    try:
                        local_env = {}
                        exec(result, {}, local_env)
                    except Exception as e:
                        st.error(f"Erro ao executar o código: {e}")

                # Botão para download
                st.download_button(
                    label="💾 Baixar código como .py",
                    data=result,
                    file_name="dashboard_gerado.py",
                    mime="text/x-python"
                )
            else:
                st.warning("O resultado não foi um código. Resultado bruto exibido abaixo:")
                st.json(result)

    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")
