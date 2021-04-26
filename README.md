# TETRIS - Ohjelmistotekniikan harjoitustyö

Peli, jossa pelaajan tehtävänä on järjestellä pelikentän yläosasta tippuvia palikoita siten, että saadaan kokonainen rivi täyttymään. Täysi rivi tuhoutuu, jolloin lisää tilaa vapautuu pelikenttään. Pisteiden kasvaessa myös pelin tempo kasvaa. Yritä päästä top-10 listaan!

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Pelin arkkitehtuuri](https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus

Asenna riippuvuudet komennolla
```bash
poetry install
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
