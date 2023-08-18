# from scipy import stats

# p = 0.5
# bernoulliDist = stats.bernoulli(p)

# bernoulliDist.pmf(0)
# bernoulliDist.pmf(1)

from scipy.stats import bernoulli

p = 0.9  # probability of success
k = 2  # number of successes
print(bernoulli.pmf(k))
