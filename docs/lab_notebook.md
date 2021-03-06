# 2018-09-03

## Backlog

 - Review keras backend
   - Validate necessary functions are available
 - Create simple example layer
 - Validate simple example layer
 - Lit review for sine-cosine decomp
 - Outline timestamp layer
 - Create timestamp layer
 
## Keras backend

 - Reviewing [keras backend](https://keras.io/backend/)
 - Support for tensorflow (google), theano (university of montreal) and cntk (microsoft)
 
### [New code](https://keras.io/backend/#using-the-abstract-keras-backend-to-write-new-code)

 - Input placeholder example
 - Variable example
 - Initializing various matrices
 - Math operations, argmax, log
 - [Sine and cosine](https://keras.io/backend/#cos)
 - losses
 - Activation functions
 - Random variables
 
## Simple example layer

Will re-create [dense layer](https://github.com/keras-team/keras/blob/master/keras/layers/core.py#L762)

 - self.add_weight: Add learnable weights (e.g. TF variables)
   - Requires some initializer
 - InputSpec: Expected input shape. Can check minimum number of dimensions, as well as requirements along a specific axis 
 - We never explicitly update the kernel / bias. That seems to happen elsewhere

# 2018-08-20

## Keras layers
 - Reviewing documentation for custom keras layers: https://keras.io/layers/writing-your-own-keras-layers/
 - Outline
 - Build method: Set up weights
 - Call method: Actual work
 - Compute output shape method: give output shape
 - Most work done in call

## Examples
 - Antirectifier: https://github.com/keras-team/keras/blob/master/examples/antirectifier.py
 - Can also use Lambda function: https://keras.io/layers/core/#lambda
 - [spectrogram](https://github.com/sophiaray/kapre/blob/master/kapre/time_frequency.py), from Sophe
 
# 2018-09-09

## Lit review

 - [cycles](https://www.le.ac.uk/users/dsgp1/COURSES/TSERIES/2CYCLES.PDF)
 - [Stolwijk](https://jech.bmj.com/content/jech/53/4/235.full.pdf)
 - [Periodogram](https://onlinecourses.science.psu.edu/stat510/node/71/)
 - [tamu](https://www.stat.tamu.edu/~jnewton/stat626/topics/topics/topic4.pdf)
 
### [cycles](https://www.le.ac.uk/users/dsgp1/COURSES/TSERIES/2CYCLES.PDF)

 - Intro to trig functions
 - Fourier Decomposition of time series: Sum over multiple frequencies
   - Can estimate using OLS
   - Can use nyquist frequency to lower bound for frequencies 
 
### [Stolwijk](https://jech.bmj.com/content/jech/53/4/235.full.pdf)

 - Use sine & cosine, because \theta (angle offset) is unknown
 
### [Periodogram](https://onlinecourses.science.psu.edu/stat510/node/71/)

 - Identity for transforming single cos to cosine and sine
 - Evaluates all frequencies from 1 to n/2, for n distinct time points, of time step t
 
### [tamu](https://www.stat.tamu.edu/~jnewton/stat626/topics/topics/topic4.pdf)

 - Time series can be broken down into constituent frequencies + \bar y
 - Plot (something proportional to amplitude) vs frequency

## Implementing

 - Writing rough interface
