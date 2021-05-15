# Testausdokumentaatio

Pelin testaus on toteutettu yksikkötestien avulla sekä toteamalla pelin toimivuus Windows 10 ja Linux Cubbli versiolla.

### Sovelluslogiikan testit

Suurin osa yksikkötesteistä on toteutettu testaamalla suoraan Level luokan komponenttien metodeja.
GameLoop luokan testit testaavat käyttäjän syötteitä.

GameLoopia testaava testiluokkaan TestGameLoop injektoidaan valeluokkina StubClock, StubEvent, StubEventQueue, StubRenderer ja StubScoreRepository.
Näistä ainoastaan StubEvent ja StubEventQueue ovat käytössä testeissä. Yksittäisistä käyttäjätapahtumista luodaan lista, esimerkiksi 
```
events = [StubEvent(pygame.KEYDOWN, pygame.K_LEFT)]
```
jonka luokka StubEventQueue saa parametrina.

### Pysyväistallennuksen testit

Pysyväistallennusta testataan luokalla TestScoreRepository. Tätä varten testit luovat pelkästään testien käytössä olevan tietokannan _test_scores.db_.
Tämä on konfiguroitu .env.test tiedostoon.

### Testauskattavuus

Testien ulkopuolelle on jätetty valikkojen luokat sekä näkymien piirtämisestä vastaavat Renderer luokat.

## Järjestelmätestaus

Testaus on toteutettu asentamalla peli käyttöohjeen ohjeiden mukaisesti, käymällä pelin toiminnallisuudet läpi vaativuusmäärittelyn mukaisesti
sekä muokkaamalla konfiguraatiotiedoston asetuksia.
