import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

m = 2
b = 5
yerr = 20
#load data from csv
data = pd.read_csv("PipelineData.csv")
x = data["x"].values
y = data["y"].values

#create set of data that ignores outliers:
deviation = np.abs(y-(m*x+b))
mask = deviation <= yerr
xClean = x[mask]
yClean = y[mask]

#fit the line
mFit, bFit = np.polyfit(xClean, yClean, 1)


#plot data
plt.scatter(x, y, label="Data")
#adding error bars at twice starndard deviation of the noise
plt.errorbar(x, m*x+b, yerr, fmt='none', ecolor='blue', capsize = 1, label = "error bars")
#line of best fit using no outlying values
plt.plot(x, mFit*x+bFit, color = "red", label = "fitted line", linestyle = "--")
#original data 
plt.plot(x, m*x+b, color = "green", label = "original data",)
plt.legend()
plt.savefig("DataPipelinePlot.png")
plt.show()

