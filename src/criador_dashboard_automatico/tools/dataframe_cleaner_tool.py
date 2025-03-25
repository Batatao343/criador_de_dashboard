from crewai_tools import tool
import pandas as pd
import json

@tool("dataframe_cleaner_tool")
def dataframe_cleaner_tool(input: dict) -> str:
    """
    Cleans a DataFrame passed as JSON string.
    Removes columns with all NaNs, imputes missing values (mean for numeric, mode for categorical),
    and returns a summary with the cleaned DataFrame in JSON format.
    
    Expected input:
    {
        "dataframe_json": "<json-encoded DataFrame>"
    }
    """
    try:
        # Recupera o DataFrame
        df = pd.read_json(input["dataframe_json"])
        original_shape = df.shape

        # Contadores para o log
        dropped_columns = []
        imputed_columns = []

        # Remove colunas completamente vazias
        for col in df.columns:
            if df[col].isnull().all():
                dropped_columns.append(col)
        df = df.drop(columns=dropped_columns)

        # Imputação simples
        for col in df.columns:
            if df[col].isnull().sum() > 0:
                if pd.api.types.is_numeric_dtype(df[col]):
                    df[col].fillna(df[col].mean(), inplace=True)
                else:
                    df[col].fillna(df[col].mode()[0], inplace=True)
                imputed_columns.append(col)

        summary = {
            "original_shape": original_shape,
            "final_shape": df.shape,
            "dropped_columns": dropped_columns,
            "imputed_columns": imputed_columns,
        }

        return json.dumps({
            "summary": summary,
            "cleaned_dataframe_json": df.to_json()
        })

    except Exception as e:
        return f"Erro ao limpar DataFrame: {str(e)}"

