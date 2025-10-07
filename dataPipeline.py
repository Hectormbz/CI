import numpy as np
import pandas as pd
import random

m = 2 #gradient
b = 5 # y-intercept
numPoints = 100

#x values
x = np.linspace(0, 100, numPoints)

#y values and noise
noise = np.random.normal(0, 1, numPoints)
y = m * x + b + noise

#save to csv
df = pd.DataFrame({"x": x, "y": y})
df.to_csv("PipelineData.csv", index = False)

