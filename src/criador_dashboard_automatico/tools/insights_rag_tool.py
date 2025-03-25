from crewai_tools import tool
import pandas as pd
import json
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import Document
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms import OpenAI

@tool("insights_rag_tool")
def insights_rag_tool(input: dict) -> str:
    """
    Gera insights a partir de um DataFrame limpo usando RAG com LlamaIndex.

    Espera como input:
    {
        "cleaned_dataframe_json": "<json-encoded dataframe>",
        "question": "Quais são os principais padrões nos dados?"
    }

    Retorna uma resposta textual com base na pergunta e nos dados fornecidos.
    """
    try:
        # Recupera o DataFrame limpo
        df_json = input.get("cleaned_dataframe_json")
        question = input.get("question")

        if not df_json or not question:
            return "Erro: 'cleaned_dataframe_json' e 'question' são obrigatórios."

        df = pd.read_json(df_json)

        # Converte cada linha do DataFrame em um pequeno documento textual
        docs = []
        for index, row in df.iterrows():
            text = f"Linha {index}: " + ", ".join([f"{col}: {val}" for col, val in row.items()])
            docs.append(Document(text=text))

        # Indexação e busca com LlamaIndex
        index = VectorStoreIndex.from_documents(docs)
        query_engine = index.as_query_engine()
        response = query_engine.query(question)

        return str(response)

    except Exception as e:
        return f"Erro ao processar os insights com RAG: {str(e)}"

