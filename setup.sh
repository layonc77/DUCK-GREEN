#!/bin/bash

# Cores para o terminal
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}[*] A iniciar configuração do DUCK GREEN Framework...${NC}"

# 1. Atualizar o sistema
echo -e "${GREEN}[*] Atualizando repositórios...${NC}"
sudo apt update -y

# 2. Instalar Wine e Python (Necessários para criar o .exe no Linux)
echo -e "${GREEN}[*] Instalando Wine, Python3 e Pip...${NC}"
sudo apt install wine wine64 python3 python3-pip wget -y

# 3. Configurar bibliotecas Python dentro do Wine
# Isso é o que permite que o PyInstaller funcione "fingindo" ser Windows
echo -e "${GREEN}[*] Instalando bibliotecas Windows no Wine... (Aguarde)${NC}"
wine python -m pip install pywin32 pyWinhook requests pyinstaller

# 4. Criar as pastas do projeto caso não existam
echo -e "${GREEN}[*] Organizando diretórios...${NC}"
mkdir -p modules output

# 5. Dar permissões de execução aos scripts
chmod +x main.py

echo -e "${BLUE}[+] Setup concluído com sucesso!${NC}"
echo -e "${BLUE}[+] Agora já podes correr: ${GREEN}python3 main.py${NC}"