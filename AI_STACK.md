                    AI Stack

             ┌────────────────────┐
             │    Streamlit UI     │
             └────────────────────┘
                       │
                       ▼
             ┌────────────────────┐
             │     LangGraph      │
             └────────────────────┘
                       │
             ┌─────────┼──────────┐
             ▼         ▼          ▼
        Finance     Policy    Support
          Agent      Agent      Agent
             │
             ▼
       BaseAgent (RAG)
             │
             ▼
     Hybrid Retriever
   (FAISS + BM25)
             │
             ▼
      MiniLM Embeddings
             │
             ▼
      ChatGroq-llama-3.3-70b-versatile
             │
             ▼
      Final Response