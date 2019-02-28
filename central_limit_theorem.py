import math
import numpy as np
from matplotlib import pyplot as plt 

mu,sigma=0,1

s=np.random.normal(mu,sigma,1000) 
# print(s)

count,bins,ignored=plt.hist(s,30,density=True)

# print(count)
# print("bins")
# print(bins)

plt.plot(bins,1/(sigma*np.sqrt(2*np.pi)*np.exp((bins-mu)**2/(2*sigma**2))),linewidth=2,color='r')

plt.title("the central limit theorem")

plt.show()