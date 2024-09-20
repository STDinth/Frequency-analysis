import math
import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
a = 2.5  # Amplitud
n = [1, 3, 5, 7, 9]
#### Uppmätta ####
dBVrms_real = [2.25, -15.7, -26.1, -34.5, -34.9]
#### Teoretiska ####
dBVrms_teori = []

def calculate_fourier_coeffecient (a, n):
    Bn_teori = (8 * a) / ((n[i] ** 2) * pi ** 2) * (-1) ** ((n[i] - 1) / 2)
    return Bn_teori

def convert_to_dBVrms_safe(B_n):
    B_n = abs(B_n)
    dBVrms = 20 * math.log10(B_n / np.sqrt(2))
    return dBVrms

for i in range(len(dBVrms_real)):
    Bn_teori = calculate_fourier_coeffecient(a, n)
    dBVrms_value = convert_to_dBVrms_safe(Bn_teori)
    dBVrms_teori.append(dBVrms_value)

plt.figure(figsize=(8, 6))
plt.plot(n, dBVrms_real, label='Uppmätt dBVrms', marker='o')
plt.plot(n, dBVrms_teori, label='Teoretisk dBVrms', marker='x')
plt.xlabel('n (Harmonisk nummer)')
plt.ylabel('dBVrms')
plt.title('Jämförelse av uppmätta och teoretiska dBVrms')
plt.legend()
plt.grid(True)
plt.show()

