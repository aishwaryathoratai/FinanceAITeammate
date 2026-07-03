import csv
from langchain_core.documents import Document

def load_emails(csv_file:str):
    documents=[]
    with open(csv_file, mode="r",encoding="utf-8") as file:
        reader=csv.DictReader(file)
        for row in reader:
            text =f"""Sender: {row['sender']},
            Receiver: {row['receiver']},
            Subject: {row['subject']},
            Body: {row['body']}
            """
        
            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": "emails.csv",
                        "email_id": row["email_id"],
                        "type": "email"
                    }
                )
            )
    return documents  

print("Emails loaded.")  