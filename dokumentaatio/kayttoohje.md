# Käyttöohje

Lataa [tästä](https://github.com/ajperttula/ot-harjoitustyo/archive/refs/tags/final.zip) pelin viimeisin release.

## Pelin asennus

Asenna pelin riippuvuudet komennolla
```bash
poetry install
```

## Asetusten muuttaminen

Voit muokata pisteiden tallennukseen käytetyn tietokannan nimeä sekä pelin värejä muokkaamalla juurihakemiston .env tiedostoa. Väri tulee antaa heksadesimaaliformaatissa. https://www.rgbtohex.net/
```bash
DATABASE_FILENAME=scores.db
BG_COLOR=#BFDBF7
TEXT_COLOR=#022B3A
BUTTON_COLOR=#1F7A8C
GRID_BG_COLOR=#FCFCFC
GRID_COLOR=#E1E5F2
BLOCK_COLOR_1=#F94144
BLOCK_COLOR_2=#F3722C
BLOCK_COLOR_3=#90BE6D
BLOCK_COLOR_4=#277DA1
BLOCK_COLOR_5=#577590
BLOCK_COLOR_6=#F9C74F
```
__HUOM! Peli tallentaa tulokset aina sen nimiseen tietokantatiedostoon, minkä olet määritellyt .env tiedostossa. Jos muutat tiedoston nimeä, et näe enää listausta vanhoista huipputuloksista. Voit palata käyttämään vanhaa tietokantaa muuttamalla nimen takaisin alkuperäiseen.__

## Pelin käynnistys

Voit nyt käynnistää pelin komennolla
```bash
poetry run invoke start
```

## Valikot

Pääset valikosta toiseen hiirellä klikkaamalla.

### Päävalikko
Voit aloittaa uuden pelin painamalla __New game__, tarkastella huipputuloksia painamalla __High Scores__ tai sulkea peli painamalla __Exit__. <br><br>
![](https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/paavalikko.png)

### Tulosvalikko
Täällä näet Top 10 tulokset. Jos kahdella pelaajalla on sama tulos, heillä on jaettu sijoitus rankingissa. Pääset takaisin päävalikkoon painamalla __Main menu__.<br><br>
![](https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/tulosvalikko.png)

### Nimenanto
Kun aloitat uuden pelin, voit antaa nimesi. Jos et anna nimeä ja pääset tuloslistalle, tuloksesi näytetään ilman nimeä. Pääset jatkamaan peliin painamalla __ENTER__.<br><br>
![](https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/nimivalikko.png)

### Pelinäkymä
Pelinäkymässä näet peliruudukon, jonka ylälaidasta tippuu palikoita. Oikeassa yläkulmassa näet pisteesi sekä seuraavana vuoroon tulevan palikan. 
Yritä järjestellä tippuvia palikoita niin, että saat rivin täyteen, jolloin rivi tuhoutuu ja lisää tilaa vapautuu peliruudukkoon. Yhden rivin tuhoaminen tuottaa yhden pisteen. 
Kun rivejä on tuhoutunut 15 kertaa, peli vaikeutuu ja palikat tippuvat nopeammin. Kannattaa sis yrittää saada tuhottua monta riviä kerrallaan, jolloin pelin nopeutumiseen menee kauemmin. 
Voit palata takaisin päävalikkoon painamalla __Main menu__.
#### Näppäinkomennot
- __Vasen nuoli__ - Liikuta palikkaa vasemmalle
- __Oikea nuoli__ - Liikuta palikkaa oikealle
- __Ylös nuoli__ - Kierrä palikkaa myötäpäivään
- __Alas nuoli__ - Nopeuta palikan putoamista
- __Välilyönti__ - Pudota palikka
- __ENTER__ - Aloita uusi peli<br><br>
![](https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/pelinakyma.png)<br><br>
Peli päättyy, kun uudella palikalla ei ole enää tilaa pudota alaspäin. <br><br>
![](https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/peli_ohi.png)
