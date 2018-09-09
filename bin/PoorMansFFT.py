from keras.engine import Layer


class Dense(Layer):
    def __init__(self, initial_frequencies):
        # TODO Initialize super

        # TODO Initialize init variables

        pass

    def build(self, input_shape):
        # TODO Shape checking

        # TODO Create kernel(s)

        # TODO Create InputSpec
        pass

    def call(self, inputs, **kwargs):
        # TODO Transform inputs to scaled inputs

        # TODO Transform by applying sine cosine basis to scaled inputs

        pass

    def compute_output_shape(self, input_shape):
        # TODO shape checking
        pass

    def get_config(self):
        # TODO Generate config with all init variables
        # TODO Pull super's config
        # TODO Update layer config w/ super's config
        pass

    def _shape_checking(self, input_shape):
        pass
