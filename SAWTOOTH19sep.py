import numpy as np
import math
import matplotlib.pyplot as plt

A = 2.5  # Amplituden (V)
f = 1000  # 1kHz
R = 8200  # ohm
C = 10 * 10**(-9)  # nF
pi = np.pi

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Funktion för att beräkna överföringsfunktionen
def calculate_transfer_function(omega, R, C):
    return 1 / (np.sqrt((omega * R * C) ** 2 + 1))

# Funktion för att beräkna Fourierkoefficienten för en sågtandsvåg
def calculate_fourier_coeffecient(A, n):
    return ((2 * A) / (n * pi)) * ((-1) ** (n - 1))

# Funktion för att konvertera till dBVrms
def convert_to_dBVrms(B_n):
    return 20 * math.log10(B_n / np.sqrt(2))

### Uppmätta dBVrms-värden
In_dBVrms = [1.0, -5.35, -10.1, -15.3, -19.7, -20.5, -25.7, -31.7, -46.1, -44.1]
Ut_dBVrms = [0.15, -7.35, -15.3, -20.1, -26.9, -30.0, -38.9, -44.1, -48.5, -55.3]
B_n_ut_dBVrms_list = []

# Loop för beräkning av dBVrms för ingångssignalen
for i in range(len(n)):
    ###### Uin ######
    B_n_in = calculate_fourier_coeffecient(A, n[i])  
    B_n_in = abs(B_n_in)
    B_n_in_dBVrms = convert_to_dBVrms(B_n_in)
    B_n_in_dBVrms = round(B_n_in_dBVrms, 3)
    

    ###### Uut #######
    omega = 2*pi*n[i]*f
    H = calculate_transfer_function(omega, R, C)
    B_n_ut = H * B_n_in
    B_n_ut_dBVrms = convert_to_dBVrms(B_n_ut)
    B_n_ut_dBVrms = round(B_n_ut_dBVrms, 3)
    B_n_ut_dBVrms_list.append(B_n_ut_dBVrms)
    print("________________________________________")
    print(f"Frequency = {1000*n[i]}")
    print(f"dBVrms in (teoretiska) = {B_n_in_dBVrms}")
    print(f"dBVrms in (uppmätta) = {In_dBVrms[i]}\n")
    print(f"dBVrms ut (teoretiska) = {B_n_ut_dBVrms}")
    print(f"dBVrms ut (uppmätta) = {Ut_dBVrms[i]}")

# Plotta teoretiska och uppmätta dBVrms-värden för ingången
plt.figure(figsize=(8, 6))
plt.plot(n, B_n_ut_dBVrms_list, label='Teoretiska dBVrms Ut', marker='o')
plt.plot(n, Ut_dBVrms, label='Uppmätta dBVrms Ut', marker='x')
plt.xlabel('Harmonisk nummer (n)')
plt.ylabel('dBVrms')
plt.title('Jämförelse mellan teoretiska och uppmätta dBVrms-värden (Utgång)')
plt.legend()
plt.grid(True)
plt.show()
