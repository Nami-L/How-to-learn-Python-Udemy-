import matplotlib.pyplot as plt

# --- Datos combinados ---
# Tiempo en ps (original)
tiempo_ps = [
    100,200,200,200,200,200,300,300,300,300,      # Test 1
    600,700,700,700,700,700,700,800,800,800,800,800, # Test 2
    1200,1200,1200,1200,1200,1200,1200,1200,1200,1200,1200, # Test 3
    1500,1500,1500,1500,1500,1500,1500,1500,1500,1500,1700 # Test 4
]

# Voltaje de entrada Vin (V)
Vin = [
    0.180,0.360,0.540,0.720,0.900,1.080,1.260,1.440,1.620,1.800,
    1.800,1.620,1.440,1.440,1.260,1.080,0.900,0.720,0.540,0.360,0.180,0.000,
    0.000,0.095,0.190,0.285,0.380,0.475,0.570,0.665,0.760,0.855,0.950,
    1.035,1.120,1.205,1.290,1.375,1.460,1.545,1.630,1.715,1.800,1.800
]

# Voltaje de salida Vout (V)
Vout = [
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,1,1,1,1,1,1,1,1,1,
    1,1,1,1,1,1,1,1,1,1,1,
    1,1,1,1,1,1,1,1,1,1,0
]

# --- Graficar ---
plt.figure(figsize=(10,5))
plt.step(tiempo_ps, Vin, where='post', label='Vin (V)', linewidth=2)
plt.step(tiempo_ps, Vout, where='post', label='Vout (V)', linewidth=2)

plt.title('Comportamiento Vin y Vout en los Tests (ps)')
plt.xlabel('Tiempo (ps)')
plt.ylabel('Voltaje (V)')
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.legend()
plt.ylim(-0.2, 2)
plt.show()
