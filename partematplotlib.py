import matplotlib.pyplot as plt
import partepandas

df = partepandas.dataframe

x = df["nombre"]
y = df["cantidad"]

plt.bar(x,y)
plt.subplots_adjust(right=1, left=0.06)
plt.show()