#!/bin/bash

# Cores para o terminal (Duck Style)
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}[*] Iniciando configuração DUCK GREEN Framework v1.0...${NC}"

# 1. Atualizar e instalar dependências do Linux
echo -e "${GREEN}[*] Verificando dependências do Kali Linux...${NC}"
sudo apt update && sudo apt install wine wine64 python3 python3-pip wget -y

# 2. Configurar o Python de Windows dentro do Wine
echo -e "${GREEN}[*] Preparando ambiente de compilação Windows (Wine)...${NC}"

# Descarrega o instalador oficial do Python para Windows
if [ ! -f "python_installer.exe" ]; then
    echo -e "${BLUE}[*] A descarregar instalador do Python 3.10 para Windows...${NC}"
    wget https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe -O python_installer.exe
fi

echo -e "${YELLOW}[!] ATENÇÃO: Uma janela de instalação vai abrir via Wine.${NC}"
echo -e "${YELLOW}[!] 1. MARCA a caixa 'Add Python 3.10 to PATH' (Obrigatório!)${NC}"
echo -e "${YELLOW}[!] 2. Clica em 'Install Now'.${NC}"
echo -e "${YELLOW}[!] 3. Quando terminar, fecha a janela do instalador.${NC}"

wine python_installer.exe

# 3. Instalar bibliotecas de hacking dentro do ambiente Wine
echo -e "${GREEN}[*] Instalando bibliotecas no ambiente virtual Windows...${NC}"
# Nota: Usamos 'wine python' para garantir que o pip instale no local correto do Wine
wine python -m pip install --upgrade pip
wine python -m pip install pywin32 pyWinhook requests pyinstaller

# 4. Criar estrutura de pastas do projeto
echo -e "${GREEN}[*] Organizando pastas do repositório...${NC}"
mkdir -p modules output

# 5. Limpeza e permissões
chmod +x main.py
rm python_installer.exe 2>/dev/null

echo -e "${BLUE}--------------------------------------------------${NC}"
echo -e "${GREEN}[+] TUDO PRONTO! Framework configurada com sucesso.${NC}"
echo -e "${BLUE}[*] Agora podes correr: ${NC}python3 main.py"
echo -e "${BLUE}--------------------------------------------------${NC}"
