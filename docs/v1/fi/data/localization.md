# Lokalisaatiotiedostot – JSON- ja .po-tallennus

SHL-järjestelmä käyttää hybridimallia lokalisoinnin hallintaan. Tämä mahdollistaa kielellisen datan helpon muokattavuuden, automaattisen päivityksen ja tehokkaan lukemisen ajon aikana.

## 1. Kaksi tiedostomuotoa, yksi tavoite

Järjestelmä tukee kahta eri formaattia eri käyttötarkoituksiin:

### A. JSON (.json) – Koneellinen suorituskyky
JSON on järjestelmän ensisijainen ajoaikainen muoto. Se on nopea lukea ja se mäppäytyy suoraan Pythonin sanakirjoiksi (dict).
- **Käyttö:** `LanguageManager` lataa nämä tiedostot käynnistyksen yhteydessä.
- **Rakenne:** Hierarkkinen avain-arvo-rakenne (esim. `{"user": {"label": "Käyttäjä"}}`).

### B. Gettext (.po) – Kääntäjän työkalut
`.po`-tiedostot ovat teollisuusstandardi ohjelmistokäännöksissä. Ne mahdollistavat ammattimaisten käännöstyökalujen (kuten Poedit tai Weblate) käytön.
- **Käyttö:** Kehittäjät ja kääntäjät muokkaavat näitä.
- **Etu:** Tukee kontekstia, monikkomuotoja ja metatietoja käännöksistä.



---

## 2. Tallennuslogiikka ja automaatio

SHL:n uniikki ominaisuus on **itseoppiva lokalisaatiovarasto**. Kun `HealerEngine` tunnistaa uuden kielellisen termin tai korjaa puuttuvan avaimen, järjestelmä voi päivittää tiedostot automaattisesti.

### Tallennusprosessi:
1. **Muutos:** Healer havaitsee uuden termin (esim. käyttäjän itse luoma osoitenimi).
2. **Normalisointi:** `LanguageManager` puhdistaa tekstin (vokaalisointu, välimerkit).
3. **Päivitys:** - Uusi avain lisätään JSON-välimuistiin.
    - Jos asetettu, järjestelmä generoi uuden entryn `.po`-tiedostoon kääntäjää varten.
4. **Validointi:** Järjestelmä varmistaa, ettei uusi avain riko olemassa olevia skeemoja.

---

## 3. Tiedostojen rakenne-esimerkki

### `lang_fi.json`
```json
{
  "action_button": {
    "label": "Tallenna",
    "tooltip": "Tallenna muutokset tietokantaan"
  },
  "user_name": {
    "label": "Käyttäjänimi"
  }
}
```

### `messages.po`
```json
msgid "action_button.label"
msgstr "Tallenna"

#. Context: Tooltip for the main action button
msgid "action_button.tooltip"
msgstr "Tallenna muutokset tietokantaan"
```

---

## 4. Healer ja "User-Created Keys"
Tutkimuksessa on tärkeää huomioida käyttäjän omat syötteet. Kun järjestelmään lisätään uusia osoitteita tai personoituja kenttiä:
* SHL tallentaa nämä "avainkielenä" (`key language`).
* Jos käyttäjä nimeää kentän "`Koti-osoite`", `Healer` tallentaa sen lokalisaatiovarastoon.
* Seuraavalla kerralla `Healer` tunnistaa tämän kentän, vaikka sen tekninen `ID` muuttuisi, koska se löytyy jo tunnetuista kielellisistä avaimista.

---

## 5. Järjestelmän nykytila ja kehitysvaiheet (WIP)

Vaikka SHL:n arkkitehtuuri on suunniteltu hybridimallia varten, on tärkeää huomioida toteutuksen nykyinen vaihe:

### 🟢 Käytössä (Production Ready)
- **JSON-pohjainen lokalisaatio:** Kaikki ajoaikainen haku, Healer-korjaukset ja `LanguageManager`-logiikka toimivat JSON-tiedostojen varassa.
- **Automaattinen päivitys:** Healer osaa päivittää JSON-varastoa lennosta.

### 🟡 Työn alla (Work in Progress)
- **.po-tiedostojärjestelmä:** Järjestelmä on suunniteltu Gettext-yhteensopivaksi, mutta automaattinen synkronointi JSON- ja .po-tiedostojen välillä on vielä kehitysvaiheessa.
- **Kääntäjän integraatio:** Tällä hetkellä .po-tiedostot on generoitu manuaalisesti tai ulkoisilla skripteillä; tavoitteena on saumaton, kaksisuuntainen integraatio, jossa kääntäjän tekemät muutokset valuvat suoraan Healerin käyttöön.

---

## 6. Vinkkejä ylläpitoon
- **Puhdistus:** Aja säännöllisesti skripti, joka poistaa `JSON`-tiedostoista avaimet, joita ei enää löydy `ui_schema.json`-tiedostosta.
- **Varmuuskopiot:** Healerin tekemät automaattiset päivitykset arkistoidaan aina aikaleimalla (vrt. `HealerMemory.save`).
- **Koodaus:** Käytä aina `UTF-8` koodausta, jotta ääkköset ja kielelliset erikoismerkit säilyvät oikein.
