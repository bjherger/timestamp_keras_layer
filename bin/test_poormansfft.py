import unittest

import pandas
from keras import Input, Model, losses
from keras.datasets import boston_housing
from keras.layers import Dense

from bin.PoorMansFFT import PoorMansFFT


class TestPoorMansFFT(unittest.TestCase):

    def test_convert_frequencies(self):
        self.assertEqual([60], PoorMansFFT._convert_frequencies(['minutely']))

        self.assertEqual([60, 31535965], PoorMansFFT._convert_frequencies(['minutely', 'yearly']))

        self.assertRaises(AssertionError, PoorMansFFT._convert_frequencies, ['shapely'])

    def test_init(self):
        initial_frequencies = ['minutely', 'yearly']
        layer = PoorMansFFT(initial_frequencies)

        # Test that super has been initialized
        self.assertTrue(hasattr(layer, 'built'))

        # Test for init variables
        self.assertCountEqual(initial_frequencies, layer.initial_frequencies)
        self.assertCountEqual([60, 31535965], layer.initial_frequencies_seconds)

    def test_integration(self):
        # Generate dataset
        obs = pandas.DataFrame(data={'date': ['2018-09-09', '2018-09-12', '2018-10-09'],
                                     'value': [0, 2, 30]})

        obs['date'] = pandas.to_datetime(obs['date'], format='%Y-%m-%d')
        obs['date_epoch'] = (obs['date'] - pandas.Timestamp("1970-01-01")) / pandas.Timedelta('1s')

        # Generate X,y
        X = obs['date_epoch'].values
        y = obs['value']

        # Create model

        inputs = Input(shape=(1,))
        x = inputs
        x = PoorMansFFT(initial_frequencies=['daily', 'monthly'])(inputs)
        x = Dense(32)(x)
        x = Dense(1)(x)

        model = Model(inputs=inputs, outputs=x)
        model.compile(optimizer='Adam', loss=losses.mean_squared_error)

        # Train model
        model.fit(X, y)
        pass
