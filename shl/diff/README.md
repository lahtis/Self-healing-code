# Diff Roadmap — Future Extensions

Tämä osio kokoaa yhteen diff‑kerroksen mahdolliset tulevat laajennukset.  
Lista toimii muistilistana ja suunnittelun tukena, jos diff‑kerrosta halutaan vahvistaa tai laajentaa tulevaisuudessa.

## 1. Blueprint diff ‑moduuli
- Vertaa kahta blueprint‑tiedostoa  
- Tunnistaa lisätyt, poistetut ja muuttuneet komponentit  
- Havaitsee muutokset text_keys‑ ja framework_map‑kentissä  
- Tuottaa rakenteellisen diff‑raportin

## 2. UCR diff ‑moduuli
- Vertaa kahta UCR‑tiedostoa  
- Tunnistaa healer‑mapin erot  
- Havaitsee data_binding‑muutokset  
- Sopii registry‑kerroksen debuggaamiseen

## 3. UI‑puu diff ‑moduuli
- Vertaa kahta UI‑puuta  
- Tunnistaa solmujen lisäykset, poistot ja attribuuttimuutokset  
- Havaitsee rakenteelliset erot  
- Auttaa middleman‑ ja healer‑kerrosten analysoinnissa

## 4. Healer diff ‑moduuli
- Vertaa healerin input‑ ja output‑rakenteita  
- Näyttää, mitä healer muutti ja miksi  
- Sopii explainability‑kerroksen perustaksi

## 5. Patcher diff ‑moduuli
- Vertaa patcher‑inputia ja patcher‑outputia  
- Tunnistaa muutokset blueprintissä tai UCR:ssä  
- Tuottaa selkeän raportin patcher‑toimista

## 6. Diff reporter
- Yhtenäinen raporttigeneraattori kaikille diff‑tyypeille  
- Tukee JSON‑, Markdown‑ ja tekstimuotoa  
- Mahdollistaa diff‑tulosten tallentamisen ja versionhallinnan

## 7. Diff visualizer (kokeellinen)
- Graafinen tai puumainen esitys diffeistä  
- Korostaa muutokset värikoodeilla  
- Auttaa hahmottamaan suuria UI‑ tai blueprint‑muutoksia
