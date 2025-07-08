---
title: Verbindungsprobleme Leitfaden
parent: IOT
---

# 🛠️ **Leitfaden: Wenn ein IoT-Gerät keine Verbindung aufbauen kann**

---

### **1. Basischeck: Voraussetzungen prüfen**

* ✅ Gerät ist **eingeschaltet** und in Kopplungsmodus (LED-Signale prüfen)
* ✅ App ist **aktuell** und hat **alle Berechtigungen** (WLAN, Standort, Bluetooth, je nach Gerät)
* ✅ Smartphone ist mit **dem gewünschten WLAN verbunden**
* ✅ WLAN ist **nicht versteckt** (SSID sichtbar)

---

### **2. WLAN-Band prüfen: 2,4 GHz vs. 5 GHz**

> **Problem**: ESP32-Geräte unterstützen **nur 2,4 GHz**

* 📱 In den WLAN-Einstellungen prüfen: Ist das Handy mit einem 5 GHz-Netz verbunden?
* 🔧 Im Router prüfen:

  * 2,4 GHz ist **aktiviert**
  * Idealerweise **unterschiedliche SSIDs** für 2,4 GHz und 5 GHz (z. B. „Heimnetz\_2G“ und „Heimnetz\_5G“)
* 📶 Gerät und Smartphone müssen **beide im selben 2,4 GHz-Netz** sein.

---

### **3. Signalstärke prüfen**

> **Problem**: Zu schwaches Signal → Abbrüche oder keine Verbindung

* 📍 Gerät näher an den Router bringen
* 🔁 WLAN-Repeater/Mesh-System verwenden
* 📡 Signalstärke mit Handy oder App (z. B. „WiFi Analyzer“) prüfen

---

### **4. Provisionierung verstehen (Einrichtungsschritt)**

> **Problem**: Initiale Kopplung schlägt fehl

Viele Geräte funktionieren so:

* App startet → sendet WLAN-Zugangsdaten an das Gerät
* Gerät verbindet sich dann mit dem Heimnetz

⚠️ Häufige Stolperfallen:

* Smartphone verlässt das provisorische WLAN des Geräts zu früh
* Standortdienste sind nicht aktiviert (Pflicht bei Android ab Android 9)
* WLAN-Zugangsdaten falsch eingegeben
* App bekommt keine Berechtigung zum WLAN-Zugriff

✅ **Lösungen**:

* Standortdienste aktivieren
* App Berechtigungen manuell prüfen
* WLAN-Passwort neu eingeben
* Einrichtung **nochmals versuchen**

---

### **5. Heimnetz prüfen**

> **Problem**: Router oder Netzkonfiguration blockiert Kommunikation

* 📡 DHCP aktiv? → Gerät bekommt IP-Adresse automatisch?
* 🔄 IP-Konflikt vermeiden (bei Bedarf feste IP zuweisen)
* 🚫 AP-Isolation/Gastmodus deaktivieren (sonst keine Kommunikation zw. Geräten)
* 🔥 Firewall-/Kindersicherung überprüfen (keine Geräte blockieren)
* 🔌 Bei Problemen: Router kurz neu starten

---

### **6. App und Gerät im gleichen Netz?**

> **Problem**: App kann das Gerät nicht erreichen

* Smartphone und IoT-Gerät **müssen im gleichen Netz** sein
* Keine Mobilfunkverbindung während Kopplung
* Kein VPN oder DNS-Filter (z. B. AdGuard) aktiv

---

### **7. Alternativtest mit Smartphone-Hotspot**

> **Schneller Ausschluss**: Liegt das Problem am Heimnetz?

* 🔁 Erstelle einen 2,4 GHz-Hotspot mit einem zweiten Smartphone
* 📶 Koppel das IoT-Gerät testweise über diesen Hotspot
* 📲 Wenn es dort klappt: Das Problem liegt **nicht am Gerät**, sondern **am Heimnetz**

---

### **8. Weitere technische Ursachen (seltener)**

* ⚙️ Firmware des Geräts veraltet oder fehlerhaft
* ⛔ Maximalanzahl verbundener Geräte am Router erreicht (z. B. bei Billigroutern)
* 📱 App-Inkompatibilität mit neuem Android/iOS
* 🧱 Defektes Gerät (selten, aber möglich)

---

## ✅ **Checkliste zum Abhaken (Kurzform)**

| Schritt                        | Erledigt? |
| ------------------------------ | --------- |
| 2,4 GHz aktiv + verbunden      | ⬜         |
| WLAN sichtbar                  | ⬜         |
| App-Berechtigungen erteilt     | ⬜         |
| Standortdienste aktiv          | ⬜         |
| Kein Gastnetz/VPN aktiv        | ⬜         |
| Signalstärke ausreichend       | ⬜         |
| DHCP aktiv / IP korrekt        | ⬜         |
| Kopplung sorgfältig wiederholt | ⬜         |
| Test mit Hotspot erfolgreich?  | ⬜         |
