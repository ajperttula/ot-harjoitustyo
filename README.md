# TETRIS - Ohjelmistotekniikan harjoitustyö

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

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
#### Testien suoritus
```bash
poetry run invoke test
```
#### Testikattavuusraportin luominen
```bash
poetry run invoke coverage-report
```
Raportti on luettavissa tiedostosta *htmlcov/index.html*
