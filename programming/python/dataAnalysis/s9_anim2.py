import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

#let's make an "animated" plot that shows how the 
#standard mean and median converge in the case
#where our sample is affected by outliers.

#we want 5% of all points to be outliers, so we 
#draw uniform random numbers for each data point. if that
#number is < 0.05, it's an outlier. if it is, 
#we model it as a gaussian with a mean of 10 and a narrow
#standard deviation of 0.1

nmax = 10000


#first, set up the data without outliers
normmean = 0.0 
normstdev = 1.0
normdata = np.random.normal(normmean, normstdev, nmax)

#now, do the outliers
outmean = 10.0
outstdev = 0.1
outdata = np.random.normal(outmean, outstdev, nmax)

#now choose the actual data from normal or outlier data sets
data = np.zeros(nmax)
test = np.random.uniform(0.0, 1.0, nmax)
for i in np.arange(nmax):
    if (test[i]<0.05):
        #it's an outlier
        data[i] = outdata[i]
    else:
        #it's a normal data point
        data[i] = normdata[i]
        
nbins = 50
#this is how many histogram bins we'll use

histrange = (-11.0, 11.0)
#we want to adopt a fixed histogram range

xgauss = np.linspace(-11, 11, 1000)

model_gauss = stats.norm.pdf(xgauss, loc=normmean, scale=normstdev)  
#this is the underlying distribution of the *normal* data points

#now let's plot all this... we've created 10,000 data points, and we don't
#want to plot them one at a time -- that's just too slow. What we'll do is plot
#the first 30,
#then 100, 110, 120... 200
#then 300, 400 --> 1000
#then 2000, 3000 --> 10,000

nplot1 = np.arange(0,30)
nplot2 = np.arange(39,200,10)
nplot3 = np.arange(299,1000,100)
nplot4 = np.arange(1999, 10000, 1000)
nplot = np.concatenate((nplot1, nplot2, nplot3, nplot4))

for i in nplot:
    #print 'i = ',i

    plt.clf()
    #this just clears the frame...
    plt.xlim(-4.0,11.0)
    plt.ylim(0,0.6) 


    #plot the legend
    plt.plot(7, 0.55, marker='o', color='black', 
             markersize=7)
    plt.plot(7, 0.50, marker='^', color='yellow', 
             markersize=15)
    plt.plot(7, 0.45, marker='^', 
             color='red', markersize=15)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.text(7.5, 0.56, 'Last',fontsize=10)
    plt.text(7.5, 0.54, 'Data Point',fontsize=10)
    plt.text(7.5, 0.49, 'Mean',fontsize=10)
    plt.text(7.5, 0.44, 'Median',fontsize=10)
 
    #plot a counter
    countstring = 'N = ' + str(i+1)
    plt.text(4.0, 0.3, countstring)

    #now plot the histogram
    current_data = data[0:i+1]

    numbers, edges, dummy = plt.hist(current_data, bins=nbins, range=histrange,
                              color="blue", density=True) 
    #density=True automatically normalizes the histogram
    #so that it integrates to unity.
    #that way we can adopt fixed y-limits
    #
    #note that plt.hist is actually pretty cool in that it returns
    #to use the actual values in the histogram: if we do things like
    #  numbers, edges, dummy = plt.hist()
    #then edges gives us the edge locations of the histogram bins and
    #numbers gives us the values in the bins. Don't worry about the additional
    #"dummy" variable for now.
    
    #work out the mean and median of the current data
    mean = np.mean(current_data)
    median = np.median(current_data)
    max = numbers.max()

    #set the y-locations of the markers
    #we make sure these are arrays (e.g. there
    #may be more than one mode)
    ymean = mean*0 + 0.35
    ymedian = median*0 + 0.275
    

    #plot the "true" distribution
    plt.plot(xgauss, model_gauss, linewidth=3, linestyle='-', color='red')
    
    #mark the "true" mean
    xav = np.array([1.*normmean, 1.*normmean])
    yav = np.array([0.0, 0.6])
    plt.plot(xav,yav,linewidth=7, linestyle='-', color='darkgray')

    #mark the location of the last data point
    plt.plot(data[i:i+1],0.5, marker='o', color='black', markersize=7)

    #mark the locations of mean and median
    plt.plot(mean, ymean, marker='^', color='yellow', markersize=15, label='Mean')
    plt.plot(median, ymedian, marker='^', color='red', markersize=15, label='Median')

    #we use plot.draw() instead of plt.show() here because we want to use the *existing*
    #plotting window, rather than a new one each time
    plt.draw()
    
    #this just pauses for 0.01s, which helps us to actually see things
    plt.pause(0.01)

