---
title: Verbindungsprobleme trotz W-Lan
parent: IOT
---

# 🚨 Leitfaden: Gerät ist mit WLAN verbunden, aber nicht in der App sichtbar

## 🧭 Übersicht: Was ist das Problem?
Das IoT-Gerät zeigt „WLAN verbunden“ an, aber:
- Es ist **nicht in der App sichtbar**
- Es lässt sich **nicht steuern**
→ Wahrscheinlich **keine Verbindung zur Cloud oder zur App**

---

## ✅ Schnell-Checkliste

| Prüfen | Mögliche Ursache | Lösung |
|--------|------------------|--------|
| 🌐 Hat der Router Internet? | Kein Internetzugang | Router/Modem neu starten |
| 📱 Hat das Smartphone Internet? | App kann Cloud nicht erreichen | WLAN + mobile Daten testen |
| 🔌 Ist Firewall/Jugendschutz aktiv? | Cloud-Verbindung wird blockiert | Testweise deaktivieren |
| 🧭 Hat das Gerät gültige IP/DNS? | Keine Gateway/DNS | Router prüfen, ggf. feste IP |
| 🔁 Ist die Provisionierung vollständig? | App hat Setup nicht beendet | Gerät resetten & neu koppeln |
| 📱 Ist das Gerät in der App angemeldet? | Anderes Benutzerkonto | Mit ursprünglichem Konto einloggen |
| ☁️ Funktioniert es über Hotspot? | Heimnetz blockiert etwas | Dann liegt’s am Router |
| 🔍 Siehst du das Gerät im Router? | Verbindung ja, Cloud nein | DNS ändern (z. B. 8.8.8.8) |
| 🔑 Muss das Gerät online sein, um sichtbar zu sein? | App zeigt nur Cloud-Geräte | Temporär mobile Daten aktivieren |

---

## 🧪 Tipps zur Fehlersuche

- ✅ Test mit **Smartphone-Hotspot** → Funktioniert’s da, liegt’s **nicht am Gerät**
- ✅ **Router-Log oder DHCP-Liste prüfen** → Hat das Gerät eine IP?
- ✅ **Provisionierung vollständig durchlaufen lassen**
- ✅ **VPN / DNS-Filter / AdBlocker deaktivieren**
- ✅ **App neu starten, ggf. neu einloggen**
- ✅ **Firmware-Reset** am Gerät (Knopf halten)

---

## 💡 Häufige Ursachen (Top 5)

1. Gerät im WLAN, aber **kein Internetzugang**
2. **Firewall blockiert** Cloud-Zugriff
3. App kann **lokal nicht kommunizieren** (kein mDNS/UDP)
4. **Provisionierung unvollständig**
5. Gerät gehört einem **anderen Konto**

---
