import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

pagespeeds = np.random.normal(3.0,1.0,100)

purchaseAmount = 100 - (pagespeeds + np.random.normal(0,0.1,100))*3

slope, intercept, r_value, p_value, std_err = stats.linregress(pagespeeds,purchaseAmount)
print("slope: %f , intercept: %f , r_value = %f , p_value = %f , Std_err = %f" % (slope, intercept, r_value, p_value, std_err))

def predict(x):
    return slope * x + intercept

fitline = predict(pagespeeds)
plt.scatter(pagespeeds,purchaseAmount)
plt.plot(pagespeeds,fitline,c='r')
plt.show()