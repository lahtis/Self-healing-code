# Testiskenaariot (Research Test Scenarios)

Tässä dokumentissa kuvataan skenaariot, joilla SHL-järjestelmän suorituskykyä ja itseparannuskykyä testataan. Skenaariot on suunniteltu simuloimaan todellisia ohjelmistomuutoksia ja virhetilanteita.

## Skenaario 1: Tekninen tunniste muuttuu (ID Breakage)

Tämä on yleisin virhetilanne käyttöliittymäautomaatiossa.

- **Lähtötilanne:** Sovelluksessa on painike, jonka ID on `btn_save_01`.
- **Muutos:** Kehittäjä päivittää koodia ja uusi ID on `save_action_final`.
- **Healer-toiminta:** 1. Healer havaitsee, ettei `btn_save_01` löydy.
    2. Se skannaa UI-puun ja löytää painikkeen, jonka tekstiavain viittaa sanaan "Tallenna".
    3. Se tarkistaa `ui_schema.json`:sta, että tyyppi (Button) täsmää.
- **Onnistumiskriteeri:** Testi jatkuu keskeytyksettä uuden ID:n avulla.



---

## Skenaario 2: Kielellinen taivutus ja lokalisointi (Linguistic Shift)

Tämä skenaario testaa `Morphology Enginen` ja vokaalisoinnun toimivuutta.

- **Lähtötilanne:** Testi etsii kenttää nimellä "Katuosoite".
- **Muutos:** Sovelluksen kieli on vaihdettu muotoon, jossa käytetään omistusliitteitä tai taivutusta (esim. "Katuosoitteesi" tai "Katuosoitteen tiedot").
- **Healer-toiminta:**
    1. `Exact Match` epäonnistuu.
    2. Healer ajaa tekstin normalisointiputken läpi.
    3. `Suffix Stripping` poistaa "si"-päätteen.
    4. `Stem Match` löytää vastaavuuden (0.8 pistettä).
- **Onnistumiskriteeri:** Järjestelmä tunnistaa kentän oikeaksi kielellisestä muutoksesta huolimatta.

---

## Skenaario 3: Frameworkin vaihto (Cross-Platform Migration)

Tämä on järjestelmän äärimmäinen testi, joka mittaa `UI Adaptereiden` ja `Middlemanien` eristyskykyä.

- **Lähtötilanne:** Lomake on toteutettu PyQt6-työpöytäsovelluksena.
- **Muutos:** Sama lomake siirretään Flet-pohjaiseen web-sovellukseen. Elementtien tekniset rakenteet (DOM vs. Qt Widgets) ovat täysin erilaiset.
- **Healer-toiminta:**
    1. Järjestelmä käyttää `Tree Builderia` lukemaan uuden ympäristön rakenteen.
    2. Se vertaa komponenttien semanttisia tarkoituksia (Middleman-kytkennät) uuteen näkymään.
- **Onnistumiskriteeri:** Data täytetään oikeisiin kenttiin uudessa frameworkissa ilman, että testilogiikkaa tai datamallia muutetaan.

---

## Skenaario 4: Käyttäjän itseluoma avainkieli

Tämä skenaario on tärkeä tutkimuksen "middleman"-idean kannalta.

- **Lähtötilanne:** Käyttäjä lisää järjestelmään uuden osoitteen nimellä "Mummon mökki".
- **Muutos:** Sovellus päivittyy ja osoitteen näyttävä listaelementti muuttaa rakennettaan.
- **Healer-toiminta:**
    1. Healer hakee `LanguageManagerin` muistista käyttäjän aiemmin tallentaman avainsanan "Mummon mökki".
    2. Se etsii ruudulta tätä nimenomaista tekstiä.
- **Onnistumiskriteeri:** Järjestelmä löytää dynaamisesti luodun elementin, vaikka se ei ollut alkuperäisessä staattisessa skeemassa.

---

## Mittarit (Metrics)

Jokaisesta skenaariosta kerätään seuraavat tiedot `HealerStats`-tiedostoon:
1. **Time to Heal:** Kuinka monta millisekuntia korjaus kesti.
2. **Confidence Score:** Millä varmuudella korjaus tehtiin.
3. **Method Priority:** Mikä heuristiikka (Text, Type, Context) ratkaisi tilanteen.
