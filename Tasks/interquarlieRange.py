# Import the numpy library as np
import numpy as np

data= [11, 8, 30, 3, 40, 4, 50, 66, 6, 70, 45] 

# First quartile (Q1)
Q1 = np.median(data[:10])

# Third quartile (Q3)
Q3 = np.median(data[10:])

# Interquartile range (IQR)
IQR = Q3 - Q1

print("The IQR is:",IQR)
