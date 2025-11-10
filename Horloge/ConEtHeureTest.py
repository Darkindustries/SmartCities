import network
import ntptime
import time
import socket
import gc

SSID = "electroProjectWifi"
PASSWORD = "B1MesureEnv"

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print("Connexion au Wi-Fi...", end="")
        wlan.connect(ssid, password)
        for _ in range(20):  # Timeout ~10s
            if wlan.isconnected():
                break
            print(".", end="")
            time.sleep(0.5)
        print()
    
    if wlan.isconnected():
        print("Connecté ! IP:", wlan.ifconfig()[0])
        return True
    else:
        print("Échec de la connexion Wi-Fi")
        return False

def sync_time():
    try:
        # Déconnexion propre pour éviter les problèmes
        ntptime.host = "pool.ntp.org"  # facultatif, mais fiable
        ntptime.settime()
        print("Heure synchronisée !")
        return True
    except:
        print("Erreur ntptime. Réessai dans 5s...")
        return False

# ==== BOUCLE PRINCIPALE ====
if connect_wifi(SSID, PASSWORD):
    # Tente plusieurs fois de synchroniser l'heure
    for _ in range(3):
        if sync_time():
            break
        time.sleep(5)

# Affichage heure actuelle
t = time.localtime()
heure = t[3]
minute = t[4]
seconde = t[5]
print(f"Heure actuelle : {heure:02d}:{minute:02d}:{seconde:02d}")

# Nettoyage mémoire
gc.collect()
