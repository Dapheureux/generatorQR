import unittest
from main import determine_encoding_mode

class TestDetermineEncodingMode(unittest.TestCase):
   def test_determine_encoding_mode_numeric(self):
        data = "12345"
        mode = determine_encoding_mode(data)
        self.assertEqual(mode, 'numeric')

def test_determine_encoding_mode_alphanumeric(self):
    data = "ABC123"
    mode = determine_encoding_mode(data)
    self.assertEqual(mode, 'alphanumeric')

def test_determine_encoding_mode_byte(self):
    data = "Hello World"
    mode = determine_encoding_mode(data)
    self.assertEqual(mode, 'byte')

def test_determine_encoding_mode_kanji(self):
    data = "漢字"
    mode = determine_encoding_mode(data)
    self.assertEqual(mode, 'kanji')


if __name__ == "__main__":
    unittest.main()
