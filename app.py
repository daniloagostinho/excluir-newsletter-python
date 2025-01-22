import os
import pandas as pd
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Escopos necessários para acesso ao Gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def authenticate_gmail():
    """Autentica com a API do Gmail e retorna o serviço."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)
        # Salva as credenciais
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def delete_emails_from_senders(service, senders):
    """Deleta e-mails de uma lista de remetentes."""
    for sender in senders:
        print(f"Procurando e-mails de: {sender}")
        # Pesquisa e-mails do remetente
        query = f'from:{sender}'
        results = service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])
        
        if not messages:
            print(f"Nenhum e-mail encontrado de {sender}")
            continue
        
        # Deleta os e-mails encontrados
        for message in messages:
            msg_id = message['id']
            service.users().messages().delete(userId='me', id=msg_id).execute()
        print(f"E-mails de {sender} foram excluídos.")

def load_senders_from_excel(file_path):
    """Carrega a lista de remetentes de uma planilha Excel."""
    df = pd.read_excel(file_path)
    return df['Email'].tolist()

def main():
    # Autentica no Gmail
    service = authenticate_gmail()

    # Opção 1: Lista de remetentes manual
    senders = ['noreply@voeazul-news.com.br']

    # Opção 2: Carregar remetentes de uma planilha Excel
    # senders = load_senders_from_excel('remetentes.xlsx')

    # Deleta os e-mails
    delete_emails_from_senders(service, senders)

if __name__ == '__main__':
    main()
