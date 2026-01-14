# Osa 7 – SHL:n kerrosmalli visuaalisena kaaviona

SHL FRAMEwork rakentuu useista kerroksista, joilla jokaisella on selkeä vastuu.  
Tämä kaavio esittää koko arkkitehtuurin yhdellä silmäyksellä – ylhäältä (UI) alas (ydinlogiikkaan).

```text
┌──────────────────────────────────────────────────────────────┐
│                          UI-KERROS                           │
│                                                              │
│  • Flet UI                                                   │
│  • CLI UI                                                    │
│  • Web UI                                                    │
│  • Mobiili UI                                                │
│                                                              │
│  → Vastaa esitystavasta                                      │
│  → Ei sisällä semantiikkaa                                   │
└──────────────────────────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│                        ADAPTERI-KERROS                       │
│                                                              │
│  • Muuntaa semanttiset elementit UI-komponenteiksi           │
│  • Eristää UI-teknologian SHL:n ytimestä                     │
│  • Mahdollistaa framework-agnostisuuden                      │
│                                                              │
│  → “Kääntäjä” semantiikan ja käyttöliittymän välillä         │
└──────────────────────────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│                    SEMANTTINEN REKISTERI                     │
│                                                              │
│  • Yhteinen sanasto ja merkitysten tietokanta                │
│  • UI-elementtien tarkoitukset, toiminnot ja roolit          │
│  • Sovelluksen “kielioppi”                                   │
│                                                              │
│  → Määrittelee mitä asiat *tarkoittavat*                     │
└──────────────────────────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│                        HEALING-KERROS                        │
│                                                              │
│  • Havaitsee puuttuvat rakenteet                             │
│  • Luo oletusarvot                                           │
│  • Korjaa ristiriidat                                        │
│  • Tallentaa muutokset pysyvästi                             │
│                                                              │
│  → Järjestelmän itseparantuva ydin                           │
└──────────────────────────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│                       DATA / PERSISTENCE                     │
│                                                              │
│  • JSON-kielitiedostot                                       │
│  • Tietokanta (esim. Jeevesin moduulit)                      │
│  • Konfiguraatiot                                            │
│                                                              │
│  → Tallentaa kaiken, mitä healing ja semantiikka tuottavat   │
└──────────────────────────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│                        YDINLOGIIKKA                          │
│                                                              │
│  • Sovelluksen varsinainen toiminnallisuus                   │
│  • Ei sisällä UI-riippuvuuksia                               │
│  • Käyttää semanttista rekisteriä ja healingiä               │
│                                                              │
│  → Sovelluksen “aivot”                                       │
└──────────────────────────────────────────────────────────────┘
```

## Kerrosmallin idea tiivistettynä

- **UI** näyttää asiat  
- **Adapterit** muuntavat asiat  
- **Semanttinen rekisteri** määrittelee mitä asiat *tarkoittavat*  
- **Healing** korjaa ja täydentää asiat  
- **Data** tallentaa asiat  
- **Ydinlogiikka** käyttää asioita

Tämä kerrosmalli tekee SHL frameworkista:

- modulaarisen  
- itseparantuvan  
- framework‑agnostisen  
- turvallisen  
- ja pitkäikäisen arkkitehtuurin
