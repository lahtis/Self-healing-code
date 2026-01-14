# UI-Skeema (V1) – Komponenttien määrittely

SHL-järjestelmä on tietomalli-ohjattu (`Data-driven`). Tämä tarkoittaa, että käyttöliittymää ei kovakoodata, vaan se määritellään `JSON`-pohjaisessa skeematiedostossa. Tämä dokumentti selittää skeeman rakenteen ja sen eri kenttien tarkoituksen.

## 1. Skeeman perusrakenne

Skeematiedosto sijaitsee polussa `[shl/ui/schema/v1/ui_schema.json]`. Sen ylin taso sisältää versiotiedot ja listan komponenteista.

```json
{
  "$schema": "[https://shl.dev/schema/ui/v1](https://shl.dev/schema/ui/v1)",
  "version": "1.0.0",
  "components": [ ... ]
}
```

## 2. Komponentin anatomia
Jokainen komponentti koostuu neljästä pääalueesta:

### A. Tunnisteet (Identity)
* `id`: Uniikki merkkijono, jota `FormEngine` ja `Healer` käyttävät viittaamiseen.
* `shl_type`: Abstrakti tyyppi, joka kertoo komponentin tarkoituksen (esim. `TEXT_INPUT`, `BUTTON`, `DROPDOWN`).

### B. Tekstiavaimet (Text Keys)
Määrittää, mitkä tekstikentät ovat käännettävissä.
* `label`: Komponentin otsikko.
* `placeholder`: Ohjeteksti kentän sisällä.
* `tooltip`: Leijuva ohjeteksti.
* `error_required`: Virheilmoitus, jos kenttä on tyhjä.

### C. Toteutukset (Implementations)
Tämä on framework-kohtainen osio. Se kertoo adapterille, mitä teknistä luokkaa käytetään.
* `class`: Frameworkin oma luokan nimi (esim. `QLineEdit` tai `TextField`).
* `supports_feature`: Bool-arvo, joka kertoo tukeeko kyseinen kirjasto tiettyä ominaisuutta (esim. `supports_placeholder`).

### D. Metadata
Ohjaa järjestelmän sisäistä logiikkaa.
* `middleman_required`: Jos true, `FormEngine` kutsuu `MiddlemanManageria` ennen datan näyttämistä.
* `supports_language_manager`: Määrittää, kulkeeko teksti kielimoottorin läpi.
* `category`: Auttaa `Healer`-moottoria ryhmittelemään hakuja (esim. `input`, `action`, `selection`).

## 3. Esimerkki: Käyttäjänimen määrittely
Tässä on tyypillinen tekstisyötteen määrittely, joka hyödyntää `Middleman`-logiikkaa:

```json
{
  "id": "user_name",
  "shl_type": "TEXT_INPUT",
  "text_keys": {
    "label": "user_name.label",
    "placeholder": "user_name.placeholder"
  },
  "implementations": {
    "PyQt6": { "class": "QLineEdit" },
    "Flet": { "class": "TextField", "supports_label": true }
  },
  "metadata": {
    "middleman_required": true,
    "category": "input"
  }
}
```

## 4. Skeeman rooli Healer-prosessissa
Kun HealerEngine yrittää korjata rikkoutunutta käyttöliittymää, se käyttää tätä skeemaa referenssinä:
* 1. Jos `ID`:tä ei löydy, `Heale`r katsoo skeemasta, mikä `shl_type` ja `class` komponentilla pitäisi olla.
* 2. Se hakee `text_key`s-kohdan avaimet ja kysyy `LanguageManagerilta` niiden nykyiset käännökset.
* 3. Näiden tietojen avulla `Healer` voi tunnistaa "kadonneen" komponentin ruudulta, vaikka sen tekninen `ID` olisi muuttunut.
 
## 5. Parhaat käytännöt
* 1. Pienet `ID`:t: Käytä selkeitä, kuvaavia ID-nimeämisiköitä (esim. `submit_btn` eikä `button1`).
* 2. Kieliavainten nimeäminen: Käytä piste-notaatiota (`komponentti.kenttä`), jotta `.po` ja `.json` käännöstiedostot pysyvät järjestyksessä.
* 3. Framework-testaus: Varmista aina, että lisätty `class` löytyy vastaavasta `UIAdapterista`.
 
     
