from matplotlib import pyplot as plt 

movies=["A","B","C","D","E"]

oscars=[5,10,3,6,7]

xs=[i+0.1 for i,c in enumerate(movies)]

# print(xs)

plt.bar(xs,oscars)

plt.ylabel('Awards')

plt.xticks([i+0.1 for i,c in enumerate(movies)],movies)

plt.show()
