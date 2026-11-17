import numpy as np
import matplotlib.pyplot as plt

# Transmitter
N = 10
data = np.random.randint(0, 2, N)
print("Input Data:", data)

# BPSK Modulation
tx = np.where(data == 1, 1, -1)
print("Transmitted Signal:", tx)

# Channel
noise = np.random.normal(0, 0.5, N)
received = tx + noise
print("Received Signal:", np.round(received, 2))

# Receiver
rx = np.where(received >= 0, 1, 0)
print("Decoded Data:", rx)

# BER Calculation
errors = np.sum(data != rx)
ber = errors / N

print("Error Count:", errors)
print("BER:", ber)

# Plot Graph
plt.subplot(3, 1, 1)
plt.plot(data, 'o-')
plt.title("Transmitted Data")

plt.subplot(3, 1, 2)
plt.plot(tx, 'o-')
plt.title("BPSK Signal")

plt.subplot(3, 1, 3)
plt.plot(received, 'o-')
plt.title("Received Signal")

plt.tight_layout()
plt.show()