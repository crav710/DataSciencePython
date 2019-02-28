from matplotlib import pyplot as plt
from collections import Counter
num_friends=[100,49,41,40,25]

def mean(x):
	return sum(x)/len(x)

def median(v):
	n=len(v)
	sorted_v=sorted(v)
	midpoint=n//2
	if n%2==1:
		return sorted_v[midpoint]
	else:
		low=midpoint-1
		high=midpoint
		return((sorted_v[low]+sorted_v[high])/2)

def quantile(x,p):
	p_index=int(p*len(x))
	return sorted(x)[p_index] 

def mode(x):
	counts=Counter(x)
	# print(counts)
	max_count=max(counts.values())
	# print(max_count)
	# print(counts.items())
	return [x_i for x_i,count in counts.items() if count==max_count]


# print(mode(num_friends))