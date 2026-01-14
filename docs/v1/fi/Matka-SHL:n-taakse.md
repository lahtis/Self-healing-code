# SHL – Syntytarina

# 0. Matka SHL:n taakse – Sisällysluettelo

Tämä tarina kuvaa SHL:n syntyä, kehitystä ja filosofiaa.  
Osat etenevät kronologisesti ja muodostavat yhtenäisen kokonaisuuden.

- [Osa 0 – Ennen Pythonia](journey/osa-0.md)
- [Osa 1 – Ensimmäiset Python-kokeilut](journey/osa-1.md)
- [Osa 2 – Arkkitehtuurin synty ja Localizerin irrottaminen](journey/osa-2.md)
- [Osa 3 – Jeevesin uusi aikakausi ja turvallisuuskerrokset](journey/osa-3.md)
- [Osa 4 – Siirtymävaihe: Tekniikasta filosofiaan](journey/osa-4.md)
- [Osa 5 – SHL:n nimeäminen ja identiteetin synty](journey/osa-5.md)
- [Osa 6 – Tulevaisuuden visio](journey/osa-6.md)
- [Osa 7 – SHL:n periaatteet tiivistettynä](journey/osa-7.md)
- [Osa 8 – Kerrosmalli visuaalisena kaaviona](journey/osa-8.md)
- [Osa 9 – Kerrosmallin selitys esimerkin kautta](journey/osa-9.md)

---

## 1. Jeeves – ensimmäinen kipinä
SHL juuret ovat Jeevesissä, pienessä RSS‑daemonissa, jonka käyttöliittymät oli tarkoitus rakentaa erikseen. Jeeves herätti yhden keskeisen kysymyksen:

**Voisiko järjestelmä ymmärtää käyttäjän tarkoituksen, ei vain koodia?**

Tämä ajatus jäi elämään ja muodosti pohjan myöhemmälle kehitykselle.

## 2. Digital Guestbook – ensimmäinen UI‑kokeilu
Seuraava vaihe oli Digital Guestbook — kokeilu, jossa käyttöliittymää rakennettiin pala palalta.  
Tässä projektissa nousi esiin ensimmäinen todellinen kipupiste:

**Kielitiedostojen käsittely oli hidasta ja virhealtista.**

Tämä johti ensimmäisen modulaarisen työkalun syntyyn.

## 3. localization.py – ensimmäinen irrotettava komponentti
Guestbookin aikana syntyi tarve automatisoida kielitiedostojen generointi.  
Tavoitteena oli:

- havaita muutokset automaattisesti  
- luoda pohjat kaikille kielimalleille  
- tehdä kääntäjän työ helpoksi  
- välttää manuaalinen, toistuva työ  

Näin syntyi `localization.py`, ensimmäinen irrotettava ja uudelleenkäytettävä komponentti — ja samalla ensimmäinen siemen SHL:n kielikerrokselle.

## 4. Oivallus: tästä voisi tulla jotain suurempaa
Kun `localization.py`-skriptiä yritettiin liittää Jeevesiin, syntyi oivallus:

**Tämä ei ole enää yhden projektin apuskripti. Tästä voisi tulla oma pakettinsa.**

Tämä johti ensimmäiseen TestPyPI‑julkaisuun (0.0.1), joka ei toiminut.  
Pieni korjaus, versio 0.0.2, ja paketti alkoi elää.

Tämä oli hetki, jolloin SHL alkoi muuttua skriptistä kirjastoksi.

## 5. Mökkireissu – hiljainen hetki, joka muutti kaiken
Pian tämän jälkeen tuli mökkireissu.  
Ei konetta.  
Vain puhelin, metsä ja aikaa ajatella.

Kaksi päivää keskusteluja AI‑työkalujen kanssa, puhelimen näppäimistö sauhuten.  
Tässä vaiheessa syntyivät:

- ensimmäinen luonnos SHL:n arkkitehtuurista  
- ajatus healing‑syklistä  
- framework‑agnostiset adapterit  
- semanttisen rekisterin perusmuoto  
- dokumentaation pohja pilvipalveluun  

Mökin rauhassa projekti muuttui:

**skriptistä → kirjastoksi → arkkitehtuuriksi → filosofiaksi.**

## 6. Jeevesin uusi aikakausi – modulaarisuus, tietokanta ja turvallisuus

Ajan myötä Jeeves kehittyi merkittävästi alkuperäisestä RSS‑daemonista.  
Uusi versio on rakennettu modulaariseksi ja se käyttää tietokantaa pohjarakenteenaan.  
Tavoitteena oli tehdä Jeevesistä laajennettava, vakaa ja tulevaisuuden projekteihin sopiva alusta.

Kehitys ei kuitenkaan ollut suoraviivaista.  
Uusi Jeeves yritti aluksi integroida AI‑työkalut liian helposti ja liian suoraan, mikä johti nopeasti ongelmiin.  
Tämän seurauksena projektiin jouduttiin rakentamaan lähes “NASAn veroinen” kolmikerroksinen turvakerros, joka:

- eristää AI‑kutsut  
- validoi syötteet ja vastaukset  
- suojaa järjestelmää vääriltä tai vaarallisilta toiminnoilta  
- varmistaa, että Jeeves pysyy vakaana ja ennustettavana

Tämän vuoksi uutta Jeeves‑versiota ei ole vielä julkaistu omaan repoonsa.  
Se on edelleen kehitysvaiheessa, mutta sen arkkitehtuuri toimii tärkeänä osana SHL:n taustaa:  
se osoittaa, miksi semanttinen välikerros, adapterit ja turvallinen orkestraatio ovat niin tärkeitä.

Uusi Jeeves toimii nyt eräänlaisena testialustana, jossa SHL:n periaatteita voidaan kokeilla käytännössä ennen kuin ne päätyvät osaksi varsinaista frameworkia.


## 7. Lopputulos: SHL
SHL ei ole enää pelkkä lokalisointityökalu.  
Se on:

- framework‑agnostinen UI‑arkkitehtuuri  
- semanttinen välikerros  
- itseparantuva järjestelmä  
- kielitietoinen moottori  
- tapa erottaa intent toteutuksesta  

Kaikki tämä syntyi Pythonia opetellessa — mutta lopputulos näyttää siltä kuin sen olisi suunnitellut kokenut arkkitehti.
