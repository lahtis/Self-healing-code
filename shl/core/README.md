# Core Roadmap — Future Extensions

Tämä osio kokoaa yhteen core‑kerroksen mahdolliset tulevat laajennukset.  
Lista toimii muistilistana ja suunnittelun tukena, jos core‑kerrosta halutaan vahvistaa tai laajentaa tulevaisuudessa.

## 1. SHLComponent v2
- Selkeämpi komponenttimalli  
- Tuki laajennetuille attribuuteille (metadata, constraints, tags)  
- Parempi integraatio healer‑ ja middleman‑kerrosten kanssa  
- Mahdollisuus komponenttikohtaisiin validointisääntöihin

## 2. UI‑solmujen laajennettu rakenne
- Yhtenäinen solmutyyppi kaikille UI‑elementeille  
- Tuki lisäattribuuteille (layout, behavior, accessibility)  
- Parempi tuki dynaamisille solmuille ja tilamuutoksille

## 3. Core schema validator
- Skeemavalidointi core‑tason rakenteille  
- Estää virheelliset komponentit ennen middleman‑ ja healer‑kerroksiin siirtymistä  
- Toimii vastaparina registry‑kerroksen UCR‑validoinnille

## 4. Core serialization layer
- Yhtenäinen tapa serialisoida ja deserialisoida SHLComponent‑ ja UI‑solmuobjekteja  
- Tuki useille formaateille (JSON, YAML)  
- Mahdollistaa helpon tallennuksen ja siirrettävyyden

## 5. Core diff hooks
- Diff‑kerroksen suora integraatio core‑objekteihin  
- Mahdollistaa komponenttien ja UI‑solmujen muutosten seuraamisen  
- Tuki automaattisille diff‑raporteille

## 6. Core event system
- Tuki sisäisille tapahtumille (component_changed, ui_node_updated)  
- Mahdollistaa reaktiiviset healing‑ ja middleman‑prosessit  
- Perusta tuleville dynaamisille ominaisuuksille

## 7. Core metadata layer
- Komponenttien ja UI‑solmujen metadata  
- Versiohistoria, lähdetiedot ja muutoksen alkuperä  
- Mahdollistaa jäljitettävyyden ja selitettävyyden

## 8. Core test utilities
- Yhtenäiset apufunktiot core‑tason testaukseen  
- Snapshot‑testit UI‑solmuille  
- Komponenttien rakenteelliset validointitestit
