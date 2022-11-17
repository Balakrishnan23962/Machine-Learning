import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:\Movies\Walmart.csv")
y=data['Profit']
x=data['Sales']
plt.scatter(y,x)
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()
