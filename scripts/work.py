
# Import libs 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import statsmodels.api as sm

# this url should be the bucket or something like that
# this file was a mess and I wrangled it in Excel
url = 'https://ptcesq.s3.amazonaws.com/mpg/cars.csv'

# load your data set 
df = pd.read_csv(url)

# grab x & y coords 
x = df.year
y = df.mpg 

# OK, let's see how much of an improvement over the years 
# reshape data into an Numpy array (not sure this is necessary) 
X = np.array(x).reshape((-1,1))
X = sm.add_constant(X)
y = np.array(y) 

# lets model 
results = sm.OLS(y, X).fit()

# Get your results 
print(results.summary())


# plot to see how mileage efficieny improved 
plt.scatter(x,y) 

# lets add a regression line
# first extract the y-intercept and slope 
intercept = results.params[0]
slope = results.params[1]

# now we add this line to the plot we just made 
plt.plot(x, slope * x + intercept, color='r') 


#  Make sure that the X11 forwarding is properly installed, 
#  otherwise this won't work 
plt.show() 







