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

#plot data
plt.scatter(x, y, label="Data")
#adding error bars at twice starndard deviation of the noise
plt.errorbar(x, mFit*x+bFit, yerr=20, fmt='none', ecolor='blue', capsize = 1, label = "error bars")
#line of best fit
plt.plot(x, mFit*x+bFit, color = "red", label = "fitted line", linestyle = "--")
#original data 
plt.plot(x, m*x+b, color = "green", label = "original data",)
plt.legend()
plt.savefig("DataPipelinePlot.png")
plt.show()

