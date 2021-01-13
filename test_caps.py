import unittest
import caps


class TestCalc(unittest.TestCase):

    def test_caps(self):
        self.assertEqual(caps.to_caps("hello"), "HELLO", "Should return HELLO")
