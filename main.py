import matplotlib.pyplot as plt
import math
import numpy as np


if __name__ == "__main__":

    plt.rcParams['toolbar'] = 'none'

    # ============== RC CONFIGURATION ==============

    # VOLTAGE in Volt
    voltage = 10
    # RESISTANCE in Ohms
    resistance = 10
    # CAPACITY in Farad
    capacity = 0.007

    # ============== ================ ==============

    tau = resistance * capacity
    tauProcessed = (1 / tau) * tau
    current = voltage / resistance

    # generate time values
    x = np.linspace(0, 5 * tauProcessed, 1000)

    voltageValues = []
    for time in x:
        voltageValues.append(voltage * (1 - math.exp(-(time/tauProcessed))))

    currentValues = []
    for time in x:
        currentValues.append(current * math.exp(-(time/tauProcessed)))

    # subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

    # plot Voltage
    ax1.plot(x, voltageValues, color='blue', label="Voltage (V)")
    ax1.set_xlabel(f"τ  ({tau}s)")
    ax1.set_ylabel("uc(t) (V)")
    ax1.set_title("RC Circuit Behavior")
    ax1.grid(True)
    ax1.legend()

    # plot Current
    ax2.plot(x, currentValues, color='red', label=f"Current (A)")
    ax2.set_xlabel(f"τ ({tau}s)")
    ax2.set_ylabel(f"i(t) (A)")
    ax2.grid(True)
    ax2.legend()

    plt.show()

