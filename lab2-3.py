#grafico circular: Quesos Canadienses
#enlace:https://www.kaggle.com/datasets/noahjanes/canadian-cheese-directory

# gracias al grafico circular o de pastel podemos apreciar y entender de mejor manera cuales 
# son los quesos favoritos 

import pandas as pd
import matplotlib.pyplot as plt

archivo = "C:\\Users\\Scarleth\\Pythom tare\\cheese_data.csv"

df = pd.read_csv(archivo)


Manufactura_tipo_De_queso_columna = 'ManufacturingTypeEn'  
MoisturePercent_columna = 'MoisturePercent'

datos_agrupados = df.groupby(Manufactura_tipo_De_queso_columna)[MoisturePercent_columna].sum()

plt.figure(figsize=(8, 8))
plt.pie(datos_agrupados, labels=datos_agrupados.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de ' + Manufactura_tipo_De_queso_columna)
plt.axis('equal')  
plt.show()
