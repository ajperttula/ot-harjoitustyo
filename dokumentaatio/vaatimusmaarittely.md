# Vaatimusmäärittely

## Pelin idea

Peli on klassinen Tetris, jossa palikoita tippuu pelialueen yläosasta alaspäin. Pelaajan tarkoituksena on siirrellä palikoita niin, että saadaan kokonainen rivi täyttymään, jolloin kyseinen rivi häviää ja lisää tilaa vapautuu pelialueelle. Ideana on saada mahdollisimman korkeat pisteet pelin nopeuden ja vaikeuden kasvaessa. Peli päättyy, kun alue täyttyy siten, että jokin palikka koskettaa pelikentän yläosaa.

## Käyttöliittymäluonnos

Käynnistettäessa peli avautuu päävalikkoon. Muita valikoita ovat itse pelinäkymä, tulosnäkymä sekä asetusnäkymä.

<img src="https://raw.githubusercontent.com/ajperttula/ot-harjoitustyo/master/dokumentaatio/kuvat/kayttoliittyma.jpeg" width="750">

## Toiminnot

### Päävalikossa
* Pelaaja voi siirtyä pelinäkymään
* Pelaaja voi siirtyä tulosnäkymään
* Pelaaja voi siirtyä asetusvalikkoon
* Pelaaja voi sulkea ohjelman

### Pelinäkymässä
* Pelaaja voi aloittaa uuden pelin
  #### Pelin ollessa käynnissä
  * Pelaaja voi kääntää putoavaa palikkaa
  * Pelaaja voi siirtää putoavaa palikkaa pelikentän laidalta toiselle
  * Pelaaja voi pudottaa palikan nopeasti
  * Peli näyttää seuraavana vuorossa olevan palikan
* Pelaaja voi siirtyä takaisin päävalikkoon

### Tulosnäkymässä
* Pelaaja voi tarkastella huipputuloksia
* Pelaaja voi palata takaisin päävalikkoon

### Asetusnäkymässä
* Pelaaja voi vaihtaa palikoiden väriteemaa
* Pelaaja voi palata päävalikkoon

## Kehitysideoita
* Peliin lisätään taustamusiikki ja efektiäänet
* Äänet päälle/pois asetusvalikosta
* Pelaaja voi muuttaa näppäinvalintoja asetusvalikossa
