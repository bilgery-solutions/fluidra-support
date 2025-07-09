---
title: W-Lan-Repeater Troubleshooting
parent: IOT
---

## 📡 **WLAN-Repeater: Worauf du achten solltest (insb. mit IoT-Geräten)**

### ✅ 1. **Gleiches WLAN-Netz verwenden (SSID)**

* Repeater sollte das **gleiche WLAN-Netz (SSID + Passwort)** wie der Hauptrouter nutzen
* → Sonst verbinden sich Geräte evtl. mit dem falschen Netz und sind nicht erreichbar

> 💡 **Keine zusätzliche SSID** wie `MeinWLAN_EXT`, wenn du keine getrennten Netze brauchst

---

### ⚠️ 2. **Client-Isolation vermeiden**

* Manche Repeater aktivieren **Client-Isolation** oder trennen "Repeater-Clients" vom Rest
* → IoT-Geräte **sehen dann keine App oder keinen Cloud-Server**

> 🔍 In den Einstellungen nach „AP Isolation“, „Client Isolation“, „Privates WLAN“ o. Ä. suchen

---

### 🕹️ 3. **Starke Signalstärke sicherstellen**

* Repeater **nicht zu weit vom Router**, aber auch **nicht zu nah am Gerät**
* Faustregel: Repeater **dort platzieren, wo das WLAN vom Hauptrouter gerade noch gut ist**

---

### 🌐 4. **2,4 GHz bevorzugen** (bei IoT-Geräten)

* Viele IoT-Geräte unterstützen **nur 2,4 GHz**, aber Repeater funken oft auf beiden Bändern
* → Achte darauf, dass das 2,4 GHz-Band **nicht deaktiviert ist**
* Bei Dualband-Repeatern: **Kein „Band Steering“ erzwingen**, wenn dein Gerät damit nicht klarkommt

---

### 🔄 5. **Stabile IP-Vergabe sicherstellen**

* Repeater sollten **kein eigener DHCP-Server** sein
* → Alle IP-Adressen müssen weiterhin **vom Haupt-Router vergeben werden**
* Sonst: Geräte im Repeater-Netz bekommen IPs, die **nicht mit dem Rest kommunizieren können**

---

### 🚫 6. **Kein „Gastnetzwerk“ über den Repeater**

* Wenn der Repeater das Gastnetz verstärkt, sind IoT-Geräte **isoliert vom Heimnetz**
* → App kann das Gerät evtl. nicht erreichen oder konfigurieren

---

### 🧪 7. **Provisionierung möglichst nahe am Haupt-Router durchführen**

* Bei Ersteinrichtung (BLE/SoftAP) kann es zu Problemen kommen, wenn das Signal über den Repeater läuft
* → Besser: Erst **direkt am Router koppeln**, dann Standort wechseln

---

### 🧰 8. **Repeater regelmäßig neu starten oder Firmware aktualisieren**

* Manche Repeater „vergessen“ Geräte, blockieren DHCP oder haben WLAN-Probleme bei Langzeitbetrieb
* Firmware-Updates helfen oft bei:

  * Mesh-Kompatibilität
  * DHCP-Relay-Problemen
  * Signalstabilität

---

## ✅ Zusammengefasst – das ist wichtig:

| Punkt                              | Empfehlung |
| ---------------------------------- | ---------- |
| **SSID gleich wie Router?**        | ✅ Ja       |
| **Client-Isolation aus?**          | ✅ Ja       |
| **2,4 GHz aktiv?**                 | ✅ Ja       |
| **DHCP nur am Router?**            | ✅ Ja       |
| **Gastnetz vermeiden?**            | ✅ Ja       |
| **Repeater-Standort gut gewählt?** | ✅ Ja       |
