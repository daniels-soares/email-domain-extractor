import re

def carregar_emails_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            return [linha.strip() for linha in f if linha.strip()]  # Remove linhas vazias e espaços
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        exit()

def domain_extractor(emails):
    dominios = set()
    for email in emails:
        match_value = re.search(r'@([a-zA-Z0-9._-]+)', email)
        if match_value:
            dominios.add(match_value.group(1))
    return dominios

# Carrega os e-mails do arquivo
mail_list = carregar_emails_arquivo("mail_list.txt")

# Extrai os domínios
extractor = domain_extractor(mail_list)

# Salva os domínios em um novo arquivo
with open("Domínios extraídos.txt", "w", encoding="utf-8") as f:
    for dominio in sorted(extractor):
        f.write(dominio + "\n")
