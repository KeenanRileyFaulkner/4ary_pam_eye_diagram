import numpy as np
import matplotlib.pyplot as plt

# Parameters
symbols = np.array([-3, -1, 1, 3]) # 4-PAM symbols BEFORE scaling with A
E_avg = 5 # Average energy of the transmitted symbols as defined in the problem (joules)
num_symbols = 200 # As defined in the problem
samples_per_symbol = 16 # As defined in the problem

# Solve for A
# For 4-ary PAM with symbols [-3, -1, 1, 3], and E_avg = 5, A is:
# sqrt(5 / (1/4 * (3^2 + 1^2 + 1^2 + 3^2)))
# = sqrt(5 / (1/4 * (9 + 1 + 1 + 9)))
# = sqrt(5 / (1/4 * 20))
# = sqrt(5 / 5)
# = 1
A = np.sqrt(E_avg / np.mean(symbols**2))

# Scale the symbols by A
symbols_scaled = symbols * A

# Generate random symbols from the scaled symbol set
random_symbols = np.random.choice(symbols_scaled, num_symbols)

# Create the NRZ signal by repeating each symbol for the duration of its symbol period
nrz_signal = np.repeat(random_symbols, samples_per_symbol)

# Create the time vector for the NRZ signal
t = np.linspace(0, num_symbols, len(nrz_signal))

# Plot the eye diagram
plt.figure(figsize=(10, 6))
# For
for i in range(0, len(nrz_signal) - 2 * samples_per_symbol, samples_per_symbol):
    plt.plot(t[:2 * samples_per_symbol], nrz_signal[i:i + 2 * samples_per_symbol], color='blue', alpha=0.5)

plt.title('4-PAM Eye Diagram for NRZ Signal with A = 1')
plt.xlabel('Time (normalized to symbol period)')
plt.ylabel('Amplitude')
plt.grid(True)

# zoom in on the x-axis to see crossing points
plt.xlim(0.9, 1.0375)

# Save the plot out to a file
plt.savefig('4_ary_pam_eye.png')