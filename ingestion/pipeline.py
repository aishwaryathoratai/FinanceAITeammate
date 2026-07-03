from .pdf_loader import load_pdfs
from .email_loader import load_emails
from .ticket_loader import load_tickets
from .finance_expense_loader import load_expenses
from .normalize import normalize_docs

def run_ingestion():

    pdf_docs=load_pdfs("data/pdfs")
    email_docs= load_emails("data/csv/emails.csv")
    ticket_docs= load_tickets("data/csv/support_tickets.csv")
    expense_docs= load_expenses("data/finance.db")
    documents=normalize_docs(pdf_docs,
                   email_docs,
                   expense_docs,
                   ticket_docs)
    return documents

print("Ingestion completed.")