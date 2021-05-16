# Vaatimusmäärittely

## Pelin idea

Peli on klassinen Tetris, jossa palikoita tippuu pelialueen yläosasta alaspäin. Pelaajan tarkoituksena on siirrellä palikoita niin, että saadaan kokonainen rivi täyttymään, jolloin kyseinen rivi häviää ja lisää tilaa vapautuu pelialueelle. Ideana on saada mahdollisimman korkeat pisteet pelin nopeuden ja vaikeuden kasvaessa. Peli päättyy, kun uusi palikka ei mahdu putoamaan pelialueelle.

## Käyttöliittymä

Käynnistettäessa peli avautuu päävalikkoon. Muita valikoita ovat tulosvalikko, nimenantovalikko sekä itse pelinäkymä.

## Toiminnot

### Päävalikossa
- Pelaaja voi aloittaa uuden pelin
- Pelaaja voi siirtyä tulosnäkymään
- Pelaaja voi sulkea ohjelman

### Nimenantonäkymässä
- Pejaala voi antaa nimensä

### Pelinäkymässä
- Pelaaja voi aloittaa koska tahansa uuden pelin painamalla ENTER
- Pelaaja voi siirtyä takaisin päävalikkoon
  #### Pelin ollessa käynnissä
  - Pelaaja voi kääntää putoavaa palikkaa
  - Pelaaja voi siirtää putoavaa palikkaa pelikentän laidalta toiselle
  - Pelaaja voi nopeuttaa palikan putoamista
  - Pelaaja voi pudottaa palikan alas
  - Peli näyttää seuraavana vuorossa olevan palikan
  - Rivin tullessa täyteen rivi katoaa
  - Rivin tullessa täyteen pisteet lisääntyy
  - Kun rivejä on tuhoutunut 15 kertaa, pelin tempo kasvaa (monta riviä kerralla lasketaan yhdeksi tuhoutumiseksi)
  - Peli loppuu, kun uudella palikalla ei ole enää tilaa pudota alaspäin
  #### Pelin loputtua
  - Jos pelaaja sai pisteitä, nimi ja pisteet tallennetaan tietokantaan
  - Pelaajalle näytetään game over teksti ja ohjeistus uuden pelin aloituksesta

### Tulosnäkymässä
- Pelaaja voi tarkastella huipputuloksia
- Pelaaja voi palata takaisin päävalikkoon

## Kehitysideoita
* Peliin lisätään taustamusiikki ja efektiäänet
* Äänet päälle/pois nappi
* Tällä hetkellä pelaaja voi konfiguroida pelin värejä. Ympäristömuuttujia voisi lisätä niin, että myös ruudun ja elementtien koot olisivat muokattavissa.
* Pelaaja voi muuttaa näppäinasetuksia
