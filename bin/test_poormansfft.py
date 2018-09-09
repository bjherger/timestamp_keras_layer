import unittest

from bin.PoorMansFFT import PoorMansFFT


class TestPoorMansFFT(unittest.TestCase):

    def test_convert_frequencies(self):
        self.assertEqual([60], PoorMansFFT._convert_frequencies(['minutely']))

        self.assertEqual([60, 31535965], PoorMansFFT._convert_frequencies(['minutely', 'yearly']))

        self.assertRaises(AssertionError,  PoorMansFFT._convert_frequencies, ['shapely'])

    def test_init(self):
        initial_frequencies = ['minutely', 'yearly']
        layer = PoorMansFFT(initial_frequencies)

        # Test that super has been initialized
        self.assertTrue(hasattr(layer, 'built'))

        # Test for init variables
        self.assertCountEqual(initial_frequencies, layer.initial_frequencies)
        self.assertCountEqual([60, 31535965], layer.initial_frequencies_seconds)
