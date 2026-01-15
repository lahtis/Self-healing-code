# SHL UI Schema — Version 1

Tämä hakemisto sisältää SHL‑järjestelmän käyttöliittymäskeeman ensimmäisen version.  
Skeema määrittelee, millaisia UI‑komponentteja järjestelmässä on ja miten ne käyttäytyvät eri kerroksissa.

## Skeeman tarkoitus

UI‑skeema toimii koko SHL‑järjestelmän perustana:

- määrittelee komponenttien rakenteen  
- kuvaa tekstikentät (`text_keys`)  
- määrittelee framework‑kohtaiset toteutukset (`implementations`)  
- sisältää metatietoa, jota healer ja middleman hyödyntävät  
- toimii SHLComponent‑luokan tietolähteenä  

Skeema on siis SHL:n “UI‑sanakirja” ja “UI‑grammatiikka”.

## Rakenne

Tämä hakemisto sisältää:

- **ui_schema.json**  
  – pääskeema, joka määrittelee kaikki komponentit  
- mahdolliset tulevat versiot tai laajennukset  
- komponenttikohtaiset lisäselitteet (jos niitä lisätään myöhemmin)

## Skeeman käyttö

Skeemaa käyttävät:

- **SHLComponent**  
  – lataa komponentin määritelmän skeemasta  
- **middleman**  
  – rakentaa UI‑puun skeeman pohjalta  
- **healer**  
  – tekee korjauksia skeeman sääntöjen mukaan  
- **adapterit**  
  – renderöivät komponentit framework‑kohtaisesti

## Tulevat laajennukset

Tulevaisuudessa tänne voidaan lisätä:

- skeeman versio 2 (v2)  
- komponenttikohtaiset lisäattribuutit  
- laajennettu metadata (layout, accessibility, behavior)  
- skeeman validointityökalut  
- automaattisesti generoitu dokumentaatio komponenteista

Tämä hakemisto toimii UI‑kerroksen perustana ja määrittelee, miten SHL ymmärtää käyttöliittymän rakenteen.
