import os
import pandas as pd
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from rich.console import Console
from rich.progress import Progress, SpinnerColumn
from rich.prompt import Confirm, Prompt

# Configurando console Rich para feedback visual
console = Console()

# Escopos necessários para acesso ao Gmail
SCOPES = ['https://mail.google.com/']

def authenticate_gmail():
    """Autentica com a API do Gmail e retorna o serviço."""
    creds = None
    
    # Remove o token.json se existir para forçar uma nova autenticação
    if os.path.exists('token.json'):
        os.remove('token.json')
    
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

def get_newsletter_emails(service):
    """Recupera e-mails de newsletters paginadamente."""
    query = 'category:promotions OR "unsubscribe"'
    messages = []
    page_token = None
    
    with Progress(SpinnerColumn(), console=console) as progress:
        task = progress.add_task("[cyan]Buscando newsletters...", total=None)
        while True:
            results = service.users().messages().list(userId='me', q=query, maxResults=50, pageToken=page_token).execute()
            messages.extend(results.get('messages', []))
            page_token = results.get('nextPageToken', None)
            if not page_token:
                break
        progress.stop()
    
    return messages

def unsubscribe_and_delete_emails(service):
    """Lista newsletters paginadamente e permite ao usuário excluir aos poucos."""
    console.rule("[bold blue]Procurando newsletters e e-mails promocionais")
    messages = get_newsletter_emails(service)
    
    total_newsletters = len(messages)
    with Progress(SpinnerColumn(), console=console) as progress:
        task = progress.add_task("[cyan]Carregando e-mails para exclusão...", total=None)
        progress.stop()
    
    console.print(f"[bold green]Foram encontrados {total_newsletters} e-mails de newsletters.")
    
    if not Confirm.ask("Deseja começar a excluí-los?"):
        return
    
    page_token = None
    while True:
        senders = {}
        for message in messages[:50]:  # Processa 50 por vez
            msg_id = message['id']
            msg_data = service.users().messages().get(userId='me', id=msg_id, format='metadata', metadataHeaders=['From']).execute()
            sender = next((header['value'] for header in msg_data['payload']['headers'] if header['name'] == 'From'), None)
            if sender:
                senders[sender] = senders.get(sender, []) + [msg_id]
        
        for sender, msg_ids in senders.items():
            if Confirm.ask(f"Deseja se desinscrever e excluir {len(msg_ids)} e-mails de {sender}?"):
                console.print(f"[cyan]Desinscrevendo e apagando e-mails de {sender}...")
                
                with Progress() as progress:
                    task = progress.add_task("[red]Apagando...", total=len(msg_ids))
                    for msg_id in msg_ids:
                        service.users().messages().delete(userId='me', id=msg_id).execute()
                        progress.advance(task)
                
                console.print(f"[bold green]Os e-mails de {sender} foram excluídos.")
            else:
                console.print(f"[bold yellow]Os e-mails de {sender} não foram apagados.")
        
        messages = messages[50:]  # Remove os 50 processados
        if not messages or not Confirm.ask("Deseja continuar vendo mais newsletters?"):
            break

def main():
    # Autentica no Gmail
    service = authenticate_gmail()
    
    # Processa newsletters e opções de exclusão
    unsubscribe_and_delete_emails(service)

if __name__ == '__main__':
    main()
