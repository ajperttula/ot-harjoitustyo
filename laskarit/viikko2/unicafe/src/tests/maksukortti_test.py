import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kortille_toimii(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.maksukortti.lataa_rahaa(-10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_nosto_onnistuu_jos_saldo_riittaa(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")

    def test_onnistunut_rahan_nosto_palauttaa_true(self):
        nosto = self.maksukortti.ota_rahaa(5)
        self.assertEqual(nosto, True)

    def test_rahan_nosto_ei_onnistu_jos_saldo_ei_riita(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_epaonnistunut_rahan_nosto_palauttaa_false(self):
        nosto = self.maksukortti.ota_rahaa(20)
        self.assertEqual(nosto, False)

    def test_kortilta_ei_voi_nostaa_negatiivista_summaa(self):
        self.maksukortti.ota_rahaa(-10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")