from matplotlib import pyplot as plt


variance =[1,2,4,8,16,32,64,128,256]

bias_squared=[256,128,64,32,16,8,4,2,1]
# print(set(zip(variance,bias_squared)))
total_error=[x+y for x,y in zip(variance,bias_squared)]
print(total_error)

xs=[i for i,c in enumerate(variance)]

plt.plot(xs,variance,'g-',label='variance')

plt.plot(xs,bias_squared,'r-',label='bias^2')

plt.plot(xs,total_error,'b:',label='total error')

plt.legend(loc=9)
plt.xlabel('Model complexity')
plt.title('Bias Model')

plt.show()