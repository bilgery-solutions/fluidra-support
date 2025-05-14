---
title: Problembehebung ZS500
parent: ZS500
---

# Problembehebung ZS500

## Geräteverhalten ZS500

| Problem | Lösungen |
| --- | --- |
| Das Gerät beginnt nicht sofort mit dem Heizen | * Beim Start verbleibt das Gerät für 30 Sekunden im „Pause“-Modus, bevor es den Betrieb aufnimmt.<br>* Wenn die Solltemperatur erreicht ist, stoppt die Wärmepumpe das Heizen: Die Wassertemperatur ist gleich oder höher als die Solltemperatur.<br>* Wenn kein oder zu wenig Wasserdurchfluss vorhanden ist, stoppt die Wärmepumpe: Überprüfen Sie, ob das Wasser korrekt durch die Wärmepumpe zirkuliert (siehe § „2.5 I Menüübersicht“) und ob die hydraulischen Anschlüsse korrekt sind.<br>* Die Wärmepumpe stoppt, wenn die Außentemperatur unter -12 °C fällt.<br>* Es kann sein, dass die Wärmepumpe eine Betriebsstörung erkannt hat (siehe § „4.2 I Fehlercodeanzeige“).<br>* Wenn Sie diese Punkte überprüft haben und das Problem weiterhin besteht: Wenden Sie sich an Ihren Händler. |
| Das Gerät entleert Wasser | * Häufig handelt es sich um Kondenswasser. Diese Flüssigkeit ist die in der Luft enthaltene Feuchtigkeit, die bei Kontakt mit kalten Teilen der Wärmepumpe (insbesondere dem Verdampfer) kondensiert. Je feuchter die Luft, desto mehr Kondenswasser entsteht (mehrere Liter pro Tag möglich). Dieses Wasser wird vom Boden der Wärmepumpe aufgefangen und durch Ablauflöcher abgeführt.<br>* Um auszuschließen, dass das Wasser aus einem Leck im Poolkreislauf stammt, schalten Sie die Wärmepumpe aus und lassen Sie die Filterpumpe laufen. Wenn weiterhin Wasser durch die Kondensatabläufe austritt, liegt ein Wasserleck vor – kontaktieren Sie Ihren Händler. |
| Der Verdampfer ist vereist | * Ihre Wärmepumpe schaltet bald in den Abtauzyklus, um das Eis zu schmelzen.<br>* Wenn die Wärmepumpe den Verdampfer nicht enteisen kann, stoppt sie den Betrieb – das bedeutet, die Außentemperatur ist zu niedrig (unter -12 °C). |
| Das Gerät „raucht“ | * Dies kann während des Abtauzyklus auftreten, wenn Wasser zu Dampf wird.<br>* Wenn sich die Wärmepumpe nicht im Abtauzyklus befindet, ist das nicht normal. Schalten Sie das Gerät sofort aus, trennen Sie es vom Stromnetz und kontaktieren Sie Ihren Händler. |
| Das Gerät funktioniert nicht | * 🔧 Wenn keine Anzeige vorhanden ist, prüfen Sie die Versorgungsspannung und die Sicherung F1.<br>* Wenn die Solltemperatur erreicht ist, stoppt die Wärmepumpe das Heizen: Die Wassertemperatur ist gleich oder höher als die Solltemperatur.<br>* Wenn kein oder zu wenig Wasserdurchfluss vorhanden ist, stoppt die Wärmepumpe: Überprüfen Sie den Wasserkreislauf (siehe § „2.5 I Menüübersicht“).<br>* Die Wärmepumpe stoppt, wenn die Außentemperatur unter -12 °C fällt.<br>* Es kann sein, dass eine Betriebsstörung erkannt wurde (siehe § „4.2 I Fehlercodeanzeige“).<br>* Das Gerät befindet sich in einem leeren Zeitfenster. Deaktivieren Sie den „Zeitraum“-Modus für manuellen Betrieb oder ändern Sie die Zeitprogrammierung. |
| Das Gerät läuft, aber die Wassertemperatur steigt nicht | * Der Betriebsmodus ist nicht leistungsstark genug („Eco Silence“ oder „Smart“-Modus aktiv). Wechseln Sie in den „Boost“-Modus und stellen Sie die Filterung manuell auf 24/24, bis die Temperatur steigt.<br>* Es könnte eine Betriebsstörung vorliegen (siehe § „4.2 I Fehlercodeanzeige“).<br>* Prüfen Sie, ob das automatische Einlassventil offen festsitzt – dies würde ständig kaltes Wasser zuführen und das Aufheizen verhindern.<br>* Es geht zu viel Wärme verloren, weil die Luft kühl ist. Verwenden Sie eine wärmeisolierende Poolabdeckung.<br>* Der Verdampfer ist durch Schmutz verstopft und kann nicht genug Energie aufnehmen. Reinigen Sie ihn (siehe § „3.2 I Wartung“).<br>* Prüfen Sie, ob äußere Umstände die Wärmepumpe behindern (siehe § „❶ Installation“).<br>* 🔧 Stellen Sie sicher, dass die Wärmepumpe richtig dimensioniert ist für den Pool und die Umgebungsbedingungen. |
| Der Ventilator läuft, aber der Kompressor stoppt gelegentlich ohne Fehlermeldung | * Wenn die Außentemperatur niedrig ist, führt die Wärmepumpe Abtauzyklen durch.<br>* Der Verdampfer ist möglicherweise verschmutzt und kann nicht ausreichend Energie aufnehmen. Reinigen Sie ihn (siehe § „3.2 I Wartung“). |
| Das Gerät löst den Leitungsschutzschalter aus | * 🔧 Prüfen Sie, ob der Leitungsschutzschalter korrekt dimensioniert ist und ob die verwendete Kabelquerschnittsgröße passt (siehe § „5.2 I Technische Daten“).<br>* 🔧 Die Versorgungsspannung ist zu niedrig – wenden Sie sich an Ihren Stromversorger. |

