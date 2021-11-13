import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

#let's make an "animated" plot that shows the histogram for 
#measurements of some quantity -- each subject to the same
#Gaussian uncertainty -- as the number of measurements increases
plt.rcdefaults()
nmax = 10000
truemean = 0.0 
truestdev = 1.0
data = np.random.normal(truemean, truestdev, nmax)
#these will be our random measurements

nbins = 30
#this is how many histogram bins we'll use

histrange = (-4.0, 4.0)
#we want to adopt a fixed histogram range

xgauss = np.linspace(-5, 5, 1000)

model_gauss = stats.norm.pdf(xgauss, loc=truemean, scale=truestdev)  
#this is the underlying distribution from which the
#uncertain measurements are drawn

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
    plt.xlim(-4.0,4.0)
    plt.ylim(0,0.6) 

    #plot the legend
    plt.plot(-3.5, 0.55, marker='o', color='black', 
             markersize=7)
    plt.plot(-3.5, 0.50, marker='^', color='yellow', 
             markersize=15)
    plt.plot(-3.5, 0.45, marker='^', 
             color='red', markersize=15)
    plt.plot(-3.5, 0.40, marker='^', 
             color='green', markersize=15)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.text(-3.25, 0.56, 'Last',fontsize=10)
    plt.text(-3.25, 0.54, 'Data Point',fontsize=10)
    plt.text(-3.25, 0.49, 'Mean',fontsize=10)
    plt.text(-3.25, 0.44, 'Median',fontsize=10)
    plt.text(-3.25, 0.39, 'Mode',fontsize=10)

    #plot a counter
    countstring = 'N = ' + str(i+1)
    plt.text(2.0, 0.5, countstring)
 
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

    #modeval is the *value* of the most common
    #element in the histogram, so now we want its location(s)
    mode = np.array([])
    for j in np.arange(nbins):
        if (max == numbers[j]):
            mode = np.concatenate([mode, [0.5*(edges[j]+edges[j+1])]])

    #set the y-locations of the markers
    #we make sure these are arrays (e.g. there
    #may be more than one mode)
    ymean = mean*0 + 0.35
    ymedian = median*0 + 0.275
    ymode = mode*0 + 0.2
    

    #plot the "true" distribution
    plt.plot(xgauss, model_gauss, linewidth=3, linestyle='-', color='red')
    
    #mark the "true" mean
    xav = np.array([1.*truemean, 1.*truemean])
    yav = np.array([0.0, 0.6])
    plt.plot(xav,yav,linewidth=7, linestyle='-', color='darkgray')

    #mark the location of the last data point
    plt.plot(data[i:i+1],0.5, marker='o', color='black', markersize=7)

    #mark the locations of mean, median and mode
    plt.plot(mean, ymean, marker='^', color='yellow', markersize=15, label='Mean')
    plt.plot(median, ymedian, marker='^', color='red', markersize=15, label='Median')
    plt.plot(mode, ymode, marker='^', color='green', markersize=15, label='Mode')

    #we use plot.draw() instead of plt.show() here because we want to use the *existing*
    #plotting window, rather than a new one each time
    plt.draw()
    
    #this just pauses for 0.01s, which helps us to actually see things
    plt.pause(0.01)

