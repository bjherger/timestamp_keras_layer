from keras.engine import Layer


class PoorMansFFT(Layer):
    def __init__(self, initial_frequencies, **kwargs):
        # Initialize super
        super(PoorMansFFT, self).__init__(**kwargs)

        # Initialize init variables
        self.initial_frequencies = initial_frequencies

        # Convert initial frequencies to duration in seconds
        self.initial_frequencies_seconds = self._convert_frequencies(initial_frequencies)

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

    @staticmethod
    def _convert_frequencies(initial_frequencies):

        conversions = {
            'minutely': 60,
            'hourly': 3600,
            'daily': 86400,
            'weekly': 604800,
            'monthly': 2628288,
            'quarterly': 7883991,
            'yearly': 31535965
        }

        # Check for unknown initial frequencies
        for initial_frequency in initial_frequencies:
            if initial_frequency not in conversions:
                raise AssertionError('Unknown initial frequency: {}. Please choose from: {}'.format(initial_frequency,
                                                                                                    conversions.keys()))

        # TODO Convert initial frequencies to duration in seconds
        initial_frequencies_seconds = list(map(lambda x: conversions[x], initial_frequencies))
        return initial_frequencies_seconds
