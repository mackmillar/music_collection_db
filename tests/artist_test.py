import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):
    
    def setUp(self):
        self.artist = Artist("Kurt Cobain")

    def test_artist_has_name(self):
        self.assertEqual("Kurt Cobain", self.artist.name)