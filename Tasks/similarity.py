from math import*
def euclidean_distance(x , y):
    return sqrt(sum (pow (a-b , 2) for a , b in zip (x, y)))
print(euclidean_distance([1,4,7,2] , [2,3,7,0]))
