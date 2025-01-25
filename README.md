# Gerenciador de Newsletters com Python

![Automação de E-mails](https://raw.githubusercontent.com/daniloagostinho/excluir-emails-gmail-python/refs/heads/main/images/robot.png) | ![Python](https://raw.githubusercontent.com/daniloagostinho/excluir-emails-gmail-python/refs/heads/main/images/python.png) | ![Gmail](https://raw.githubusercontent.com/daniloagostinho/excluir-emails-gmail-python/refs/heads/main/images/gmail.png)

Este projeto permite **listar, se desinscrever e excluir automaticamente** e-mails de newsletters no Gmail. Ele utiliza a API do Gmail para identificar e processar inscrições em listas de e-mails promocionais.

> **Nota:** Atualmente, na versão **1.0**, o suporte é limitado ao Gmail. Versões futuras incluirão suporte a outros provedores de e-mail.

# Preview

![Preview](https://github.com/daniloagostinho/excluir-newsletter-python/blob/main/images/Preview.gif)

## Recursos
- Autenticação segura utilizando OAuth2.
- Identificação automática de newsletters e e-mails promocionais.
- Opção de desinscrição automática antes da exclusão.
- Exclusão seletiva ou em massa de newsletters.
- Feedback visual amigável no terminal.

## Requisitos
Certifique-se de ter instalado:
- Python 3.10 ou superior
- Uma conta Google configurada para permitir o uso da API do Gmail

## Instalação

1. Clone o repositório:
   ```bash
   git clone git@github.com:daniloagostinho/gerenciador-newsletters-python.git
   cd gerenciador-newsletters-python
   ```

2. Instale as dependências com pip:
   ```bash
   pip install -r requirements.txt
   ```

   2. Instale as dependências com conda:
   ```bash
   conda install pandas requests
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
   - **Excluir todas as newsletters de uma vez**
   - **Visualizar as inscrições e selecionar quais remover**

3. O script tentará **se desinscrever automaticamente** das newsletters antes de excluí-las.

4. Siga as instruções no terminal para concluir o processo.

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
- [ ] Melhorar o reconhecimento automático de links de desinscrição.
- [ ] Adicionar suporte a etiquetas para classificar e-mails antes da exclusão.
- [ ] Melhorar feedback visual no terminal com mais opções de UX.
- [ ] Adicionar suporte a múltiplas contas de Gmail.

## Problemas Conhecidos
- Apenas mensagens com permissões adequadas podem ser excluídas. Certifique-se de que o escopo `https://mail.google.com/` está configurado corretamente.
- Alguns links de desinscrição podem exigir interação manual.

## Contato
Caso tenha dúvidas ou problemas, entre em contato pelo e-mail [danilodev.silva@gmail.com](mailto:danilodev.silva@gmail.com).
