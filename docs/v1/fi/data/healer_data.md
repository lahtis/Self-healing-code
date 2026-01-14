# Healer-lokit ja muisti – Datan rakenne ja arkistointi

Tämä dokumentti kuvaa, miten SHL-järjestelmä tallentaa "kokemuksensa". Healerin toiminta perustuu siihen, että jokainen onnistunut ja epäonnistunut korjausyritys muuttaa järjestelmän sisäistä tilaa ja parantaa sen tulevaa tarkkuutta.

## 1. HealerMemory: Oppimisen tallennuspaikka

`HealerMemory` on järjestelmän tilastollinen aivo. Se tallennetaan JSON-muodossa, jotta se on helppo ladata ja analysoida.

### Datan rakenne (`memory.json`)
Muistitiedosto sisältää numeerista dataa eri hakuheuristiikkojen onnistumisesta:

- **Success/Fail laskurit:** Pitävät kirjaa siitä, kuinka monta kertaa `text`, `type` tai `context` -pohjainen haku on toiminut.
- **Confidence (Luottamus):** Dynaamisesti laskettu arvo (onnistumiset / yritykset). Healer priorisoi metodeja, joilla on korkein confidence.
- **Selector History:** Lista viimeisimmistä hyväksytyistä selektoreista, jotka Healer on löytänyt korvauksena rikkoutuneille ID-tunnuksille.

---

## 2. Arkistointilogiikka (Versioning)

SHL:n muistinhallinta on suunniteltu tutkimuskäyttöön, jossa "oppimiskäyrän" seuranta on kriittistä.

### Automaattinen arkistointi:
Aina kun `save()`-metodia kutsutaan ja tiedosto on muuttunut, järjestelmä suorittaa seuraavan syklin:
1. **Timestamp:** Luodaan aikaleima (esim. `2026-01-14_11-30-00`).
2. **Rename:** Nykyinen `memory.json` siirretään arkistoon nimellä `memory_TIMESTAMP.json`.
3. **Write:** Tallennetaan uusi, päivitetty tila `memory.json`-tiedostoon.

Tämä varmistaa, ettei dataa koskaan ylikirjoiteta lopullisesti, ja mahdollistaa paluun aiempaan "viisaustasoon", jos järjestelmä alkaa tehdä vääriä korjauksia (overfitting).

---

## 3. HealerLogger: Auditointi ja diagnostiikka

Siinä missä `Memory` tallentaa tilastoja, `Logger` tallentaa konkreettisia tapahtumia. Jokainen "Heal Attempt" tuottaa lokimerkinnän.

### Lokimerkinnän sisältö:
- **Target ID:** Komponentti, jota yritettiin korjata.
- **Method Used:** Mitä heuristiikkaa käytettiin (esim. `find_by_text`).
- **Old Selector:** Alkuperäinen, rikkoutunut tekninen tunniste.
- **New Selector:** Healerin löytämä uusi, toimiva tunniste.
- **Timestamp:** Milloin korjaus tapahtui.

Tämä loki on elintärkeä **Patch-automaatiolle**: sen perusteella järjestelmä voi ehdottaa päivityksiä suoraan `ui_schema.json` -tiedostoon.

---

## 4. Datan elinkaari (Lifecycle)

1. **Generation:** `FormEngine` havaitsee virheen $\rightarrow$ `HealerEngine` tuottaa ratkaisun.
2. **Logging:** Korjaustapahtuma kirjataan `HealerLoggerin` kautta.
3. **Updating:** `HealerMemory` päivittää tilastot ja tallentaa ne levylle.
4. **Archiving:** Vanha muisti siirretään `/archive`-kansioon.
5. **Analysis:** `HealerStats` lukee muistia ja lokia tuottaakseen tarkkuusraportteja.

---

## 5. Kehityskohteet (Roadmap)
- **Log Rotation:** Toteutetaan mekanismi, joka pakkaa vanhat lokitiedostot tilan säästämiseksi.
- **Visual Analytics:** Kehitetään työkalu, joka piirtää kuvaajia `HealerStats`-datasta suoraan GitHub-sivulle.
