import numpy
import pandas

import matplotlib.pyplot as plt


def main():
    # Generate dataset
    obs = pandas.DataFrame(data={'date': pandas.date_range('1970-01-01 00:00:00', periods=366, freq='D')})

    obs['date'] = pandas.to_datetime(obs['date'], format='%Y-%m-%d')
    obs['date_epoch'] = (obs['date'] - pandas.Timestamp("1970-01-01")) / pandas.Timedelta('1s')

    # Generate X,y
    X = obs['date_epoch'].values

    print()
    print('X')
    print(X)

    # Initialize frequencies
    # day, Month, year
    day_len = 86400

    freq = [[day_len*30.4], [day_len*365.25/4],[day_len*365.25]]
    freq = (numpy.array(1) / freq) * 2 * numpy.pi

    # Multiply to create sine & cosine arguments

    arguments = numpy.transpose(X * freq)

    print()
    print('arguments')
    print(arguments)

    # Apply sine and cosine functions to arguments
    sin_values = numpy.sin(arguments)
    cos_values = numpy.cos(arguments)

    print()
    print('sine')
    print(sin_values)
    print()
    print('cosine')
    print(cos_values)

    obs['sin_monthly'] = sin_values[:, 0]
    obs['sin_quarterly'] = sin_values[:, 1]
    obs['sin_yearly'] = sin_values[:, 2]

    obs['cos_monthly'] = cos_values[:, 0]
    obs['cos_quarterly'] = cos_values[:, 1]
    obs['cos_yearly'] = cos_values[:, 2]

    variables = ['sin_monthly', 'sin_quarterly', 'sin_yearly']

    for variable in variables:
        plt.plot(obs['date'], obs[variable], label=variable)

    legend = plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
