# Pelin arkkitehtuurikuvaukset

## Pelin rakenne


<img src="https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/pakkauskaavio.png">

Kokonaisuus koostuu kolmesta kerroksesta: käyttöliittymä, sovelluslogiikka sekä tiedon pysyväistallennus.

### Käyttöliittymä
Käyttöliittymä on jaoteltu omiin luokkiin näkymien perusteella. Jokainen näkymä käyttää lisäksi UIRenderer luokkaa näytön piirtämiseen. Tulosnäkymä hyödyntää lisäksi ScoreRepository luokkaa tulosten hakemiseen tietokannasta. Käyttöliittymä koostuu seuraavista näkymistä:

- Päävalikko
- Tulosvalikko
- Nimenantovalikko

### Sovelluslogiikka
Sovelluslogiikan rungon muodostaa luokka GameLoop. Hakemisto game_loop sisältää kaikki GameLoopin tarvitsemat luokat. Lisäksi GameLoop hyödyntää GameRenderer luokkaa pelinäkymän piirtämiseen.

### Pysyväistallennus
Pelin tulosten tallentamisesta huolehtii luokka ScoreRepository, joka tallentaa pelaajan nimen ja pelin tuloksen SQLite tietokantaan. Oletuksena tiedostonimi on scores.db, mutta sitä voi muuttaa juurihakemistosta löytyvän .env tiedoston kohdasta DATABASE_FILENAME.

## Luokkakaaviot

<img src="https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Luokkakaavio.png">

## Sekvenssikuvaukset

Sovelluslogiikan rungon muodostaa luokka GameLoop. Kuvataan tässä new_game() metodin suorittamat alustustoimenpiteet ennen varsinaisen pelisilmukan aloittamista:

<img src="https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sekvenssikaavio_gameloopin_kaynnistys.png">

Metodi new_game(player) saa argumenttina pelaajan syöttämän nimen, joka laitetaan talteen. Sen jälkeen se kutsuu olion sisäistä metodia __reset_game(), joka asettaa silmukan tilaa kuvaavan muuttujan running arvoon True, pelin tilannetta kuvaavan totuusarvomuttujan game_over arvoon False ja kutsuu sitten Level luokan metodia reset_game_state(). Tämä metodi kutsuu Block luokan metodia reset_block_position(), joka alustaa palikan paikan peliruudukon koordinaatteihin (0, 4) sekä asettaa palikan muodoksi ja väriksi seuraavana vuorossa olleen palikan arvot sekä arpoo uuden muodon ja värin seuraavalle palikalle. Tämän jälkeen kutsutaan Grid luokan metodia reset_grid(), joka alustaa 2-ulotteisena taulukkona esitetyn peliruudukon nollilla. Sitten kutsutaan Score luokan metodia reset_score(), joka alustaa luokan muuttujat score ja counter nolliksi. Lopuksi kutsutaan Pace luokan metodia reset_pace(), joka alustaa muuttujat counter ja integer nolliksi, difficultyn arvoon yksi sekä totuusarvomuuttujan go_fast Falseksi. Nyt alustustoimet on tehty ja on aika kutsua varsinaista pelisilmukkametodia __start().

Metodi start pyörii silmukassa, kunnes game over tilanne aiheuttaa siirtymisen finished metodin silmukkaan. Silmukan kutsujärjestys on seuraava:

1. tarkista onko peli ohi __check_game_over()
2. tarkista onko palikan aika liikkua alaspäin __check_counter()
3. tarkista onko rivejä tuhottu niin monta, että on aika nopeuttaa peliä __check_score()
4. tarkista käyttäjän syötteet __check_events()
5. piirrä kuva näytölle __render_game()
6. kutsu clock oliota, joka ajastaa silmukan pyörimään 60 kertaa sekunnissa __clock.tick(60)

__Alla kuvattuna tilanne, jossa peli todetaan päättyneeksi.__

<img src="https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sekvenssikaavio_peli_ohi_tarkistus.png">

