import inspect
import unittest

from bin import Dense


class TestDense(unittest.TestCase):

    def test_init(self):
        layer = Dense.Dense(10)

        self.assertEqual(10, layer.units)

    def test_build_shape(self):
        layer = Dense.Dense(10)
        self.assertRaises(AssertionError, layer.build, input_shape=[10])

    def test_build_bias(self):
        layer = Dense.Dense(10, use_bias=True)
        layer.build(input_shape=(None, 100))
        self.assertIsNotNone(layer.bias)

    def test_build_no_bias(self):
        layer = Dense.Dense(10, use_bias=False)
        layer.build(input_shape=(None, 100))
        self.assertIsNone(layer.bias)

    def test_compute_output_shape(self):
        layer = Dense.Dense(10, use_bias=True)
        output_shape = layer.compute_output_shape((None, 100))

        self.assertEqual((None, 10), output_shape)

    def test_get_config(self):
        layer = Dense.Dense(10, use_bias=True)
        sig = inspect.signature(Dense.Dense.__init__)
        expected_args = set([p.name for p in sig.parameters.values()])

        unserialized_args = ['self', 'kwargs']
        for unserialized_arg in unserialized_args:
            expected_args.remove(unserialized_arg)

        expected_args.update(['name', 'trainable'])

        self.assertCountEqual(expected_args, layer.get_config().keys())
