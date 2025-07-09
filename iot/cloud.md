---
title: Probleme mit Cloud-Verbindung (funktionierendes W-Lan)
parent: IOT
---

## 🧭 Wahrscheinlichste Ursachen für Cloud-Verbindungsprobleme (trotz funktionierendem WLAN):

---

### ✅ **1. Provisionierung unvollständig / fehlgeschlagen**

* Gerät ist zwar im WLAN, **hat aber keine Cloud-Anmeldung abgeschlossen**
* App- oder Verbindungsabbruch während der Einrichtung
* Cloud-Token oder Device-ID wurde **nicht richtig übertragen**

🔧 **Lösung**:

* Gerät **auf Werkseinstellungen zurücksetzen**
* Provisionierung **neu und vollständig durchführen**

---

### ✅ **2. Gerät ist noch mit einem anderen Cloud-Konto verknüpft („device binding“)**

* Viele Plattformen (z. B. Tuya, Smart Life, Xiaomi) erlauben **nur 1 Besitzerkonto**
* Gerät ist also **online, aber für dich unsichtbar**, da mit altem Konto verknüpft

🔧 **Lösung**:

* Gerät vollständig zurücksetzen
* Oder ursprüngliches Konto verwenden
* Manche Hersteller verlangen „Besitzübergabe“ per App (z. B. QR-Code oder Unpairing)

---

### ✅ **3. Firmware-Fehler oder beschädigte Konfiguration**

* Flash-Speicher des ESP32 defekt oder z. B. durch Spannungsschwankung beim Flashen beschädigt
* Gerät „hängt“ in einem Zustand, in dem es sich nicht korrekt bei der Cloud meldet

🔧 **Lösung**:

* **Neu flashen**, ggf. mit bekannter stabiler Firmware-Version
* Vorher über UART-Log prüfen (wenn verfügbar)

---

### ✅ **4. Clock/Zeitsynchronisation schlägt fehl**

* Einige Cloud-Dienste (z. B. MQTT über TLS) **verlangen korrekte Uhrzeit**
* Wenn das Gerät z. B. **keinen NTP-Server erreicht**, schlägt die Verbindung fehl

🔧 **Lösung**:

* DNS prüfen (NTP braucht DNS-Auflösung)
* Firmware so konfigurieren, dass **ein funktionierender NTP-Server** verwendet wird (z. B. `pool.ntp.org`)

---

### ✅ **5. Device-UUID / Zertifikate fehlen oder sind ungültig**

* Cloud verlangt **eindeutige Kennung (Device ID, UUID, Token)**
* Wenn diese beim Flashen oder der Provisionierung **nicht gesetzt wurden**, meldet sich das Gerät **zwar im Netz, aber nicht korrekt bei der Cloud**

🔧 **Lösung**:

* Prüfen, ob die korrekten Token/Keys vorhanden sind
* Bei vorgefertigten Modulen: Vergleich mit funktionierendem Gerät
* Bei Eigenbau: logs oder serielle Ausgabe überprüfen

---

### ✅ **6. DNS- oder TLS-Fehler auf dem Gerät**

* Gerät **findet die Cloud-Domain nicht**, z. B. wegen falsch konfiguriertem DNS
* Oder kann keine TLS-Verbindung aufbauen (z. B. abgelaufenes Root-Zertifikat)

🔧 **Lösung**:

* DNS manuell setzen (z. B. Google DNS `8.8.8.8`)
* TLS-Fehler prüfen (→ Logausgabe über UART)
* CA-Zertifikate in Firmware prüfen (z. B. bei `esp_tls`)

---

## 🔎 Zusammenfassung: Wahrscheinlichste Ursachen (Ranking)

1. ❌ **Provisionierung unvollständig oder abgebrochen**
2. 🔒 **Cloud-Bindung an anderes Konto**
3. 🧠 **Defekte oder leere Konfiguration / Token fehlen**
4. 🕒 **NTP-Zeitsynchronisation scheitert**
5. 🔐 **TLS-Verbindungsfehler (CA-Zertifikat, Uhrzeit)**
6. 💥 **Hardware- oder Flashproblem**
