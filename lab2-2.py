#grafico de lineas: Goleadores de balon de oro
#enlace:https://www.kaggle.com/datasets/farzammanafzadeh/ballon-dor-2024-nominees-league-stats

#podemos apreciar gracias el grafico lineal con mayor presicion cuales son los jugadores que han 
#anotado mas goles en el balon de oro

import pandas as pd
import matplotlib.pyplot as plt


archivo = "C:\\Users\\Scarleth\\Pythom tare\\2024 Ballon.csv"

try:
    df = pd.read_csv(archivo)
    
    print("Datos cargados con éxito. Primeras filas del archivo:")
    print(df.head())
    
    plt.figure(figsize=(10,6))

    for player in df['player'].unique():
        player_data = df[df['player'] == player]
        plt.plot(player_data['Performance-G+A'], player_data['age'], label=player)

    plt.title('Evolución de la tabla de goleadores en el Balón de Oro')
    plt.xlabel('Performance-G+A')
    plt.ylabel('age')
    plt.legend(title='player')
    plt.grid(True)

    plt.show()

except FileNotFoundError:
    print(f"El archivo no se encontró en la ruta especificada: {archivo}")
except Exception as e:
    print(f"Ha ocurrido un error al cargar el archivo: {e}")



