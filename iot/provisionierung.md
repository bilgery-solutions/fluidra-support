---
title: Provisionierung Troubleshooting
parent: IOT
---

# 🛠️ IoT-Provisionierung – Support-Checkliste bei Verbindungsproblemen

## 📍 Ziel: Gerät lässt sich nicht mit App verbinden oder meldet „Zeitzonenfehler“

---

## ✅ 1. Basisprüfung (Allgemein)

- [ ] Ist das Gerät eingeschaltet und im Provisionierungsmodus? (z. B. blinkende LED)
- [ ] Ist das Smartphone mit dem **richtigen 2,4 GHz WLAN** verbunden?
- [ ] Ist **Bluetooth aktiviert** (für BLE-Provisionierung)?
- [ ] Sind **Standortdienste aktiv** (besonders bei Android)?
- [ ] Hat die App alle nötigen Berechtigungen?

---

## 🌐 2. Internetverbindung im Heimnetz prüfen

- [ ] Kommen andere Geräte ins Internet?
- [ ] Testweise ein Gerät (z. B. Smartphone oder PC) vom gleichen WLAN aus:
  - [ ] Webseite `https://google.de` funktioniert?
  - [ ] Aufruf von `http://pool.ntp.org` im Browser leitet auf eine Seite um? (zeigt DNS + Internet OK)

---

## 🧩 3. DNS-Probleme ausschließen

- [ ] In Router-Oberfläche prüfen: Welcher **DNS-Server ist eingetragen**?
  - Falls möglich: Temporär auf `8.8.8.8` oder `1.1.1.1` umstellen
- [ ] Router neu starten
- [ ] Pi-hole / AdGuard Home / Kindersicherung aktiv?
  - → DNS-Filter ausschalten oder Ausnahmen einrichten

---

## 🕒 4. NTP-Zeitabgleich prüfen

- [ ] Port 123/UDP könnte blockiert sein (selten, aber möglich)
- [ ] Test am PC im gleichen WLAN:

  **Windows CMD:**
  ```
  w32tm /stripchart /computer:pool.ntp.org /dataonly /samples:3
  ```

  **Linux/macOS:**
  ```
  ntpdate -q pool.ntp.org
  ```

  → Wenn Fehler oder Timeout: NTP wird blockiert

---

## 📲 5. Provisionierung über mobilen Hotspot testen

- [ ] Hotspot auf einem zweiten Smartphone einrichten (2,4 GHz)
- [ ] Gerät mit Hotspot provisionieren
- [ ] Funktioniert es hier → Fehler liegt **nicht am Gerät**, sondern **am Heimnetz**

---

## 🧼 6. Gerät zurücksetzen & neu provisionieren

- [ ] Gerät vollständig auf Werkseinstellungen zurücksetzen (Knopf halten, Anleitung beachten)
- [ ] App schließen und neu öffnen
- [ ] Provisionierung erneut durchführen

---

## 📦 7. Spezialfälle

- [ ] Gerät ist bereits mit anderem Konto verknüpft → „Besitzübergabe“ nötig?
- [ ] Alte Firmware → kann Cloudserver nicht erreichen (manchmal bei längerer Lagerung)
- [ ] TLS schlägt fehl wegen falscher Zeit → zurück zu Punkt 4

---

## 📌 Empfehlung bei anhaltenden Problemen

- [ ] DNS-Server auf dem Router dauerhaft auf z. B. `1.1.1.1` setzen
- [ ] Geräte möglichst **nah am Router provisionieren**
- [ ] Kindersicherungen, Netzwerksperren oder Adblocker (Pi-hole etc.) prüfen
- [ ] Bei Mesh-Systemen → testweise an Haupt-Router koppeln
