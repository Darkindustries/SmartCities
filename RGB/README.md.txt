# 🌡️ Projets MicroPython – Raspberry Pi Pico W

Ce dépôt contient **trois programmes**
Chaque programme illustre une étape supplémentaire dans la lecture et l’affichage de données.

---

## 📁 Contenu du dossier

### 1. `OnlyMic`
➡️ **Description :**  
Lecture des données du capteur **SoundSensor** (Sons) et affichage des valeurs directement dans le **terminal série**.

**Fonctionnalités :**
- Lecture continue des mesures du SoundSensor  
- Affichage des valeurs capté par l'ADC 
- Rafraîchissement régulier des données  

---

### 2. `OnlyRGBB`
➡️ **Description :**  
La led RGB reçoi des valeurs pour la faire scintiller avec une palette de couleurs.

**Fonctionnalités :**
- Affichage de divers couleurs 
---

### 3.🎧 `SOUND_DETECTOR`

➡️ **Description :**
Programme complet de **détection de pics sonores** utilisant le **Raspberry Pi Pico W**.  
Un **microphone analogique** (connecté à une entrée **ADC**) mesure en continu le niveau sonore ambiant.  
Lorsqu’un **pic sonore** est détecté (dépassement d’un seuil relatif), une **LED RGB WS2812** s’allume brièvement avec une **couleur aléatoire**, puis s’éteint.

---

### ⚙️ Fonctionnalités principales
- 🎤 Lecture du signal analogique depuis le **microphone** (`GP26 / ADC0`)  
- 🧮 Moyennage sur plusieurs échantillons pour obtenir un **niveau de référence stable**  
- 🚨 Détection automatique d’un **pic sonore** au-delà d’un **seuil relatif (`THRESHOLD`)**  
- 🌈 Indication visuelle via **LED RGB WS2812** :  
  - Affichage d’une **couleur aléatoire** lors de chaque détection  
  - Extinction automatique après un court **flash lumineux (`FLASH_DURATION`)**

---

### 🧠 Paramètres ajustables

| Paramètre | Rôle | Valeur par défaut |
|------------|------|-------------------|
| `MIC_PIN` | Broche ADC connectée au microphone | `GP26` |
| `LED_PIN` | Broche de la LED WS2812 | `GP18` |
| `NUM_LEDS` | Nombre de LED RGB utilisées | `1` |
| `SAMPLES` | Nombre d’échantillons pour la moyenne | `200` |
| `THRESHOLD` | Sensibilité du seuil de détection | `1.1` |
| `DEBOUNCE_MS` | Délai minimal entre deux pics | `100 ms` |
| `FLASH_DURATION` | Durée du flash LED | `100 ms` |

---

## 🧰 Matériel utilisé

- Raspberry Pi Pico W  
- Sound Sensor
- LED RGB WS2812  
 

