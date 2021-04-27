# Pelin arkkitehtuurikuvaukset

## Luokkakaaviot

<img src="https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Luokkakaavio.png">

## Sekvenssikuvaukset

Sovelluslogiikan rungon muodostaa luokka GameLoop. Kuvataan tässä new_game() metodin suorittamat alustustoimenpiteet ennen varsinaisen pelisilmukan aloittamista:

<img src="https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sekvenssikaavio_gameloopin_kaynnistys.png">

Metodi new_game() kutsuu olion sisäistä metodia __reset_game(), joka asettaa totuusarvomuuttujan game_over Falseksi ja kutsuu sen jälkeen Level luokan metodia reset_game_state(). Tämä metodi asettaa Level luokassa oleven game_over totuusarvomuuttujan Falseksi ja kutsuu Block luokan metodia reset_block_position(), joka alustaa palikan paikan peliruudukon koordinaatteihin (0, 4) sekä määrittelee palikan muodon ja värin. Tämän jälkeen kutsutaan Grid luokan metodia reset_grid(), joka alustaa 2-ulotteisena taulukkona esitetyn peliruudukon nollilla. Sitten kutsutaan Score luokan metodia reset_score(), joka alustaa luokan muuttujat score ja counter nolliksi. Nyt metodi reset_game_state() on valmis ja seuraavaksi __reset_game() kutsuu Pace luokan metodia reset_pace(), joka alustaa muuttujat counter ja integer nolliksi, difficultyn arvoon yksi sekä totuusarvomuuttujan go_faset Falseksi. Nyt alustustoimet on tehty ja on aika kutsua varsinaista pelisilmukkametodia start().

Käydään läpi pelisilmukan ensimmäinen vaihe, joka tarkistaa tahdistinluokalta Pace, onko palikan aika tippua alaspäin.

<img src="https://github.com/ajperttula/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sekvenssikaavio_palikan_liikkeen_ajastus.png">

Metodi start pyörii ikuisessa silmukassa, kunnes game over tilanne pysäyttää sen. Silmukka kutsuu ensimmäiseksi luokan sisäistä metodia __check_counter(), joka puolestaan kutsuu Pace luokan metodia check_counter(). Pace luokassa kutsutaan ensin luokan sisäistä metodia __increase_counter(), joka lisää laskurin arvoon vaikeustason arvon tai, pelaajan pitäessä alaspäin nappia painettuna, vaikeustason arvon nelinkertaisena. Seuraavaksi check_counter() laskee, onko muuttujan counter arvo niin iso, että sen arvo jaettuna 60:llä ylittää muuttujan integer arvon. Jos on, niin muuttujan integer arvoa lisätään yhdellä ja palautetaan True, muussa tapauksessa False. Tässä siis tahdistetaan palikan liike niin, että aluksi palikka putoaa yhden ruudun sekunnissa ja vaikeustason kasvaessa nopeammin. Jos check_counter() palautti True, palikan on aika siirtyä alaspäin ja kutsutaan Level luokan metodia lower_block().
