# Kielioppisäännöt & Morfologinen normalisointi

Tämä dokumentti määrittelee SHL-järjestelmän kielellisen älyn perusteet. Suomen kieli on rakenteeltaan agglutiininen (sanoihin liitetään päätteitä), mikä tekee perinteisestä tekstintunnistuksesta haastavaa. SHL ratkaisee tämän morfologisella normalisointiprosessilla.

## 1. Miksi kielellinen äly?

Perinteiset UI-automaatiotyökalut perustuvat tarkan merkkijonon vastaavuuteen (Exact Match). Jos Healer etsii nappia "Tallenna", mutta käyttöliittymässä lukeekin "Tallennat" tai "Tallennetaan", tavallinen algoritmi antaa tulokseksi 0 % vastaavuuden. 

SHL:n kielimoottori ymmärtää, että näiden kaikkien sanojen **semanttinen juuri** on sama, ja sallii dynaamisen korjauksen kielellisistä muutoksista huolimatta.



---

## 2. Vokaalisointu (Vowel Harmony)

Suomen kielessä vokaalit jaetaan etu- (ä, ö, y) ja takavokaaleihin (a, o, u). Tämä vaikuttaa siihen, mitä päätteitä sanaan voidaan liittää (neutraalit vokaalit i ja e käyvät molempien kanssa).

- **Sääntö:** Jos sanassa on takavokaaleja, pääte on muotoa *-ssa* tai *-lla*. Jos sanassa on vain etuvokaaleja (tai neutraaleja), pääte on *-ssä* tai *-llä*.
- **Normalisointi:** Healer osaa tunnistaa päätteen tyypin vokaalisoinnun perusteella ja "kuoria" sen pois löytääkseen sanan perusmuodon.
    - *Esimerkki:* "Pankissa" -> "Pankki", "Metsässä" -> "Metsä".

---

## 3. Astevaihtelu (Consonant Gradation)

Sanan sisäiset konsonantit (k, p, t) muuttuvat taivutettaessa vahvan ja heikon asteen välillä. Tämä on kriittinen vaihe normalisoinnissa.

- **Kuvio:** Healer sisältää säännöt yleisimmille vaihteluille (esim. kk -> k, pp -> p, tt -> t).
- **Esimerkki:**
    - Skeemassa määritelty: `pankki`
    - Ruudulla havaittu: `pankin`
    - **Logiikka:** Healer tunnistaa "n"-päätteen (genetiivi) ja tietää, että "k" on "kk":n heikko aste. Järjestelmä palauttaa vahvan asteen vertailua varten.



---

## 4. Normalisointiprosessi (The Pipeline)

Kun Healer skannaa ruutua, jokainen löytynyt teksti kulkee seuraavan putken läpi ennen lopullista pisteytystä:

1. **Lowercasing:** Poistetaan kirjaskoon vaikutus (esim. "TALLENNA" -> "tallenna").
2. **Suffix Stripping:** Tunnistetaan ja poistetaan yleisimmät päätteet (ssa/ssä, lla/llä, n, t, ssa/stä).
3. **Consonant Restoration:** Palautetaan mahdolliset astevaihtelut (esim. heikko aste -> vahva aste).
4. **Fuzzy Scoring:** Verrataan puhdistettua tulosta `ui_schema.json`:n ja `localization.json`:n avaimiin.

---

## 5. Pisteytys ja painotus (Scoring Rules)

Healer ei tee "kyllä/ei"-päätöksiä, vaan laskee vastaavuuden todennäköisyyden:

| Vastaavuus | Tyyppi | Pisteet | Esimerkki |
| :--- | :--- | :--- | :--- |
| **Exact** | Täydellinen match | 1.0 | "Tallenna" == "Tallenna" |
| **Stem** | Vartalo täsmää | 0.8 | "Pankissa" -> "Pankki" |
| **Gradation** | Astevaihtelumatch | 0.7 | "Pankin" -> "Pankki" |
| **Partial** | Yhdyssanan osa | 0.5 | "Käyttäjänimi" sisältää sanan "nimi" |



---

## 6. Nykytila ja tulevaisuus (WIP)

Tämä kielimoottori on parhaillaan integraatiovaiheessa osaksi `HealerEngineä`. 

**Tulevaisuuden kehityskohteet:**
- Täysiverinen morfologinen analysaattori (esim. integrointi Voikko- tai Omorfi-kirjastoihin).
- Yhdyssanojen automaattinen purku ja semanttinen analyysi.
- Kontekstuaalinen ymmärrys (esim. tunnistaa, että "Lisää" ja "Uusi" voivat samassa kontekstissa tarkoittaa samaa toimintoa).
