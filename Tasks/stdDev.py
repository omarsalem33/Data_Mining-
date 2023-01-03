# without built in function

from math import sqrt
data= [11, 8, 30, 3, 40, 4, 50, 66, 6, 70, 45] 

mean =sum(data)/len(data)
SUM= 0
for i in data :
    SUM +=(i-mean)**2



stdeV = sqrt(SUM/(len(data)-1)) 
print("The Standard Deviation of the sample is:",(stdeV))

# with builtin function

# import statistics

# data = [11,8,8,3,4,4,5,6,6,7,8]
# print("The Standard Deviation of the sample is:",(statistics.stdev(data)))