# Email Domain Extractor 🛡️

Este script em Python carrega uma lista de e-mails e extrai todos os domínios únicos encontrados. Ideal para quem deseja realizar análises de segurança, investigar possíveis tentativas de phishing, ou simplesmente organizar uma lista de domínios em campanhas de e-mail.

### 💡 Aplicações:
- **Análise de campanhas de phishing**: Identifique rapidamente domínios falsos ou suspeitos.
- **Inteligência de ameaças**: Extraia domínios para enriquecer suas pesquisas de segurança.
- **Verificação de domínios**: Crie uma lista de domínios única a partir de uma lista de e-mails.

### ✅ O que o script faz, resumidamente:

- Lê um arquivo de e-mails (mail_list.txt).
- Remove linhas vazias e espaços.
- Extrai os domínios de cada e-mail com uma expressão regular.
- Remove duplicatas (usando set()).
- Salva os domínios únicos em um arquivo de saída (Domínios extraídos.txt), em ordem alfabética.

### 🛠️ Como usar:
1. Crie um arquivo chamado `mail_list.txt` com um e-mail por linha.
2. Execute o script para extrair os domínios:
   `python domain_extractor.py`

### 📄 Exemplo de entrada (mail_list.txt):
<img width="278" height="70" alt="image" src="https://github.com/user-attachments/assets/e88de5b3-ed0d-4e5f-ad72-b7ad9988b90a" />

### 📂 Saída gerada (Domínios extraídos.txt):

<img width="261" height="71" alt="image" src="https://github.com/user-attachments/assets/3f7b67d8-209e-4582-833f-640693ac79b6" />


### 📌 Requisitos:

- Python 3.6 ou superior
- Nenhuma biblioteca externa necessária


