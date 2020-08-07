import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score

np.random.seed(2)

pagespeeds = np.random.normal(3.0,1.0,1000)
purchaseAmount = np.random.normal(50.0,10.0,1000) / pagespeeds

#plt.scatter(pagespeeds,purchaseAmount)
#plt.show()

x = np.array(pagespeeds)
y = np.array(purchaseAmount)

p4 = np.poly1d(np.polyfit(x,y,4))

xp = np.linspace(0,7,100)
plt.scatter(x,y)
plt.plot(xp,p4(xp),c='r')
plt.show()

r2 = r2_score(y,p4(x))
print(r2)
