# Kielelliset säännöt (Grammatical Engine)

Tämä dokumentti kuvaa SHL-järjestelmän kielellistä älyä. Vaikka moottorin tekninen integraatio on osittain kesken (WIP), nämä säännöt muodostavat perustan sille, miten Healer pystyy tunnistamaan suomenkielisiä komponentteja dynaamisesti.

## 1. Miksi kielellinen äly on välttämätön?

Suomen kieli on morfologisesti rikas. Perinteiset käyttöliittymätestit etsivät tarkkaa merkkijonoa (esim. "Tallenna"). Jos käyttöliittymässä lukeekin "Tallennat" tai "Tallennetaan", perinteinen testi epäonnistuu. 

**SHL hyödyntää kielioppisääntöjä normalisoidakseen tekstin ennen vertailua.**



---

## 2. Keskeiset säännöt (The Big Three)

Healer-moottorin `Text Match` -algoritmi perustuu kolmeen pääsääntöön:

### A. Vokaalisointu (Vowel Harmony)
Suomen kielessä päätteet vaihtelevat sanan vokaalien mukaan (esim. *-ssa* vs. *-ssä*).
- **Logiikka:** Healer tunnistaa, että "Pankissa" ja "Metsässä" sisältävät saman lokatiivisen merkityksen.
- **Sovellus:** Kun Healer etsii avainta `store`, se osaa normalisoida päätteet pois ja verrata vain sanan vartaloa.

### B. Vokaaligradation (Asteitaistelu)
Sanan vartalo muuttuu taivutettaessa (esim. *pankki* -> *pankin*, *tyttö* -> *tytön*).
- **Logiikka:** Moottori sisältää säännöt yleisimmille K-P-T -vaihteluille.
- **Sovellus:** Jos `SHLComponent` määrittelee tekstiksi "Pankki", mutta ruudulla lukee "Pankin tiedot", Healer ymmärtää näiden olevan sama semanttinen kohde.

### C. Yhdyssanat ja yhdyssanahaku
Käyttöliittymissä sanat on usein yhdistetty (esim. `tallenna_painike` tai `saveButton`).
- **Logiikka:** Moottori pilkkoo sanat osiin ja etsii merkityksellisiä "middleman"-sanoja.
- **Sovellus:** Tunnistaa, että "Käyttäjänimi" ja "Käyttäjän nimi" viittaavat samaan `user_name` -komponenttiin.

---

## 3. Pisteytyslogiikka (Scoring Rules)

Healer ei tee "kyllä/ei" -päätöksiä, vaan se laskee **Linguistic Distance** -arvon:

1. **Exact Match (1.0):** Teksti on täsmälleen sama kuin kielitiedostossa.
2. **Stem Match (0.8):** Sanan vartalo täsmää, kun taivutuspäätteet on poistettu vokaalisoinnun sääntöjen mukaan.
3. **Fuzzy Grammatical Match (0.6):** Sana on tunnistettavissa astevaihtelun tai yhdysosien perusteella.



---

## 4. Työn alla (WIP): Integraatio HealerEngineen

Tällä hetkellä `LanguageManager` tarjoaa peruskäännökset. Seuraavassa vaiheessa (V2) `HealerEngine._find_by_text` laajennetaan kutsumaan `GrammarEngine`-luokkaa, joka suorittaa yllä mainitut normalisoinnit.

**Tavoite:** Healerin on pystyttävä sanomaan:
> *"Löysin tekstin 'Tallennat'. Se ei ole sama kuin 'Tallenna', mutta vokaalisoinnun ja vartalon perusteella se on 92 % varmuudella etsimäsi toiminto."*

---

## 5. Tutkimuksellinen arvo

Tämä on SHL-tutkimuksen uniikein osa. Se siirtää itseparannuksen painopisteen **rakenteellisesta tunnistamisesta kielelliseen ymmärtämiseen**. Tämä on erityisen kriittistä suomen kaltaisissa kielissä, joissa sanat muuttavat muotoaan kontekstin mukaan.
