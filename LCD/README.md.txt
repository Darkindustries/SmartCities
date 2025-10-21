# 🌡️ Projets MicroPython – Raspberry Pi Pico W

Ce dépôt contient **trois programmes**
Chaque programme illustre une étape supplémentaire dans la lecture et l’affichage de données.

---

## 📁 Contenu du dossier

### 1. `DHT20`
➡️ **Description :**  
Lecture des données du capteur **DHT20** (température et humidité) et affichage des valeurs directement dans le **terminal série**.

**Fonctionnalités :**
- Lecture continue des mesures du DHT20  
- Affichage formaté des valeurs (`Température : xx°C`, `Humidité : yy%`)  
- Rafraîchissement régulier des données  

---

### 2. `LCD1`
➡️ **Description :**  
Même principe que le premier programme, mais les valeurs sont **affichées sur un écran LCD**.

**Fonctionnalités :**
- Lecture des données du DHT20  
- Affichage sur un **écran LCD 16x2 (I2C)**    

---

### 3. `LCD2`
➡️ **Description :**  
Programme complet de **régulation de température** à l’aide du **Raspberry Pi Pico W**.  
Une **résistance variable (potentiomètre)** permet de définir une température de consigne (entre 15°C et 35°C).  
Le système compare cette consigne à la température réelle mesurée par le **DHT20**, puis agit en conséquence sur une **LED**, un **buzzer**, et l’écran **LCD**.

**Fonctionnalités principales :**
- 🔧 Lecture du potentiomètre → conversion en température de consigne (15°C à 35°C)  
- 🌡️ Lecture du capteur DHT20 chaque seconde  
- 🧮 Comparaison entre température mesurée et consigne  
- 🖥️ Affichage LCD :  
  - Ligne 1 : `Set: xx°C` (température de consigne)  
  - Ligne 2 : `Ambient: yy°C` (température mesurée)  

---

### ⚙️ Contrôles et comportements

| Condition | Action |
|------------|---------|
| 🌡️ Température mesurée > consigne | LED clignote à **0,5 Hz** |
| 🌡️ Température mesurée > consigne + 3°C | **Buzzer** activé, LED clignote plus vite, affichage `"ALARM"` sur LCD |

- 💫 Battement progressif (dimmer) de la LED  
- 🔁 Clignotement du mot `"ALARM"` sur l’écran LCD  

---

## 🧰 Matériel utilisé

- Raspberry Pi Pico W  
- Capteur DHT20  
- Écran LCD 16x2 (I2C)  
- Potentiomètre (résistance variable)  
- LED + résistance  
- Buzzer   