Jos palikan todetaan törmänneen jo ennen kuin se on liikkunut alaspäin, asetetaan totuusarvomuuttuja game_over arvoon True ja kutsutaan sisäistä metodia __save_score(), joka puolestaan kutsuu ScoreRepository luokan metodia save_score(), mikäli pisteitä on kertynyt pelin aikana. Tämä metodi tallentaa pelaajan nimen ja pisteet tietokantaan. Lopuksi kutsutaan sisäistä metodia __finished(), joka on vastaava silmukka kuin __start(), mutta pelkällä syötteiden tarkistuksella ja kuvan piirtämisellä.

__Käydään läpi pelisilmukan toinen vaihe, joka tarkistaa tahdistinluokalta Pace, onko palikan aika tippua alaspäin.__

<img src="https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sekvenssikaavio_palikan_liikkeen_ajastus.png">

Silmukka kutsuu ensimmäiseksi luokan sisäistä metodia __check_counter(), joka puolestaan kutsuu Pace luokan metodia check_counter(). Pace luokassa kutsutaan ensin luokan sisäistä metodia __increase_counter(), joka lisää laskurin arvoon vaikeustason arvon tai, pelaajan pitäessä alaspäin nappia painettuna, vaikeustason arvon nelinkertaisena. Seuraavaksi check_counter() laskee, onko muuttujan counter arvo niin iso, että sen arvo jaettuna 60:llä ylittää muuttujan integer arvon. Jos on, niin muuttujan integer arvoa lisätään yhdellä ja palautetaan True, muussa tapauksessa False. Tässä siis tahdistetaan palikan liike niin, että aluksi palikka putoaa yhden ruudun sekunnissa ja vaikeustason kasvaessa nopeammin. Jos check_counter() palautti True, palikan on aika siirtyä alaspäin ja kutsutaan Level luokan metodia lower_block().

__Lower_block sisältää itsessään palikan törmäystarkistuksen, peliruudun päivityksen, täysien rivien tuhoamisen ja uuden palikan siirron alkukoordinaatteihin.__

<img src="https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sekvenssikaavio_palikan_liike_alas.png">

Palikkaa siirretään ensin yksi ruutu alaspäin ja sen jälkeen tarkistetaan aiheuttaako tämä sijainti törmäyksen toiseen palikkaan tai meneekö palikan sijainti ohi peliruudukon reunoista. Yksinkertaisessa tapauksessa palikka ei törmää, ja funktio palauttaa True.
Jos palikan siirto alaspäin aiheutti törmäyksen, siirretään palikka takaisin edelliseen sijaintiin. Sen jälkeen kutsutaan Grid luokan metodia, joka muuttaa ne koordinaatit ruudukossa, jossa palikka sijaitsee, palikan värikoodin arvoon. Sen jälkeen kutsutaan toista Grid luokan metodia check_for_full_rows(), joka tarkistaa, tuliko ruudukkoon täysiä rivejä. Jos täysiä rivejä havaitaan, ne poistetaan ja vastaava määrä tyhjiä rivejä lisätään ruudukon ylälaitaan. Lopuksi palautetaan poistettujen rivien määrä.
Lopuksi kutsutaan Block luokan metodia reset_position(), joka palauttaa palikan alkusijaintiin. Tämän jälkeen funktio palauttaa False.

__Alla kuvattu tilanne, miten vaikeusaste lisääntyy, kun rivejä on tuhottu 15 kertaa.__

<img src="https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sekvenssikaavio_pisteiden_tarkistus.png">

Silmukka kutsuu sisäistä metodia __check_score(), joka kutsuu Score luokan funktiota check_score(). Tämä funktio palauttaa True, jos counter muuttujan arvo on 15. Samalla counter arvo nollataan. Tämän jälkeen kutsutaan Pace luokan metodia increase_difficulty(), joka nostaa difficulty muuttujan arvoa yhdellä.

Käyttäjän syötteitä voivat olla palikan liikuttaminen vasemmalle tai oikealle, palikan kierto, palikan putoamisen nopeuttaminen tai palikan pudotus. Liikuttaminen vasemmalle ja oikealle hyödyntää samaa level luokan funktiota block_collides() törmäysten tarkistukseen. Palikan putoaminen on toteutettu siten, että lower_block() funktiota suoritetaan silmukassa, kunnes se palauttaa False.
