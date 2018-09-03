from keras.engine import Layer, InputSpec

from keras import backend as K, initializers


class Dense(Layer):

    def __init__(self, units, use_bias=True, kernel_initializer='glorot_uniform', **kwargs):
        super(Dense, self).__init__(**kwargs)
        self.units = units
        self.use_bias = use_bias
        self.kernel_initializer = initializers.get(kernel_initializer)

    def build(self, input_shape):
        assert len(input_shape) >= 2
        input_dim = input_shape[-1]

        self.kernel = self.add_weight(name='kernel',
                                      shape=(input_dim, self.units),
                                      initializer=self.kernel_initializer)

        if self.use_bias:
            self.bias = self.add_weight(name='bias',
                                        shape=(self.units,),
                                        initializer='zeros')
        else:
            self.bias = None

        self.input_spec = InputSpec(min_ndim=2, axes={-1: input_dim})

    def call(self, inputs, **kwargs):

        output = K.dot(inputs, self.kernel)

        if self.use_bias:
            output = K.bias_add(output, self.bias)

        return output

    def compute_output_shape(self, input_shape):
        assert len(input_shape) >= 2
        assert input_shape[-1]

        output_shape = list(input_shape)
        output_shape[-1] = self.units

        return tuple(output_shape)

    def get_config(self):
        config = {
            'units': self.units,
            'use_bias': self.use_bias,
            'kernel_initializer': initializers.serialize(self.kernel_initializer)
        }

        base_config = super(Dense, self).get_config()
        config.update(base_config)
        return config
