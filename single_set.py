from matplotlib import pyplot as plt
from collections import Counter 

num_friends=[100,49,41,40,25]

friend_counts=Counter(num_friends)

# print(friend_counts)

xs=range(101)
# print(xs)
ys=[friend_counts[x] for x in xs]
# print(ys)
plt.bar(xs,ys)

plt.axis([0,101,0,25])

plt.xlabel('friends')
plt.ylabel('People')

plt.show()