## Fehlercodeanzeige ZS500

### Fehlercodeanzeige ZS500 Teil 1

| Anzeige                                                                                 | Mögliche Ursachen                                                                  | Lösungen                                                                                   | Rücksetzung                                               |
| --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Fehler 01**<br/>Kommunikationsfehler zwischen Steuerplatine und Anzeigetafel         | Schlechte Verbindung zwischen Platine A1 und A2                                    | Überprüfen Sie die RJ11- und RJ45-Steckverbindungen zwischen den Platinen                  | Automatisch (bei weniger als 4 Fehlern pro Stunde) oder ⏻ drücken |
|                                                                                         | Stromversorgungsfehler der Platinen                                                | Überprüfen Sie die Stromversorgung der Platinen                                            |                                                          |
|                                                                                         | Defekte Platinen                                                                   | Platinen austauschen                                                                       |                                                          |
| **Fehler 02**<br/>Überhitzung der Elektronikplatine                                     | Lüftungsschlitze an der Geräterückseite blockiert                                  | Rückwand reinigen. Falls das Problem bestehen bleibt: einen autorisierten Techniker rufen | Automatisch (bei weniger als 4 Fehlern pro Stunde) oder ⏻ drücken |
|                                                                                         | Ventilatormotor funktioniert nicht korrekt                                         | Ventilatormotor austauschen                                                                |                                                          |
| **Fehler 03**<br/>Automatischer Schutz bei Netzinstabilitäten                           | Überspannung, Stromausfall oder Spannungseinbruch im Netz                          | Netzqualität prüfen                                                                        | Automatisch (bei weniger als 4 Fehlern pro Stunde) oder ⏻ drücken |
|                                                                                         | Fehlerhafte Erdung                                                                 | Erdungskabel prüfen und korrekt anschließen                                                |                                                          |
|                                                                                         | Platine A1 funktioniert nicht korrekt                                              | Platine A1 austauschen                                                                     |                                                          |

### Fehlercodeanzeige ZS500 Teil 2

| Anzeige                                                                                 | Mögliche Ursachen                                                                  | Lösungen                                                                                   | Rücksetzung                                               |
| --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Fehler 05**<br/>Fehler am Ventilatormotor                                             | Ventilatormotor nicht angeschlossen                                                | Anschluss des Ventilatormotors prüfen. Falls Problem bleibt: autorisierten Techniker rufen | Automatisch (bei weniger als 4 Fehlern pro Stunde) oder ⏻ drücken |
|                                                                                         | Ventilatormotor defekt                                                             | Ventilatormotor austauschen                                                                |                                                          |
| **Fehler 06**<br/>Überhitzung der Stromversorgung des Kompressors                       | Lüftungsschlitze an der Rückwand blockiert                                         | Rückwand reinigen<br/>Falls Problem bleibt: autorisierten Techniker rufen                  | Automatisch (bei weniger als 4 Fehlern pro Stunde) oder ⏻ drücken |
|                                                                                         | Ventilatormotor funktioniert nicht korrekt                                         | Ventilatormotor austauschen                                                                |                                                          |
|                                                                                         | Über- oder Unterspannung der Stromversorgung                                       | Netzspannung prüfen (max. 240V ±10 %)                                                      |                                                          |
| **Fehler 07**<br/>Überstromversorgung des Kompressors                                   | Kompressor funktioniert nicht korrekt                                              | Kompressor austauschen                                                                     | Automatisch (bei weniger als 4 Fehlern pro Stunde) oder ⏻ drücken |
|                                                                                         | Platine A1 funktioniert nicht korrekt                                              | Platine A1 austauschen                                                                     |                                                          |
|                                                                                         | Fehlanschluss der Erdungsmasse                                                     | Erdungskabel korrekt anschließen                                                           |                                                          |

