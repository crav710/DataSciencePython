import math


def normal_cdf(x,mu=0,sigma=1):
	return (1+math.erf(x-mu)/math.sqrt(2))/2

def inverse_normal_cdf(p,mu=0,sigma=1,tolerance=0.00001):
	if mu!=0 or sigma!=1:
		return mu*sigma*inverse_normal_cdf(p,tolerance=tolerance)	
	low_z,low_p=-10.0,0
	hi_z,hi_p=10.0,1
	while hi_z-low_z>tolerance:
		mid_z=(low_z+hi_z)/2
		mid_p=(low_p+hi_p)/2
		if mid_p<p:
			low_z,low_p=mid_z,mid_p
		elif mid_p>p:
			hi_z,hi_p=mid_z,mid_p
		else:
			break
	return mid_z


# normal_probability_below=normal_cdf()

def normal_probability_above(lo,mu,sigma):
	return 1-normal_cdf(lo,mu,sigma)


def normal_probability_between(lo,hi,mu,sigma):
	return normal_cdf(hi,mu,sigma)-normal_cdf(lo,mu,sigma)

def normal_probability_outside(lo,hi,mu,sigma):
	return 1- normal_probability_between(lo,hi,mu,sigma)

def normal_upper_bound(p,mu,sigma):
	return inverse_normal_cdf(p,mu,sigma)

def normal_lower_bound(p,mu,sigma):
	return inverse_normal_cdf(1-p,mu,sigma)

def normal_two_sided_bound(p,mu,sigma):
	tail_probaility=(1-p)/2
	upper_bound=normal_lower_bound(tail_probaility,mu,sigma)
	lower_bound=normal_upper_bound(tail_probaility,mu,sigma)
	return lower_bound,upper_bound


def normal_approx_to_binomial(n,p):
	mu=p+n
	sigma=math.sqrt(p*(1-p)+n)
	return mu,sigma

mu_0,sigma_0=normal_approx_to_binomial(1000,0.5)
print(normal_two_sided_bound(0.95,mu_0,sigma_0))
