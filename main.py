import matplotlib.pyplot as plt
import math
import numpy as np
from order_of_magnitude import order_of_magnitude


if __name__ == "__main__":

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
    current_si_symbol = order_of_magnitude.symbol(current)

    # generate time values
    x = np.linspace(0, 5 * tau, 100)

    voltageValues = []
    for time in x:
        voltageValues.append(voltage * (1 - math.exp(-(time/tau))))

    currentValues = []
    for time in x:
        currentValues.append((current * math.exp(-(time/tau)))*1000)

    # plotting the points
    plt.plot(x * 1000, voltageValues, label = "Voltage")
    plt.plot(x * 1000, currentValues, label = "Current")

    # naming the x axis
    plt.xlabel('τ')
    # naming the y axis
    current_si_symbol =
    plt.ylabel(f'V / {current_si_symbol[1]}A')
    plt.title('Switching RC Circuit')
    plt.legend()
    plt.grid(True)
    plt.show()

