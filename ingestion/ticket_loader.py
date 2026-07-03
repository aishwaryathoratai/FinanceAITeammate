import csv
from langchain_core.documents import Document

def load_tickets(csv_file:str):
    documents=[]
    with open(csv_file, mode="r", encoding= "utf-8") as file:
        for row in csv.DictReader(file):
            text=f"""
            Issue:
            {row['issue']}
            Resolution:
            {row['resolution']}
            Status:
            {row['status']}
            """
            documents.append(Document(page_content=text,metadata={"source": "support_tickets.csv","ticket_id":row["ticket_id"],"type":"ticket "}))
    return documents
print("tickets loaded.")
