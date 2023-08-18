import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objs as go
import seaborn as sns
from scipy.stats import norm

# calculate the probability density function (pdf) of a normal distribution
pdf = norm.pdf(0, loc=0, scale=1)
print(pdf)

# calculate the cumulative distribution function (cdf) of a normal distribution
cdf = norm.cdf(0, loc=0, scale=1)
print(cdf)

# calculate the percent point function (ppf) of a normal distribution
ppf = norm.ppf(0.5, loc=0, scale=1)
print(ppf)


# plot multiple normal distributions in one plot figure
x = np.linspace(-10, 10, 1000)
plt.plot(x, norm.pdf(x, 0, 1), label="mean=0, std=1")
plt.plot(x, norm.pdf(x, 2, 2), label="mean=2, std=2")
plt.plot(x, norm.pdf(x, -3, 0.5), label="mean=-3, std=0.5")
plt.legend()
plt.show()


# plot multiple normal distributions in an interactive plot
x = np.linspace(-10, 10, 1000)
trace1 = go.Scatter(x=x, y=norm.pdf(x, 0, 1), mode="lines", name="mean=0, std=1")
trace2 = go.Scatter(x=x, y=norm.pdf(x, 2, 2), mode="lines", name="mean=2, std=2")
trace3 = go.Scatter(x=x, y=norm.pdf(x, -3, 0.5), mode="lines", name="mean=-3, std=0.5")
data = [trace1, trace2, trace3]
layout = go.Layout(title="Multiple Normal Distributions", xaxis=dict(title="X"), yaxis=dict(title="PDF"))
fig = go.Figure(data=data, layout=layout)
fig.show()
