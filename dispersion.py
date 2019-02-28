from collections import Counter 
num_friends=[100,49,41,40,25]
from  central_tendencies import mean


def data_range(x):
	return max(x)-min(x)

print(data_range(num_friends))


# variance 

def de_mean(x):
	x_bar=mean(x)
	return [x_i-x_bar for x_i in x]

def variance(x):
	n=len(x)
	deviation=de_mean(x)
	return sum_of_squares(deviation)/(n-1)

def sum_of_squares(v):
	return dot(v,v)

def dot(v,w):
	return sum(v_i*w_i for v_i,w_i in zip(v,w))

print(variance(num_friends))

