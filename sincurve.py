import numpy as np

import matplotlib.pyplot as plot


time = np.arange(0, 10, 0.1);

# Amplitude of the sine wave 

amplitude   = np.sin(time)

plot.plot(time, amplitude)

# TITLE

plot.title('Sine wave')

# X-AXIS

plot.xlabel('Time')

# Y-AXIS
plot.ylabel('Amplitude = sin(time)')

plot.grid(True, which='both')

plot.axhline(y=0, color='k')

plot.show()
