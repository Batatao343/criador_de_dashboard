# 📊 Criador Automático de Dashboards com IA

Este projeto utiliza **CrewAI** para orquestrar agentes autônomos que transformam um arquivo de dados (.csv ou .xlsx) em um **dashboard interativo com Streamlit**, passando por etapas como limpeza de dados, análise, sugestão de visualizações, e geração de código Python.

---

## 🚀 Como Funciona

### 💡 Pipeline Inteligente com Agentes

O sistema utiliza múltiplos agentes, cada um com responsabilidades claras:

| Agente                  | Responsabilidade |
|------------------------|------------------|
| `data_cleaner_agent`   | Limpeza e tratamento dos dados (nulos, médias, etc.) |
| `insights_agent`       | Geração de insights e análise dos dados com RAG |
| `visualization_agent`  | Sugestão de visualizações ideais com base no dataset |
| `prompt_builder_agent` | Monta o prompt técnico com base nos insights e gráficos |
| `code_generation_agent`| Gera código Python com Streamlit para criar o dashboard |

