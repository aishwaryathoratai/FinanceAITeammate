                    User
                      │
                      ▼
                FastAPI (main.py)
                      │
                      ▼
             LangGraph (graph.py)
                      │
                      ▼
             Supervisor Agent
          ┌────────┼─────────┐
          ▼        ▼         ▼
   Finance Agent Policy Agent Support Agent
          │        │         │
          └────────┼─────────┘
                   ▼
           Hybrid Retriever
      ┌────────┼─────────┐
      ▼        ▼         ▼
  ChromaDB   SQLite     CSV
                   │
                   ▼
                LLM (Groq/OpenAI)
                   │
                   ▼
              Answer + Sources