# Sanasto (Vocabulary)

Tämä sivu selittää SHL-järjestelmässä käytetyt keskeiset termit ja käsitteet. Termistö on osittain englanninkielinen ohjelmistokehityksen standardien mukaisesti, mutta niiden merkitys on määritelty SHL-arkkitehtuurin näkökulmasta.

## A
* **Adapter (UI Adapter):** Kerros, joka muuttaa abstraktin komponenttimääritelmän konkreettiseksi widgetiksi (esim. Flet tai PyQt6).
* **Audit Trail:** HealerLoggerin tuottama historiatieto kaikista suoritetuista korjausyrityksistä ja niiden onnistumisista.

## C
* **Confidence (Luottamusarvo):** HealerMemoryn laskema tilastollinen arvo (0.0–1.0), joka kertoo, kuinka luotettavana järjestelmä pitää tiettyä korjausmetodia.

## E
* **Engine (FormEngine):** Järjestelmän keskeinen orkestraattori, joka hallitsee lomakkeiden rakentamista, datan syöttämistä ja kielen vaihtamista.

## G
* **Grammatical Engine:** Kielellinen komponentti, joka ymmärtää suomen kielen sääntöjä (vokaalisointu, astevaihtelu) ja auttaa tunnistamaan tekstipohjaisia komponentteja.

## H
* **Healer (HealerEngine):** Järjestelmän itseparannusyksikkö, joka etsii ja korjaa rikkoutuneet käyttöliittymäyhteydet.
* **Heuristic (Heuristiikka):** Sääntö tai menetelmä (esim. tekstihaku tai tyyppihaku), jota Healer käyttää etsiessään kadonnutta komponenttia.

## I
* **Intent (Tarkoitus):** Komponentin semanttinen merkitys (esim. "tallenna-toiminto"), joka pysyy samana, vaikka tekninen toteutus muuttuisi.

## L
* **LanguageManager:** Komponentti, joka hallitsee lokalisaatiotiedostoja (.json, .po) ja hoitaa dynaamisen kielenkäännöksen.

## M
* **Middleman (Keskimies):** Datamuunnin, joka toimii puskurina raakadatan (esim. User-objekti) ja UI-komponentin välillä.
* **Morfologia:** Kielitieteen osa-alue, joka tutkii sanojen muotoja ja taivutusta; SHL:n kielellisen älyn perusta.

## N
* **Node (UINode):** Yksittäinen elementti UI-puussa (Tree), joka sisältää tiedot elementin tyypistä, tekstistä ja sijainnista.

## S
* **Schema (UI-Skeema):** JSON-tiedosto, joka toimii "Single Source of Truth" -lähteenä kaikille käyttöliittymän komponenteille.
* **Selector (Selektori):** Tekninen tunniste (esim. ID, XPath tai CSS-polku), jolla ohjelmisto löytää elementin käyttöliittymästä.
* **Semantic Stability:** SHL:n tavoitetila, jossa sovellus pysyy toiminnallisena, vaikka sen tekninen rakenne muuttuu.

## T
* **Tree Builder:** Työkalu, joka skannaa aktiivisen käyttöliittymän ja rakentaa siitä hierarkkisen puun itseparannusta varten.

## V
* **Vowel Harmony (Vokaalisointu):** Suomen kielen sääntö, joka määrittää sanan päätteet vokaalien mukaan; kriittinen osa SHL:n tekstintunnistusta.
