import matplotlib.pyplot as plt
import math
import numpy as np

plt.rcParams['toolbar'] = 'none'

# ============== RC CONFIGURATION ==============

# VOLTAGE in Volt
voltage = 100
# RESISTANCE in Ohms
resistance = 1000
# CAPACITY in Farad
capacity = 0.000001

# ============== ================ ==============

tau = resistance * capacity
current = voltage / resistance

# generate time values
x = np.linspace(0, 5 * tau, 100)

voltageValues = []
for time in x:
    voltageValues.append(voltage * (1 - math.exp(-(time/tau))))

currentValues = []
for time in x:
    currentValues.append((current * math.exp(-(time/tau)))*1000)

# plotting the points
plt.plot(x * 1000, voltageValues, label = "Voltage [u(t)]")
plt.plot(x * 1000, currentValues, label = "Current [i(t)]")

# naming the x axis
plt.xlabel('τ')
# naming the y axis
plt.ylabel('%')
plt.title('Switching RC Circuit')
plt.legend()
plt.grid(True)
plt.show()
