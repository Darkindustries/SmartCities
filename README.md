# SmartCities

Le **Raspberry Pi Pico W** est une carte microcontrôleur compacte et abordable, conçue pour les projets embarqués et IoT.  
Elle est équipée de :  
- **Processeur Arm Cortex-M0+** à 133 MHz  
- **264 Ko de RAM**  
- **2 Mo de mémoire flash**  
- **26 broches GPIO multifonctions** (SPI, I2C, UART, PWM)

![Raspberry Pi Pico W](https://user-images.githubusercontent.com/124893862/219611249-dd82aad6-da4c-41f7-a80e-fc87fd51e38a.png)

Le Pico W intègre un **module Wi-Fi**, idéal pour les projets connectés nécessitant un contrôle à distance ou un échange de données.  

La carte se programme facilement avec **MicroPython**, une version légère de Python pour microcontrôleurs. MicroPython propose de nombreuses bibliothèques pour interagir avec le matériel : GPIO, PWM, I2C, SPI, UART, etc.  
On peut aussi utiliser des bibliothèques tierces compatibles pour enrichir ses projets.

![MicroPython sur Pico W](https://user-images.githubusercontent.com/124893862/219622236-a85db1f7-3dd8-4ba2-a3bf-8396c5b27cb0.png)

---

## Broches GPIO

Le Pico W dispose de **26 broches GPIO multifonctions** :  
- 2 × SPI  
- 2 × I2C  
- 2 × UART  
- 3 × ADC 12 bits  
- 16 × PWM

La carte possède également **8 broches de masse (GND)** et plusieurs broches d’alimentation (3,3 V et 5 V).

![GPIO Pico W](https://user-images.githubusercontent.com/124893862/219611075-1f9e3f77-ad73-4504-9a44-8857870773e3.png)

---

## Shield Grove pour Pico

Le **Grove Shield** simplifie le câblage vers différents modules grâce à des connecteurs codés par couleur :  
- Le nom de chaque broche est indiqué sur le connecteur  
- La tension peut être commutée entre **3,3 V et 5 V**  
- Double rangée de connecteurs femelles pour un câblage facile vers le Pico  

**Exemple :** [Grove Shield For Pi Pico v1.0 – Seed Studio](https://www.seeedstudio.com/)

![Grove Shield](https://user-images.githubusercontent.com/124893862/219610776-ff0e4372-5288-4e84-8a42-88c22d09d84c.png)