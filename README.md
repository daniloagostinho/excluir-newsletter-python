# Excluir E-mails em lote com Python

![Robô Excluir e-mails](https://raw.githubusercontent.com/daniloagostinho/excluir-emails-gmail-python/refs/heads/main/images/robot.png) | ![Python](https://raw.githubusercontent.com/daniloagostinho/excluir-emails-gmail-python/refs/heads/main/images/python.png) | ![Gmail](https://raw.githubusercontent.com/daniloagostinho/excluir-emails-gmail-python/refs/heads/main/images/gmail.png)

Este projeto permite excluir e-mails automaticamente do Gmail com base em uma lista de remetentes, fornecida manualmente ou através de uma planilha Excel. Ele utiliza a API do Gmail para realizar a autenticação e interações com a conta.

> **Nota:** Atualmente, na versão **1.0**, o suporte é limitado ao Gmail. Versões futuras incluirão suporte a outros provedores de e-mail.

## Recursos
- Autenticação segura utilizando OAuth2.
- Exclusão de e-mails com base em remetentes especificados.
- Carregamento de remetentes a partir de uma planilha Excel.
- Feedback visual amigável no terminal.

## Requisitos
Certifique-se de ter instalado:
- Python 3.10 ou superior
- Uma conta Google configurada para permitir o uso da API do Gmail

## Instalação

1. Clone o repositório:
   ```bash
   git clone git@github.com:daniloagostinho/excluir-emails-gmail-python.git
   cd excluir-emails-gmail-python
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure o arquivo `credentials.json`:
   - Acesse o [Google Cloud Console](https://console.cloud.google.com/).
   - Crie um projeto e ative a API do Gmail.
   - Gere credenciais do tipo "OAuth 2.0 Client ID" e baixe o arquivo `credentials.json`.
   - Coloque o arquivo na raiz do projeto.

4. Certifique-se de adicionar os seguintes escopos ao aplicativo:
   ```plaintext
   https://mail.google.com/
   ```

## Uso

1. Execute o script principal:
   ```bash
   python app.py
   ```

2. Escolha entre:
   - Fornecer uma lista de remetentes manualmente no código.
   - Carregar remetentes de uma planilha Excel com uma coluna chamada `Email`.

3. Siga as instruções no terminal para excluir os e-mails.

## Estrutura do Projeto

```
.
├── app.py                 # Script principal
├── requirements.txt       # Dependências do projeto
├── LICENSE                # Licença do projeto
├── README.md              # Documentação principal
├── token.json             # Token gerado após autenticação (adicionado ao .gitignore)
├── credentials.json       # Credenciais da API (adicionado ao .gitignore)
└── utils/
    └── helper.py          # Funções auxiliares (opcional)
```

## Contribuições

Contribuições são bem-vindas! Siga as instruções abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para suas alterações:
   ```bash
   git checkout -b minha-nova-feature
   ```
3. Faça commit das alterações:
   ```bash
   git commit -m "Adicionei uma nova feature"
   ```
4. Envie sua branch:
   ```bash
   git push origin minha-nova-feature
   ```
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Roadmap
- [ ] Adicionar suporte a etiquetas para classificação de e-mails antes da exclusão.
- [ ] Melhorar feedback visual no terminal com mais opções de UX.
- [ ] Adicionar suporte a múltiplas contas de Gmail.

## Problemas Conhecidos
- Apenas mensagens com permissões adequadas podem ser excluídas. Certifique-se de que o escopo `https://mail.google.com/` está configurado corretamente.
- Algumas mensagens podem não ser encontradas dependendo da sintaxe da consulta no Gmail.

## Contato
Caso tenha dúvidas ou problemas, entre em contato pelo e-mail [danilodev.silva@gmail.com](mailto:danilodev.silva@gmail.com).

