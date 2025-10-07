import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#load data from csv
data = pd.read_csv("PipelineData.csv")
x = data["x"].values
y = data["y"].values

#fit the line
mFit, bFit = np.polyfit(x, y, 1)
m = 2
b = 5

#plot fitted data
plt.scatter(x, y, label="Data")
plt.plot(x, mFit*x+bFit, color = "red", label = "fitted line", linestyle = "--")
plt.plot(x, m*x+b, color = "green", label = "original data",)
plt.legend()
plt.savefig("DataPipelinePlot.png")
plt.show()

