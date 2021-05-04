# Käyttöohje

Lataa tästä pelin viimeisin release.

## Pelin asennus

Asenna pelin riippuvuudet komennolla
```bash
poetry install
```
Alusta sen jälkeen tietokantayhteys komennolla
```bash
poetry run invoke build
```

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
Täällä näet Top 10 tulokset. Jos kahdella pelaajalla on sama tulos, heilä jaettu sijoitus rankingissa. Pääset takaisin päävalikkoon painamalla __Main menu__.<br><br>
![](https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/tulosvalikko.png)

### Nimenanto
Kun aloitat uuden pelin, voit antaa nimesi. Jos et anna nimeä ja pääset tuloslistalle, siellä näytetään vain tulos ilman nimeä. Pääset jatkamaan peliin painamalla __ENTER__.<br><br>
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
