## UITreePrinter

`ui_tree_printer.py` tarjoaa työkalun UINode‑pohjaisen käyttöliittymäpuun tulostamiseen.  
Sitä käytetään erityisesti debuggaamiseen ja UI‑puun rakenteen hahmottamiseen.

### Ominaisuudet

- Tulostaa UI‑puun sisennettynä ja luettavana
- Näyttää solmun:
  - tyypin
  - id‑arvon
  - tekstin
  - selectorin
- Tukee rekursiivista puun läpikäyntiä
- Sopii snapshot‑tarkasteluun ja testaukseen

### Esimerkki tulosteesta
* Button id='submit' text='Send'
* Icon id='arrow'

### Rooli SHL‑arkkitehtuurissa

- Middleman rakentaa UI‑puun  
- Healer voi muokata sitä  
- **UITreePrinter näyttää lopputuloksen selkeästi**  
- Auttaa kehittäjiä ymmärtämään, mitä UI‑puussa tapahtuu

### Tulevat laajennukset

- Värikoodaus (tyypit, muutokset, metadata)
- JSON‑muotoinen tuloste
- Diff‑integraatio UI‑solmujen muutosten korostamiseen
- Tulostus tiedostoon (snapshot‑logit)

UI‑puu on SHL‑järjestelmän keskeinen rakenne, ja sen ympärille voidaan rakentaa useita tulevia laajennuksia:

### 1. UI Tree Validator
- Tarkistaa UI‑solmujen rakenteen ja attribuutit  
- Estää virheelliset solmut ennen healer‑vaihetta  
- Toimii vastaparina registry‑ ja core‑validoinnille

### 2. UI Tree Metadata Layer
- Mahdollistaa solmukohtaisen metadatan (layout, behavior, accessibility)  
- Auttaa adaptereita ja healer‑kerrosta tekemään parempia päätöksiä  
- Luo pohjan tuleville UI‑ominaisuuksille

### 3. UI Tree Diff Integration
- Korostaa UI‑puun muutokset värikoodeilla tai symboleilla  
- Sopii snapshot‑testaukseen ja debuggaamiseen  
- Yhdistyy diff‑kerroksen raportteihin

### 4. UI Tree Snapshot System
- Tallentaa UI‑puun tilan tiedostoon  
- Mahdollistaa regressiotestauksen  
- Auttaa seuraamaan UI‑rakenteen evoluutiota

### 5. UI Tree Search & Query API
- Mahdollistaa solmujen hakemisen tyypin, id:n tai tekstin perusteella  
- Sopii testaukseen ja automaatioon  
- Luo pohjan tuleville analytiikkatyökaluille

### 6. Visual UI Tree Renderer
- Graafinen esitys UI‑puusta (esim. ASCII‑kaavio tai HTML‑visualisointi)  
- Auttaa hahmottamaan suuria käyttöliittymiä  
- Sopii dokumentaatioon ja debuggaamiseen

### 7. UI Tree Transformation Hooks
- Mahdollistaa UI‑puun muokkaamisen ennen healer‑vaihetta  
- Tuki automaattisille optimoinneille ja normalisoinneille  
- Luo pohjan tuleville “pre‑healing” ‑säännöille


