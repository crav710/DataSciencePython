import random

def run_exp():
	return (random.random()<0.5 for i in range(1000))

# print(run_exp)

def reject_fairness(experiment):
	for flip in experiment:
		print (flip)
	num_heads=len([flip for flip in experiment if flip])
	return num_heads<469 or num_heads >531

random.seed(0)

experiments=[run_exp() for i in range(1000)]
# print(experiments)
num_rejections=len([experiment for experiment in experiments if reject_fairness(experiment)])
reject_fairness(experiments[0])

print (num_rejections)