from matplotlib import pyplot as plt

friends=[70,65,72,63,71,64,60,64,67]
minutes=[176,130,105,124,182,145,168,195,132]

labels=['a','b','c','d','e','f','g','h','i']

plt.scatter(friends,minutes) 

for label,friend_count,minute_count in zip(labels,friends,minutes):
	plt.annotate(label,xy=(friend_count,minute_count),xytext=(-5,5),textcoords='offset points')
	plt.title('Minute VS friends')
	plt.xlabel("friends")
	plt.ylabel("daily Minute spennt")

plt.show()