### Fehlercodeanzeige ZS500 Teil 3

| Anzeige                                                                                 | Mögliche Ursachen                                                                  | Lösungen                                                                                   | Rücksetzung                                               |
| --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Fehler 08**<br/>Niederdruckstörung im Kältekreislauf                                  | Druckfehler im Niederdruckkreis (wenn Problem nach Reset bestehen bleibt)          | Autorisierten Techniker rufen                                                              | Automatisch (bei weniger als 4 Fehlern pro Stunde) oder ⏻ drücken |
|                                                                                         | Wärmetauscher durch Schmutz verstopft                                              | Wärmetauscher reinigen                                                                    |                                                          |
| **Fehler 09**<br/>Hochdruckstörung im Kältekreislauf                                    | Unzureichender Wasserdurchfluss                                                    | Durchfluss erhöhen (Bypass prüfen), Poolfilter auf Verstopfung prüfen                     | Automatisch (bei weniger als 4 Fehlern pro Stunde) oder ⏻ drücken |
|                                                                                         | Luft-Wasser-Gemisch gelangt in das Gerät                                           | Hydrauliksystem des Pools prüfen                                                           |                                                          |
|                                                                                         | Durchflussregler blockiert                                                         | Durchflussregler prüfen                                                                   |                                                          |
| **Fehler 10**<br/>Sensorfehler ST3 (Abtausensor)                                        | Sensor defekt oder getrennt (J14-Stecker)                                          | Sensor wieder anschließen oder austauschen                                                 | ⏻ drücken                                                |
| **Fehler 11**<br/>Sensorfehler ST (Lufteinlasssensor)                                   | Sensor defekt oder getrennt (J12-Stecker)                                          | Sensor wieder anschließen oder austauschen                                                 | ⏻ drücken                                                |
| **Fehler 12**<br/>Sensorfehler ST5 (Sensor am Verdichteraustritt) | Sensor defekt oder getrennt (J13-Stecker) | Sensor wieder anschließen oder austauschen | ⏻ drücken |
| **Fehler 13**<br/>Sensorfehler ST4 (Sensor an der Kältemittelleitung) | Sensor defekt oder getrennt (J16-Stecker) | Sensor wieder anschließen oder austauschen | ⏻ drücken |
| **Fehler 14**<br/>Sensorfehler ST1 (Wasserzulaufsensor) | Sensor defekt oder getrennt (J46-Stecker) | Sensor wieder anschließen oder austauschen | ⏻ drücken |

## Technische Spezifikationen ZS500

| **ZS500** | Einheit | MD4 | MD5 | TD5 | MD8 | TD8 |
| --------- | ------- | ---- | ---- | ---- | ---- | ---- |
| Betriebstemperaturbereich | Luft | -12 bis 40 °C | -12 bis 40 °C | -12 bis 40 °C | -12 bis 40 °C | -12 bis 40 °C |
| Betriebstemperaturbereich | Wasser | 12 bis 32 °C | 12 bis 32 °C | 12 bis 32 °C | 12 bis 32 °C | 12 bis 32 °C |
| Stromversorgung |  | 220–240 V / 50 Hz | 220–240 V / 50 Hz | 380–415 V / 50 Hz | 220–240 V / 50 Hz | 380–415 V / 50 Hz |
| Zulässige Netzspannungsschwankung |  | ±6 % (im Betrieb) | ±6 % (im Betrieb) | ±6 % (im Betrieb) | ±6 % (im Betrieb) | ±6 % (im Betrieb) |
| Verschmutzungsklasse |  | I | I | I | I | I |
| Verschmutzungsgrad |  | 2 | 2 | 2 | 2 | 2 |
| Überspannungskategorie |  | III | III | III | III | III |
| Nennstromaufnahme | A | 7,5 | 10 | 4,4 | 15 | 6 |
| Max. Stromaufnahme | A | 10 | 13,9 | 6 | 22 | 8 |
| Mindestleiterquerschnitt | mm² | 3 x 2,5 | 3 x 2,5 | 5 x 2,5 | 3 x 6 | 5 x 2,5 |
| Prüfdruck | Pa | 300.000 | 300.000 | 300.000 | 300.000 | 300.000 |
| Betriebsdruck | Pa | 150.000 | 150.000 | 150.000 | 150.000 | 150.000 |
| Druckverlust | mWS (Meter Wassersäule) | 1,5 | 1,5 | 1,5 | 1,5 | 1,5 |
| Empfohlener Wasserdurchfluss | m³/h | 4 | 5 | 5 | 6 | 6 |


