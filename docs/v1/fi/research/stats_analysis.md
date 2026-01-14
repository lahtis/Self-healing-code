# Suorituskyky ja Stats (Statistical Analysis)

Tämä dokumentti määrittelee, miten SHL-järjestelmän tehokkuutta ja luotettavuutta mitataan. Pelkkä itseparannus ei riitä; meidän on pystyttävä osoittamaan datan avulla, kuinka tarkasti ja nopeasti järjestelmä oppii.

## 1. Keskeiset suorituskykymittarit (KPIs)

Seuraamme kolmea päämittaria jokaisen testiajon ja korjaustilanteen yhteydessä:

### A. Recovery Rate (Palautumisaste)
Lasketaan, kuinka monta prosenttia rikkoutuneista komponenteista Healer pystyi korjaamaan automaattisesti ilman ihmisen interventiota.
* **Kaava:** $(Onnistuneet Korjaukset / Kaikki Virhetilanteet) * 100$

### B. Mean Time to Heal (MTTH)
Aika, joka kuluu virheen havaitsemisesta siihen, että `FormEngine` on saanut uuden validin selektorin ja jatkaa toimintaansa.
* **Tavoite:** < 500ms (verrattuna manuaaliseen korjaamiseen, joka kestää minuutteja tai tunteja).

### C. False Positive Rate
Kuinka usein Healer teki "korjauksen", joka oli teknisesti väärä (esim. painoi väärää nappia). Tätä valvotaan `Type Integrity` -säännöillä.



---

## 2. HealerMemoryn tilastollinen analyysi

`HealerStats`-luokka lukee `memory.json`-tiedostoa ja tuottaa analyysin eri metodien luotettavuudesta:

| Metodi | Painoarvo (Initial) | Todellinen onnistuminen | Confidence Score (Lopullinen) |
| :--- | :--- | :--- | :--- |
| **Exact Text Match** | 1.0 | 95% | **0.95** |
| **Morphological Match** | 0.8 | 88% | **0.70** |
| **Type & Order Match** | 0.4 | 60% | **0.24** |

**Havainto:** Jos `Morphological Match` (vokaalisointu jne.) tuottaa jatkuvasti korkeita pisteitä, järjestelmä nostaa sen prioriteettia suhteessa teknisiin selektoreihin.

---

## 3. Oppimiskäyrän visualisointi

Järjestelmä arkistoi muistia aikaleimoilla (`memory_TIMESTAMP.json`). Tämä mahdollistaa oppimiskäyrän seuraamisen:
1. **Cold Start:** Ensimmäiset ajot, jolloin Confidence-arvot ovat matalia.
2. **Learning Phase:** Healer kerää lokidataa ja vahvistaa kielellisiä sääntöjä.
3. **Stable State:** Järjestelmä on saavuttanut tason, jossa se tunnistaa komponentit lähes 100% varmuudella, vaikka UI-kirjasto vaihtuisi.



---

## 4. Raportointi (HealerLogger Export)

Jokaisen tutkimusjakson päätteeksi `HealerLogger` generoi koosteen, joka sisältää:
* **Audit Log:** Lista kaikista tehdyistä "temp-fixeistä".
* **Linguistic Hits:** Mitkä vokaalisoinnun tai astevaihtelun säännöt olivat aktiivisimpia.
* **Bottlenecks:** Tilanteet, joissa Healer joutui pyytämään apua (Confidence < 0.5).

---

## 5. Tutkimuksen uutuusarvo (Scientific Contribution)

Tämä data todistaa, että **kielellinen konteksti (Semantic Context)** on vakaampi ankkuri käyttöliittymäautomaatiossa kuin tekniset ID-tunnukset. Tilastot osoittavat, että vaikka ID-tunnukset muuttuvat usein, komponenttien tarkoitus ja kielellinen esitysmuoto säilyvät vakaina.
