

```markdown
# 🦆 DUCK GREEN Framework v1.0

![Python](https://img.shields.io/badge/Python-3.8+-green.svg)
![Platform](https://img.shields.io/badge/Platform-Kali_Linux-blue.svg)
![Target](https://img.shields.io/badge/Target-Windows-red.svg)

**DUCK GREEN** é uma framework de automação para Red Team e testes de penetração, focada na geração de agentes de monitorização remota (Keylogging & Clipboard) com persistência no Windows.

## 🚀 Funcionalidades
* **Geração Automatizada:** Cria executáveis (.exe) injetando URLs dinamicamente.
* **Persistência:** Instalação automática no registo do Windows.
* **Captura Inteligente:** Monitoriza teclas e área de transferência (Clipboard).
* **Receptor Flask:** Servidor dedicado para recepção e armazenamento de logs.
* **UAC Bypass:** Solicitação automática de privilégios administrativos.

## 🛠️ Instalação

Primeiro, clona o repositório e configura o ambiente:

```bash
git clone [https://github.com/TEU_USER/DUCK-GREEN.git](https://github.com/TEU_USER/DUCK-GREEN.git)
cd DUCK-GREEN
chmod +x setup.sh
./setup.sh
```

## 💻 Como Usar

1.  **Inicia a Framework:**
    ```bash
    python3 main.py
    ```
2.  **Gera o Agente:** Escolha a opção `1`, insira a sua URL (Ngrok/IP) e o ficheiro será gerado na pasta `output/`.
3.  **Inicia o Receptor:** Escolha a opção `2` para ficar a aguardar as conexões.

## ⚠️ Aviso Legal
Este software foi desenvolvido apenas para fins educacionais e testes de segurança autorizados. O uso desta ferramenta em sistemas sem permissão explícita é ilegal.
```