## Stückliste ZS500

### Unterstückliste Elektronik ZS500

| Nr.                           | Bezeichnung                                                         | Art. Nr.  | Anzahl |
| ----------------------------- | ------------------------------------------------------------------- | --------- | ------ |
| 25                            | Paddelschalter                                                      | B0052400A | 1    |
| 26-30                         | Fühler ST1, ST2, ST3, ST4, ST5<br/>(1 Ersatzfühler mit Wagoklemmen) | R06740    | 5    |
| 31                            | Steuerung / Regeleinheit kpl., ohne Display für MD4                 | B0203200A | 1    |
| 31                            | Steuerung / Regeleinheit kpl., ohne Display für MD5                 | B0052100A | 1    |
| 31                            | Steuerung / Regeleinheit kpl., ohne Display für MD8                 | B0203300A | 1    |
| 31                            | Steuerung / Regeleinheit kpl., ohne Display für TD5                 | B0224900A | 1    |
| 31                            | Steuerung / Regeleinheit kpl., ohne Display für TD8                 | B0225000A | 1    |
| 34                            | Hauptplatine A1 inkl. Patch A4 für MD4                        | R07146    | 1    |
| 34                            | Hauptplatine A1 inkl. Patch A4 für MD5                        | R07147    | 1    |
| 34                            | Hauptplatine A1 inkl. Patch A4 für MD8                        | R07148    | 1    |
| 34                            | Hauptplatine A1 inkl. Patch A4 für TD5                        | B0217300B | 1    |
| 34                            | Hauptplatine A1 mit integriertem Patch für TD8                | B0217400B | 1    |
| 34                            | Feinsicherung für Platine A1, 25A 6,3 × 32                          | B0050600A | 1    |
| 46                            | Kondensator 1500μF 400V für TD5, TD8                                | B0217700A | 1    |
| 56                            | Steuerkabel RJ11/45 2M                                              | B0051900A | 1    |
| 37                            | Entstörfilter EMC für MD4, MD5                                      | B0050900A | 1    |
| 37                            | Entstörfilter EMC für MD8                                           | WTC04000  | 1    |
| 37                            | Entstörfilter EMC für TD5, TD8                                      | B0217600A | 1    |
| 32                            | Umschaltrelais 12A 230V, 2 Wechsler                                 | B0050800A | 1    |
| 32                            | Relais TD5, TD8                                                     | B0217500A | 1    |
| 33                            | Filterspule 30 KHZ 1,5mH 22A                                        | B0050700A | 1    |
| 38                            | Induktor Filter für DTx (400V)                                      | R0848700  | 1    |
| 47                            | Feinsicherung für Platine A1, 25A 6,3 × 32                          | B0050600A | 1    |
| 42                            | Heizpatrone 55W L750                                                | B0051000A | 1    |
| 66                            | Lüftermotor                                                         | B0050300A | 1    |
| 76                            | Bedieneinheit / Display PAD                                   | WVH00001  | 1    |
|                         | Patch A4 für Hauptplatine A1                                        | R06930    | 1    |
|                         | Filter für 4-Wege-Ventil                                            | R0800000  | 1    |

### Unterstückliste Kältetechnik ZS500

