import sqlite3
from langchain_core.documents import Document

def load_expenses(db_file:str):

    documents=[]
    conn=sqlite3.connect(db_file)
    cursor=conn.cursor()
    cursor.execute(""" select expense_id,employee_id,amount,status from expenses""")
    rows=cursor.fetchall()
    conn.close()
    for row in rows:
        text=f"""Expense ID: {row[0]}
    Employee: {row[1]}
    Amount: {row[2]}
    Status: {row[3]}"""
        documents.append(Document(page_content=text, metadata={
            "source": "finance.db",
            "type": "expense"
        }))
    return documents

print("Expenses loaded.")