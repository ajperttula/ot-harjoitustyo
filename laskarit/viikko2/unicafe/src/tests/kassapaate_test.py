import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassa, None)

    def test_alkukassa_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_alussa_nolla_myytya_edullista_lounasta(self):
        self.assertEqual(self.kassa.edulliset, 0)

    def test_alussa_nolla_myytya_maukasta_lounasta(self):
        self.assertEqual(self.kassa.maukkaat, 0)

    # syö edullisesti käteisellä testit

    def test_edullisen_lounaan_osto_kateisella_lisaa_myytyjen_edullisten_lounaiden_maaraa(self):
        self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_edullisen_lounaan_osto_tasarahalla_lisaa_myytyjen_edullisten_lounaiden_maaraa(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_edullisen_lounaan_osto_tasarahalla_lisaa_kassaan_edullisen_lounaan_hinnan(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_edullisen_lounaan_osto_kateisella_lisaa_kassaan_edullisen_lounaan_hinnan(self):
        self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_edullisen_lounaan_osto_tasarahalla_ei_anna_vaihtorahaa(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(vaihtoraha, 0)

    def test_edullisen_lounaan_osto_kateisella_palauttaa_oikean_vaihtorahan(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)

    def test_myytyjen_edullisten_lounaiden_maara_ei_muutu_jos_maksu_ei_riita(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_edullisen_lounaan_ostoyritys_liian_pienella_summalla_ei_muuta_kassan_saldoa(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_edullisen_lounaan_ostoyritys_liian_pienella_summalla_palauttaa_koko_maksun(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)

    # syö maukkaasti käteisellä testit

    def test_maukkaan_lounaan_osto_kateisella_lisaa_myytyjen_maukkaiden_lounaiden_maaraa(self):
        self.kassa.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_maukkaan_lounaan_osto_tasarahalla_lisaa_myytyjen_maukkaiden_lounaiden_maaraa(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_maukkaan_lounaan_osto_tasarahalla_lisaa_kassaan_maukkaan_lounaan_hinnan(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_maukkaan_lounaan_osto_kateisella_lisaa_kassaan_maukkaan_lounaan_hinnan(self):
        self.kassa.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_maukkaan_lounaan_osto_tasarahalla_ei_anna_vaihtorahaa(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(vaihtoraha, 0)

    def test_maukkaan_lounaan_osto_kateisella_palauttaa_oikean_vaihtorahan(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(450)
        self.assertEqual(vaihtoraha, 50)

    def test_myytyjen_maukkaiden_lounaiden_maara_ei_muutu_jos_maksu_ei_riita(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_maukkaan_lounaan_ostoyritys_liian_pienella_summalla_ei_muuta_kassan_saldoa(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_maukkaan_lounaan_ostoyritys_liian_pienella_summalla_palauttaa_koko_maksun(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)

    # syö edullisesti kortilla testit

    def test_onnistunut_edullisen_lounaan_osto_kortilla_lisaa_myytyjen_edullisten_lounaiden_lukumaaraa(self):
        kortti = Maksukortti(300)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_onnistunut_edullisen_lounaan_osto_kortilla_palauttaa_true(self):
        kortti = Maksukortti(300)
        arvo = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(arvo, True)

    def test_epaonnistunut_edullisen_lounaan_osto_kortilla_ei_lisaa_myytyjen_edullisten_lounaiden_lukumaaraa(self):
        kortti = Maksukortti(200)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_epaonnistunut_edullisen_lounaan_osto_kortilla_palauttaa_false(self):
        kortti = Maksukortti(200)
        arvo = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(arvo, False)

    def test_onnistunut_edullisen_lounaan_osto_kortilla_ei_muuta_kassan_saldoa(self):
        kortti = Maksukortti(300)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_epaonnistunut_edullisen_lounaan_osto_kortilla_ei_muuta_kassan_saldoa(self):
        kortti = Maksukortti(200)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    # syö maukkaasti kortilla testit

    def test_onnistunut_maukkaan_lounaan_osto_kortilla_lisaa_myytyjen_maukkaiden_lounaiden_lukumaaraa(self):
        kortti = Maksukortti(500)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_onnistunut_maukkaan_lounaan_osto_kortilla_palauttaa_true(self):
        kortti = Maksukortti(500)
        arvo = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(arvo, True)

    def test_epaonnistunut_maukkaan_lounaan_osto_kortilla_ei_lisaa_myytyjen_maukkaiden_lounaiden_lukumaaraa(self):
        kortti = Maksukortti(200)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_epaonnistunut_maukkaan_lounaan_osto_kortilla_palauttaa_false(self):
        kortti = Maksukortti(200)
        arvo = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(arvo, False)

    def test_onnistunut_maukkaan_lounaan_osto_kortilla_ei_muuta_kassan_saldoa(self):
        kortti = Maksukortti(500)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_epaonnistunut_maukkaan_lounaan_osto_kortilla_ei_muuta_kassan_saldoa(self):
        kortti = Maksukortti(200)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    # rahan lataus kortille testit

    def test_rahan_lataus_kortille_lisaa_kassan_arvoa_vastaavasti(self):
        kortti = Maksukortti(200)
        self.kassa.lataa_rahaa_kortille(kortti, 200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100200)

    def test_rahan_lataus_kortille_ei_lisaa_kassan_arvoa_jos_summa_nolla(self):
        kortti = Maksukortti(200)
        self.kassa.lataa_rahaa_kortille(kortti, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_rahan_lataus_kortille_ei_lisaa_kassan_arvoa_jos_summa_negatiivinen(self):
        kortti = Maksukortti(200)
        self.kassa.lataa_rahaa_kortille(kortti, -100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)