| Nr.                           | Bezeichnung                                                         | Art. Nr.  | Anzahl |
| ----------------------------- | ------------------------------------------------------------------- | --------- | ------ |
| 1                             | Kompressor für MD4, MD5                                             | B0050500A | 1    |
| 1                             | Kompressor für MD8                                                  | B0185300A | 1    |
| 1                             | Kompressor für TD5                                                  | V0145000A | 1    |
| 1                             | Kompressor für TD8                                                  | V0145100A | 1    |
| 6                             | Verdampfer für MD4                                                  | M0126100A | 1    |
| 6                             | Verdampfer für MD5, TD5, MD8, TD8                                   | M0042500A | 1    |
| 17                            | Druckminderventil für MD4                                           | WTC03927  | 1    |
| 17                            | Druckminderventil für MD5, TD5, MD8, TD8                            | WTC03928  | 1    |
| 40                            | Spule für Druckminderventil                                         | B0217200A | 1    |
| 20                            | 4-Wege-Ventil für MD4, MD5, TD5                                     | WTC03989  | 1    |
| 20                            | 4-Wege-Ventil für MD8, TD8                                          | V0144700A | 1    |
| 41                            | Magnetschalter für 4-Wege-Ventil                                    | WTC03836  | 1    |
| 44                            | Druckwächter Niederdruck                                            | B0051200A | 1    |
| 45                            | Druckwächter Hochdruck                                              | B0051100A | 1    |
| 75                            | Kondensator / Wärmetauscher für MD4, MD5, TD5                    | R06954    | 1    |
| 75                            | Kondensator / Wärmetauscher für MD8, TD8                         | R06957    | 1    |
|                         | Trockner Byflow (BFK 83S) für MD4, MD5, TD5                    | WDA01388  | 1    |
|                         | Trockner Byflow (BFK 84S) für MD8, TD8                         | WDA01389  | 1    |

### Unterstückliste Gehäuse ZS500

| Nr.            | Bezeichnung                                                                                   | Art. Nr.  | Anzahl |
| -------------- | --------------------------------------------------------------------------------------------- | --------- | ---- |
| 10             | Obere Abdeckung                                                                               | A0240800A | 1    |
| 11             | Frontblende                                                                                   | A0240500A | 1    |
| 12             | Lüftergehäuse                                                                                 | A0240700A | 1    |
| 13             | Kondensator Austrittsplatte                                                                   | M0041200A | 1    |
| 14             | Technikzugang Gehäuse Eckteil                                                                 | M0041300A | 1    |
| 15             | Grundplatte                                                                                   | A0240600A | 1    |
| 54             | Aufkleber Zodiac Logo                                                                         | W2070A    | 1    |
| 71             | Schutzgitter für Verdampfer                                                                   | A0261000A | 1    |
| 68             | Motorkonsole für Ventilator / Propeller für MD4                                               | M0132900A | 2    |
| 68             | Motorkonsole für Ventilator / Propeller für MD5, MD8, TD5, TD8                                | M0041400A | 2    |
| o. Nr.         | Bedienfolie für PAD                                                                           | WZD00001  | 1    |

### Unterstückliste Sonstiges ZS500

| Nr.            | Bezeichnung                                                                                   | Art. Nr.  | Anzahl |
| -------------- | --------------------------------------------------------------------------------------------- | --------- | ---- |
| 2              | Schallschutzhaube für Kompressor für MD4, MD5, TD5                                            | T0041900A | 1    |
| 2              | Schallschutzhaube für Kompressor für MD8, TD8                                                 | T0067500A | 1    |
| 7              | Kondensatablaufwinkel                                                                         | WTC02971  | 1    |
| 50             | Anti-Vibrationsfuß                                                                            | A0261100A | 4    |
| 67             | Propeller / Ventilator                                                                        | WTC03955  | 1    |
| 77             | Set Fixierscheiben für Stutzen                                                                | R06415    | 1    |
| E              | Anschluss-Stück Kondensator oben (mit Abzweig)                                                | A0358000A | 1    |
| F              | Anschluss-Stück Kondensator unten (ohne Abzweig)                                              | A0357800A | 1    |
| 78             | Halbverschraubung (Paar) 1 ½", 50 mm inkl. Dichtung                                           | W20RDU    | 2    |
| 79             | Flachdichtung für Halbverschraubung 1 ½", 50 mm                                               | WNS03428  | 2    |
|         | Reparaturset für Kondensator / Tauchhülse                                                     | R0890200  | 1    |
|         | Verschlusskappe für Kondensatoranschlüsse (gelb außen = WPC02908 / milchig innen = DWPC02908) | DWPC02908 | 2    |
|         | Befestigungsclips für Plastikteile                                                            | M0042300A | 10   |
|          | Befestigungsclips für Metallteile                                                             | M0042400A | 2    |
|          | Auffangwanne mit Ablaufwinkel                                                                 | R07240    | 1    |
|         | Wandhalterung für Bedieneinheit                                                               | WH000201  | 1    |
|          | Umbausatz Indoor                                                                              | WH000202  | 1    |
|          | Abdeckhaube                                                                                   | R07096    | 1    |
|          | Reinigungsmittel 5L                                                                           | WMA03491  | 1    |
|          | Reinigungsmittel in Sprühflaschen (Set mit 5 x 50 ml)                                         | R06147    | 1    |
