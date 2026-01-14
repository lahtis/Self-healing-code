# Osa 1 – Ensimmäiset Python‑kokeilut ja Digital Guestbook

Kun varhainen CLI‑projekti oli jäänyt tauolle, seuraava askel oli siirtyä Pythonin pariin.  
Tämä vaihe ei vielä ollut SHL:ää, mutta se oli ensimmäinen konkreettinen yritys rakentaa järjestelmä, joka ymmärtää rakenteita ja semantiikkaa paremmin kuin perinteinen kovakoodattu UI.

## Digital Guestbook – ensimmäinen UI‑kokeilu

Ensimmäinen todellinen Python‑projekti oli Digital Guestbook.  
Se oli yksinkertainen, mutta tärkeä kokeilu:

- käyttöliittymä rakennettiin pala palalta  
- lokalisointi tehtiin käsin  
- rakenteet olivat hajallaan  
- ja jokainen muutos piti tehdä useaan paikkaan  

Tämä projekti paljasti ensimmäisen suuren kipupisteen:

**kielitiedostojen ylläpito oli hidasta, virhealtista ja epäkäytännöllistä.**

Juuri tämä ongelma synnytti ensimmäisen pienen apuskriptin.

## Ensimmäinen tarkistusskripti – pieni työkalu, suuri vaikutus

Digital Guestbookin aikana syntyi tarve tarkistaa, löytyvätkö kaikki `loc.L("avain")`‑kutsut JSON‑kielitiedostosta.  
Tähän tehtiin yksinkertainen Python‑skripti, joka:

- luki koodin  
- etsi kaikki lokalisointiavaimet  
- vertasi niitä JSON‑tiedostoon  
- listasi puuttuvat avaimet  

Tämä skripti oli pieni, mutta se paljasti nopeasti, että ongelma ei ollut vain puuttuvissa avaimissa.  
Ongelma oli koko tavassa, jolla lokalisointi oli sidottu UI:hin.

## Ensimmäinen Localizer – oppiva lokalisointimoottori

Seuraava askel oli rakentaa `Localizer`‑luokka, joka:

- luki kielikoodin configista  
- latasi oikean JSON‑tiedoston  
- loi puuttuvat avaimet automaattisesti  
- ja toimi ensimmäisenä “oppivana” komponenttina

Tämä oli ensimmäinen hetki, jolloin projekti alkoi muistuttaa arkkitehtuuria, ei vain skriptiä.

## Oivallus: tästä voi kasvaa jotain suurempaa

Kun Localizeria yritettiin liittää Jeevesiin, syntyi tärkeä oivallus:

**lokalisointi ei ole vain käännöksiä – se on osa UI:n semanttista rakennetta.**

Tämä ajatus oli ensimmäinen askel kohti SHL FRAMEworkin filosofiaa.


Hetki, jossa pienet työkalut alkoivat kasvaa kohti suurempaa kokonaisuutta.
