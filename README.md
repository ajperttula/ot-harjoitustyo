# TETRIS - Ohjelmistotekniikan harjoitustyö

Peli, jossa pelaajan tehtävänä on järjestellä pelikentän yläosasta tippuvia palikoita siten, että saadaan kokonainen rivi täyttymään. Täysi rivi tuhoutuu, jolloin lisää tilaa vapautuu pelikenttään. Pisteiden kasvaessa myös pelin tempo kasvaa.

Lataa uusin release [tästä](https://github.com/ajperttula/ot-harjoitustyo/archive/refs/tags/viikko5.zip)

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Pelin arkkitehtuuri](https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus

Asenna riippuvuudet komennolla
```bash
poetry install
```
Alusta tietokantayhteys komennolla
```bash
poetry run invoke build
```
Käynnistä peli komennolla
```bash
poetry run invoke start
```

## Komentorivitoiminnot

#### Pelin käynnistys
```bash
poetry run invoke start
```
#### Pylint testaus
```bash
poetry run invoke lint
```
#### Testien suoritus
```bash
poetry run invoke test
```
#### Testikattavuusraportin luominen
```bash
poetry run invoke coverage-report
```
Raportti on luettavissa tiedostosta *htmlcov/index.html*
