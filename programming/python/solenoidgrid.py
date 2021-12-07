from matplotlib import pyplot as plt
import numpy as np
import biot_savart as bs
from scipy import stats
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp





#bs.write_target_volume("coil.txt", "coil", (30, 15, 15), (-5, -0.5, -2.5), 1, 1)
# generates a target volume from the coil stored at coil.txt
# uses a 30 x 15 x 15 bounding box, starting at (-5, -0.5, -2.5)
# uses 1 cm resolution

#bs.plot_coil("coil.txt")
# plots the coil stored at coil.txt

#fields, positions = bs.read_target_volume("coil")
# reads the volume we created

#bs.plot_fields(fields, positions, which_plane='z', level=5, num_contours=50)
# plots the fields we just produced
# plotting along the plane x = 5, with 50 contours


#help(bs.write_target_volume)
#help(bs.helmholtz_coils)
#1help(bs.get_field_vector)


bs.helmholtz_coils("helm1.txt", "helm2.txt", 397, 15.15, 20, 1.5)
# makes a pair of helmholtz coils
# 50 segments each, with radius of 5 cm
# spaced out by 2 cm, located at z = +/- 1 respectively
# 1 amp of current

#bs.plot_coil("helm1.txt", "helm2.txt")
bs.plot_coil("helm1.txt")

bs.write_target_volume("helm1.txt", "targetvol1", (0, 80, 15), (0, -40, 0), 0.5, 0.5)
#bs.write_target_volume("helm2.txt", "targetvol2", (20, 20, 20), (-10, -10, -10), 0.5, 0.5)
# use a target volume of size 10, centred about origin

h1, pos1 = bs.read_target_volume("targetvol1")
#h2, pos2 = bs.read_target_volume("targetvol2")
# produce the target volumes we want

# use linear superposition of magnetic fields, to get the combined effects of multiple coils
#h_total = h1 + h2

bs.plot_fields(h1*1000, pos1, which_plane='x', level=0, num_contours=50)

#print(bs.get_field_vector(h1, (0, 10, 13), (0, 0, 0), 0.5))
magnetic_field_gauss = []
magnetic_field_gauss1 = []
magnetic_field_gauss2 = []
for y in range(-40, 41, 1):
    field = bs.get_field_vector(h1, (0, y, 13), (0, -40, 0), 0.5)
    magnetic_field_gauss.append([y, field[2]])
    
for y in range(-40, 41, 1):
    field = bs.get_field_vector(h1, (0, y, 11), (0, -40, 0), 0.5)
    magnetic_field_gauss1.append([y, field[2]])
    
for y in range(-40, 41, 1):
    field = bs.get_field_vector(h1, (0, y, 15), (0, -40, 0), 0.5)
    magnetic_field_gauss2.append([y, field[2]])
    
xvalues = []
yvalues = []
xvalues12 = []
yvalues12 = []
xvalues14 = []
yvalues14 = []
for q in magnetic_field_gauss[:]:
    x = q[0]
    y = q[1] * 1000
    xvalues.append(x)
    yvalues.append(y)
    
for q in magnetic_field_gauss1[:]:
    x = q[0]
    y = q[1] * 1000
    xvalues12.append(x)
    yvalues12.append(y)

for q in magnetic_field_gauss2[:]:
    x = q[0]
    y = q[1] * 1000
    xvalues14.append(x)
    yvalues14.append(y)
    
plt.grid()
plt.xlabel("Distance (cm)")
plt.ylabel("x component Magnetic Field Strength (Gauss)")


yerror = []
for q in range(len(yvalues12)):
    x = yvalues12[q] - yvalues[q]
    yerror.append(x)



distance, gauss = np.loadtxt('data.txt', \
                                        unpack = True, \
                                        usecols = (0, 1), \
                                        delimiter = ',')
distanceapp = []
for x in distance:
    z = x + 40
    distanceapp.append(z)
    

plt.plot(xvalues, yvalues, label="Theoretical B_x magnetic field")
plt.plot(distance, gauss, label="Experimental B_x magnetic field")
plt.errorbar(xvalues, yvalues, yerr=yerror, elinewidth=1)
#plt.plot(xvalues12, yvalues12, label="Theoretical B_x magnetic field")
#plt.plot(xvalues14, yvalues14, label="Theoretical B_x magnetic field")
plt.legend(loc=2, prop={'size': 7})
plt.show()

if False:
    
    def gaussian(x, mu, sig):
        return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
    
    x_values = np.arange(-40, 40,)
    mu = np.mean(yvalues)
    sig = np.std(yvalues)
    plt.plot(x_values, gaussian(x_values, mu, sig))
    
    plt.show()

if False:
    mean = np.mean(xvalues)
    standard_deviation = np.std(xvalues)
    
    x_values = np.arange(-40, 40, 0.1)
    y_values = stats.norm(mean, standard_deviation)
    
    #plt.plot(x_values, y_values.pdf(x_values)*25.75*13, label="")
    plt.plot(x_values, y_values.pdf(x_values), label="Normalised gaussian distribution of theoretical values")
    plt.legend(loc=2, prop={'size': 6})



x = np.asarray(xvalues)
y = np.asarray(yvalues)

n = len(x)
mean = sum(x*y)/n
#sigma = sum(y*(x-mean)**2)/n
sigma = np.std(xvalues)

def gaus(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(gaus,x,y,p0=[1,mean,sigma])
#print(popt, sigma)

plt.plot(x,y,label='Theoretical B_x magnetic field')
plt.plot(x,gaus(x,*popt),label='Gaussian fit')
plt.legend(loc=2, prop={'size': 7})
plt.grid()
plt.show()


#gaussdis = []
#for x in range(len(xvalues)):
 #   poop = gaus(x, *popt)[x]

print(gaus(x,*popt))
print(yvalues)
#print(magnetic_field_gauss)
for i in range(len(xvalues)):
    chi = 0
    chi += ((yvalues[i] - gaus(x, *popt)[i])**2)/(gaus(x, *popt)[i])
    
print(chi)



# def biosavart(z,x):
#    magnitude = 









# def main():
#    for z in range(20):
#        for x in range(20):
#            magnitude = biosavart(z,x)








#if __name__ == '__name__':
 #   main()
    