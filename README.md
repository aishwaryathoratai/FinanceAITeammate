# 💼 Enterprise Finance AI Teammate

## Project Overview

Enterprise Finance AI Teammate is a **multi-agent Retrieval-Augmented Generation (RAG)** application designed to answer enterprise-related questions accurately using company documents.

The application automatically classifies user queries into different business domains using a **Supervisor Agent** and routes them to specialized agents. Each agent retrieves relevant information using **Hybrid Retrieval (FAISS + BM25)** before generating grounded responses with an LLM.

The system is built using **LangGraph**, demonstrating an enterprise-style multi-agent workflow with modular, maintainable components.

---

# Features

* Multi-Agent Architecture using LangGraph
* Supervisor Agent for intelligent routing
* Specialized Finance, Policy, and Support Agents
* Hybrid Retrieval (FAISS + BM25)
* Hugging Face Embeddings
* Streamlit User Interface
* Pydantic Input & Output Validation
* Source Attribution
* Performance Evaluation Script

---

# Project Architecture

```text
                   User
                     │
                     ▼
              Streamlit App
                     │
                     ▼
               LangGraph Graph
                     │
                     ▼
            Supervisor Agent
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
 Finance Agent  Policy Agent  Support Agent
      │              │              │
      └──────────────┼──────────────┘
                     ▼
            Hybrid Retriever
             (FAISS + BM25)
                     │
                     ▼
         Relevant Enterprise Documents
                     │
                     ▼
              ChatGroq-llama-3.3-70b-versatile
                     │
                     ▼
          Final Answer + Sources
```

---

# Folder Structure

```text
Finance_AI_Teammate/

├── app.py
├── graph.py
├── prompts.py
├── schemas.py
├── retriever.py
├── ingestion.py
├── create_embeddings.py
├── evaluation.py
├── test_questions.csv
├── requirements.txt
│
├── agents/
│   ├── base_agent.py
│   ├── supervisor.py
│   ├── finance_agent.py
│   ├── policy_agent.py
│   └── support_agent.py
│
├── data/
│
└── vectorstore/
```

---

# AI Stack

| Component             | Technology                             |
| --------------------- | -------------------------------------- |
| Programming Language  | Python                                 |
| Multi-Agent Framework | LangGraph                              |
| LLM                   | ChatGroq-llama-3.3-70b-versatile1-mini                           |
| Embedding Model       | sentence-transformers/all-MiniLM-L6-v2 |
| Vector Database       | FAISS                                  |
| Keyword Search        | BM25                                   |
| Retrieval Strategy    | Hybrid Retrieval                       |
| UI                    | Streamlit                              |
| Validation            | Pydantic                               |

---

# Multi-Agent Workflow

### Step 1

The user submits a question through the Streamlit interface.

Example:

> "How can I claim travel reimbursement?"

---

### Step 2

The Supervisor Agent classifies the query into one of three categories:

* Finance
* Policy
* Support

---

### Step 3

The selected agent receives the request.

Example:

Finance Agent

---

### Step 4

The agent retrieves relevant enterprise documents using Hybrid Retrieval.

* FAISS performs semantic search.
* BM25 performs keyword search.
* Results are combined before passing context to the LLM.

---

### Step 5

The retrieved context is inserted into a prompt template.

---

### Step 6

GPT-4.1-mini generates a grounded response.

---

### Step 7

The application returns:

* Final Answer
* Source Documents
* Selected Agent

---

# Hybrid Retrieval

This project combines two retrieval techniques.

## FAISS

Used for semantic similarity search.

Advantages:

* Fast
* Lightweight
* Excellent semantic understanding


## BM25

Used for keyword matching.

Advantages:

* Strong exact-term retrieval
* Complements vector search

---

## Why Hybrid Retrieval?

Using FAISS alone may miss exact keywords.

Using BM25 alone may miss semantic meaning.

Combining both retrieval methods improves document relevance and reduces hallucinations.

---

# Evaluation

The project includes an evaluation pipeline using **evaluation.py**.

Evaluation metrics include:

* Routing Accuracy
* Average Response Latency
* Retrieved Source Count

Sample evaluation dataset:

```text
How do I claim travel reimbursement?
Expected Agent → Finance

What is the leave policy?
Expected Agent → Policy

My VPN is not working.
Expected Agent → Support
```

---

# Cost Optimization

The following techniques are used to reduce inference cost:

* Lightweight embedding model (MiniLM)
* Hybrid Retrieval to improve retrieval precision
* Top-K document retrieval
* Shared BaseAgent implementation to eliminate duplicate logic
* Prompt templates to minimize token usage
* Temperature set to 0 for deterministic responses

---

# Security & Governance

* User input is validated using Pydantic.
* Responses are grounded using retrieved enterprise documents.
* Source documents are returned for transparency.
* API keys should be stored securely using environment variables in production.
* The modular architecture allows future integration of authentication and access control.

---

# Technologies Used

* Python
* LangGraph
* LangChain
* Groq
* Hugging Face
* FAISS
* BM25
* Streamlit
* Pydantic

---

# Installation

Clone the repository.

```bash
git clone <repository-url>
```
cd enterprise-finance-ai-teammate

```bash
Create a Virtual Environment

python -m venv .venv

.venv\Scripts\activate
```
Install dependencies.

```bash
pip install -r requirements.txt
```
Configure Environment Variables
```bash
Create a file named .env in the project root.

Example:

GROQ_API_KEY=your_groq_api_key_here

Replace your_groq_api_key_here with your actual Groq API key.
```
Prepare the Dataset
```bash
Place all enterprise documents inside the data/ folder.

Example:

data/

finance_policy.pdf

leave_policy.pdf

travel_policy.pdf

it_support.pdf

employee_handbook.pdf

finance.csv

The system supports:

PDF documents
CSV files
```
Generate embeddings.

```bash
python create_embeddings.py
```

Generate Embeddings
Run the application.

```

streamlit run app.py
```

Run evaluation.

```bash
python evaluation.py
```

---

# Sample Questions

### Finance

* How can I claim travel reimbursement?
* How do I submit an expense report?

### Policy

* What is the leave policy?
* Can I work from home?

### Support

* My VPN is not working.
* I forgot my laptop password.

---

# Future Improvements

* Add Human-in-the-Loop approval for sensitive requests.
* Integrate reranking models for improved retrieval.
* Add conversation memory.
* Support additional enterprise departments (HR, Legal, IT Operations).
* Add authentication and role-based access control.
* Deploy using Docker and cloud infrastructure.

---

# Conclusion

This project demonstrates an enterprise-ready Multi-Agent RAG system that combines LangGraph orchestration, Hybrid Retrieval, and Large Language Models to provide accurate, explainable, and domain-specific responses. The modular architecture allows easy extension with additional agents, making it suitable for real-world enterprise AI applications.
