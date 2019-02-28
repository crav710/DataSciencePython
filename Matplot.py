from matplotlib import pyplot as plt 

years=[1950,1960,1970,1980,1990,2000]

gdp=[300.2,263.2,323.2,434.5,987.2,123.2]

# creating a line chart
plt.plot(years,gdp,color='red',marker='o',linestyle='solid')

plt.ylabel("GDP")

plt.show()