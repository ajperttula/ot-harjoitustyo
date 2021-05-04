# Vaatimusmäärittely

## Pelin idea

Peli on klassinen Tetris, jossa palikoita tippuu pelialueen yläosasta alaspäin. Pelaajan tarkoituksena on siirrellä palikoita niin, että saadaan kokonainen rivi täyttymään, jolloin kyseinen rivi häviää ja lisää tilaa vapautuu pelialueelle. Ideana on saada mahdollisimman korkeat pisteet pelin nopeuden ja vaikeuden kasvaessa. Peli päättyy, kun uusi palikka ei mahdu putoamaan pelialueelle.

## Käyttöliittymäluonnos

Käynnistettäessa peli avautuu päävalikkoon. Muita valikoita ovat itse pelinäkymä, tulosnäkymä sekä asetusnäkymä.

<img src="https://raw.githubusercontent.com/ajperttula/ot-harjoitustyo/master/dokumentaatio/kuvat/kayttoliittyma.jpeg" width="750">

## Toiminnot

### Päävalikossa
- [x] Pelaaja voi siirtyä pelinäkymään
- [x] Pelaaja voi siirtyä tulosnäkymään
- [ ] Pelaaja voi siirtyä asetusvalikkoon
- [x] Pelaaja voi sulkea ohjelman

### Nimenantonäkymässä
- [x] Pejaala voi antaa nimensä

### Pelinäkymässä
- [x] Pelaaja voi aloittaa koska tahansa uuden pelin painamalla ENTER
- [x] Pelaaja voi siirtyä takaisin päävalikkoon
- [x] Peli loppuu, kun uudella palikalla ei ole enää tilaa pudota alaspäin
  #### Pelin ollessa käynnissä
  - [x] Pelaaja voi kääntää putoavaa palikkaa
  - [x] Pelaaja voi siirtää putoavaa palikkaa pelikentän laidalta toiselle
  - [x] Pelaaja voi nopeuttaa palikan putoamista
  - [x] Pelaaja voi pudottaa palikan alas
  - [x] Peli näyttää seuraavana vuorossa olevan palikan
  - [x] Rivin tullessa täyteen rivi katoaa
  - [x] Rivin tullessa täyteen pisteet lisääntyy
  - [x] Kun rivejä on tuhoutunut 15 kertaa, pelin tempo kasvaa (monta riviä kerralla lasketaan yhdeksi tuhoutumiseksi)
  #### Pelin loputtua
  - [x] Jos pelaaja sai pisteitä, nimi ja pisteet tallennetaan tietokantaan 

### Tulosnäkymässä
- [x] Pelaaja voi tarkastella huipputuloksia
- [x] Pelaaja voi palata takaisin päävalikkoon

### Asetusnäkymässä
- [ ] Pelaaja voi vaihtaa palikoiden väriteemaa
- [ ] Pelaaja voi palata päävalikkoon

## Kehitysideoita
* Peliin lisätään taustamusiikki ja efektiäänet
* Äänet päälle/pois asetusvalikosta
* Pelaaja voi muuttaa näppäinvalintoja asetusvalikossa
