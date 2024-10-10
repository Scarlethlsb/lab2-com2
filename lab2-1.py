import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo CSV
archivo = "C:\\Users\\Scarleth\\Pythom tare\\canciones.csv"

# Leer el archivo CSV
df = pd.read_csv(archivo)

# Filtrar solo las canciones de Taylor Swift
filtro_taylor = df[df["artist(s)_name"] == "Taylor Swift"]

# Seleccionar las columnas necesarias
filtro_taylor = filtro_taylor[['artist(s)_name', 'track_name', 'in_spotify_charts']]

# Ordenar las canciones por las más escuchadas (mayor in_spotify_charts)
filtro_taylor = filtro_taylor.sort_values(by='in_spotify_charts', ascending=False)

# Crear la gráfica de barras
plt.figure(figsize=(10,6))
plt.barh(filtro_taylor['track_name'], filtro_taylor['in_spotify_charts'], color='skyblue')

# Añadir título y etiquetas
plt.title('Canciones más escuchadas de Taylor Swift en Spotify Charts')
plt.xlabel('Veces en los Spotify Charts')
plt.ylabel('Canción')

# Invertir el orden de las canciones para que la más escuchada esté arriba
plt.gca().invert_yaxis()

# Mostrar la gráfica
plt.tight_layout()
plt.show()
