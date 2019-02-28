from matplotlib import pyplot as plt
mentions =[500,505]
years=[2013,2014]
plt.bar([2012.6,2013.6],mentions)
plt.xticks(years)
plt.ylabel('frequency graph')

plt.ticklabel_format(useOffSET=False)

plt.axis([2012.5,2014.5,499,506])

plt.title('Huge Increase ')
plt.show()
