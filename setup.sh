#!/bin/bash

# Cores para o terminal
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}[*] Iniciando configuração DUCK GREEN Framework v1.1...${NC}"

# 1. Instalar dependências do sistema
echo -e "${GREEN}[*] Verificando dependências do Kali (Wine e Python)...${NC}"
sudo apt update && sudo apt install wine wine64 python3 python3-pip python3-venv wget -y

# 2. Criar e Ativar Ambiente Virtual (venv) no Linux
echo -e "${GREEN}[*] Configurando ambiente virtual (venv) do projeto...${NC}"
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}[+] Pasta venv criada.${NC}"
fi

# Ativando o ambiente para o restante da instalação
source venv/bin/activate
echo -e "${YELLOW}[*] Ambiente virtual ATIVADO.${NC}"

# 3. Instalar bibliotecas do Linux (Receptor) no venv
echo -e "${GREEN}[*] Instalando dependências do Receptor no venv...${NC}"
pip install --upgrade pip
pip install requests flask  # Flask é necessário para o receptor.py

# 4. Configurar Python de Windows no Wine (Compilador)
echo -e "${GREEN}[*] Preparando compilador Windows no Wine...${NC}"
if [ ! -f "python_installer.exe" ]; then
    wget https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe -O python_installer.exe
fi

echo -e "${YELLOW}[!] ATENÇÃO: Marque 'Add Python to PATH' na janela que vai abrir!${NC}"
wine python_installer.exe

# 5. Instalar dependências de compilação dentro do Wine
echo -e "${GREEN}[*] Instalando dependências de compilação no Wine...${NC}"
wine python -m pip install --upgrade pip
wine python -m pip install pywin32 pyWinhook requests pyinstaller

# 6. Finalização
mkdir -p modules output
chmod +x main.py
rm python_installer.exe 2>/dev/null

echo -e "${BLUE}--------------------------------------------------${NC}"
echo -e "${GREEN}[+] TUDO PRONTO! venv configurada e ativa.${NC}"
echo -e "${YELLOW}[!] IMPORTANTE: Sempre que abrir um novo terminal, use:${NC}"
echo -e "${NC}source venv/bin/activate${NC}"
echo -e "${BLUE}[*] Inicie com: ${NC}python3 main.py"
echo -e "${BLUE}--------------------------------------------------${NC}"
