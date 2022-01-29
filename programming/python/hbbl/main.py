import math
import statistics as s
import numpy as np
from scipy import stats, optimize as opt, special
from matplotlib import pyplot as plt

class one:
    '''functions needed for part one'''
    def getData(self, filename):
        '''self explanatory
            args: filename
            returns: nothing, instead outputs global variables of 
            Object, parallax, errpar, Period, m, A, errA'''
        global Object, parallax, errpar, Period, m, A, errA
        Object, parallax, errpar, Period, m, A, errA = np.genfromtxt(filename, \
                                            unpack = True, \
                                            usecols = (0, 1, 2, 3, 4, 5, 6), \
                                            comments = '#', \
                                            dtype = str)

        parallax = [eval(x) for x in parallax]
        errpar = [eval(x) for x in errpar]
        Period = [eval(x) for x in Period]
        m = [eval(x) for x in m]
        A = [eval(x) for x in A]
        errA = [eval(x) for x in errA]

    def distanceFromEarth(self, p_mas, p_maserr):
        '''calculate distance from earth from p_mas including its error
            args: p_mas, p_maserr | type = list
            returns: nothing, instead outputs new global variables of d_pc and d_pcerr (which are defined as distance from the Earth'''
        global d_pc
        global d_pcerr
        d_pc = []
        d_pcerr = []
        for x in p_mas:
            d_pc.append(1000/x)
        for x in p_maserr:
            d_pcerr.append((1000)/x)

    def Mabs(self, m, A, d_pc, d_pcerr, errA):
        '''calculate Mabs including its error from 
            args: apparent magnitudes, extinction, distance from earth, extinction error | type = list
            returns: nothing, instead outputs M absolute and M absolute error to global variables'''
        global M
        global Merr
        M = []
        Merr = []
        for x in range(len(m)):
            M.append(m[x] - (5 * np.log10(d_pc[x])) + 5 - A[x])
            # Merr.append(M[x] * (np.sqrt(((errA[x] / A[x]) ** 2) + ((np.log10(d_pcerr[x]) / np.log10(d_pc[x])) ** 2))))
            # Merr.append((np.sqrt(((errA[x]) ** 2) + (5* d_pcerr[x] / errpar[x]) ** 2)))
            Merr.append((np.sqrt(((errA[x]) ** 2) + (5 * (np.log(d_pcerr[x]) / d_pc[x]))) ** 2))
        # print(Merr)
        
    def func(self, x, slope, intercept):
        '''form of the line of fit for curve_fit'''
        line = intercept + slope*x
        return line

    def chi2(self, O, E, sig):
        '''calculate chi2 from
            args: observed values, expected values, sigma balls | type = list
            returns: chi squared'''
        chisq = 0
        for q in range(len(O)):
            # chipart = (((O[q] - E[q]) ** 2) / E[q] ) + 1
            chipart = (((O[q] - E[q]) ** 2) / (sig[q] ** 2) )
            # print(chipart)
            chisq += chipart
        return chisq

def partone():
    '''does all the calls necessary for part 1, generates graphs and prints
        to terminal important values'''
    one.getData("MW_Cepheids.dat")
    one.distanceFromEarth(parallax, errpar)
    one.Mabs(m, A, d_pc, d_pcerr, errA)
    plt.title('M vs $\log_{10}(P)$')
    plt.xlabel('Period [$\log_{10}(P[days])$]')
    plt.ylabel('Absolute Magnitude [mag]')
    plt.errorbar(np.log10(Period), M, xerr = None, yerr = Merr, ls = 'none')
    plt.scatter(np.log10(Period), M, marker = 'x')
    sig_y=Merr
    start_slope = 5.0
    start_intercept = -10
    global popt, pcov
    popt, pcov = opt.curve_fit(f=one.func, xdata=np.log10(Period), ydata=M, \
                                        sigma=sig_y, p0=(start_slope, start_intercept),\
                                        absolute_sigma=True)
    y = []
    for a in range(len(m)):
        y.append((popt[0] ) * (np.log10(Period[a])) + popt[1])#  - 3.637)
    plt.plot(np.log10(Period), y)
    perr = np.sqrt(np.diag(pcov))
    best_slope = popt[0]
    best_intercept = popt[1]
    chi2 = one.chi2(M, y, Merr)
    print('Best slope:', best_slope)
    print('Best intercept:', best_intercept)
    print('X^2:', chi2)
    print('X^2 normalised:', chi2 / (len(m) - 1))
    global slope_err, intercept_err
    slope_err = np.sqrt(pcov[0, 0])
    intercept_err = np.sqrt(pcov[1, 1])
    print('error on the slope:', slope_err)
    print('error on the interecept:', intercept_err)
    plt.show()

class two:
    '''functions needed for part 2'''
    def getData(self, filename):
        '''are you really asking wha this does?
            args: filename
            returns: nothing, outputs data to global variables'''
        global Name, logP, m1
        Name, logP, m1 = np.genfromtxt(filename, \
                                        unpack = True, \
                                        comments = '#', \
                                        dtype = str)
        logP = [eval(x) for x in logP]
        m1 = [eval(x) for x in m1]
        global Amw
        Amw = 0.0682
        Name = np.delete(Name, 6)
        logP = np.delete(logP, 6)
        m1 = np.delete(m1, 6)
    
    def distanceFromEarth(self, logP, m1, Amw):
        '''calculates distance from earth to object from
            args: log of period - type = list, m apparent - type = list, extinction - type = float
            returns: nothing, outputs to global variables ngdis, M1, M1err, ngdiserr, ngdisaverage and ngdisaverageerr'''
        global ngdis
        global M1
        global M1err
        global ngdiserr
        global ngdisaverage
        global ngdisaverageerr
        ngdisaverageerr = 0
        ngdisaverage = 0
        ngdiserr = []
        M1errupper = []
        M1errlower = []
        M1err = []
        M1 = []
        ngdis = []
        for x in range(len(logP)):
            M1.append((popt[0] * logP[x]) + popt[1])
        for x in range(len(logP)):
            M1errupper.append(((popt[0] + slope_err) * logP[x]) + (popt[1] + intercept_err))
        for x in range(len(logP)):
            M1errlower.append(((popt[0] - slope_err) * logP[x]) + (popt[1] - intercept_err))
        for x in range(len(logP)):
            ngdis.append(10 ** ((m1[x] - M1[x] + 5 - Amw) / 5))
        for x in range(len(logP)):
            M1err.append(M1errupper[x] - M1errlower[x])
        for x in range(len(logP)):
            ngdiserr.append(10 ** ((m1[x] - M1err[x] + 5 - Amw) / 5))
        for x in range(len(logP)):
            ngdisaverage += ngdis[x]
            if x == len(logP) - 1:
                ngdisaverage = ngdisaverage / len(logP)
        for x in range(len(logP)):
            ngdisaverageerr += ngdiserr[x]
            if x == len(logP) - 1:
                ngdisaverageerr = ngdisaverageerr / len(logP)

def parttwo():
    '''does all the calls necessary for part 2, generates graphs and prints
        to terminal important values'''
    two.getData('ngc4527_cepheids.dat')
    two.distanceFromEarth(logP, m1, Amw)
    # plt.errorbar(logP, ngdis, yerr = ngdiserr, ls = 'none')
    # plt.xlabel("pog")
    # plt.ylabel("pog")
    # plt.scatter(logP, ngdis, marker = 'x')
    # print(ngdis)
    # aver = 0
    # for x in range(len(ngdis)):
    #     aver += ngdis[x]
    # average = aver/len(ngdis)
    # print(M1err)
    # print(average)
    # plt.show()
    print('Distance from ngc4527 (from average of all data in Parsecs):', ngdisaverage)
    print('Error in the distance from ngc4527 (average of all errors in Parsecs):', ngdisaverageerr)

class three:
    '''functions needed for part 3'''
    def getData(self, filename):
        '''self explanatory
            args: filename
            returns: nothing, instead outputs global variables of 
            Galaxy, Recession, distance, distanceerr, distance1, distanceerr1'''
        global Galaxy, Recession, distance, distanceerr, distance1, distanceerr1
        distance1, distanceerr1 = [], []
        Galaxy, Recession, distance, distanceerr = np.genfromtxt(filename, \
                                        unpack = True, \
                                        comments = '#', \
                                        dtype = str)
        Recession = [eval(x) for x in Recession]
        distance = [eval(x) for x in distance]
        distanceerr = [eval(x) for x in distanceerr]
        for x in range(len(distance)):
            distance1.append(distance[x] * 1000000)
            distanceerr1.append(distanceerr[x] * 1000000)
        # Recession = np.ndarray.tolist(np.delete(Recession, [0, 4]))
        # distance = np.ndarray.tolist(np.delete(distance, [0, 4]))
        # distanceerr = np.ndarray.tolist(np.delete(distanceerr, [0, 4]))

    def hbblconst(self, v_rec, D_gal, D_galerr = None):
        '''calculates hubble constant for inputs of int or list
            args: recession velocity, distance from galaxy, distance from galaxy error | type = list or int or floats but must all be the same
            returns: H_0 and H_0'''
        if type(v_rec) is list: # and type(D_gal) is list and type(D_galerr) is list:
            H_0 = []
            H_0err = []
            for x in range(len(v_rec)):
                H_0.append(v_rec[x] / D_gal[x])
                H_0err.append((v_rec[x] / D_gal[x] + D_galerr[x]) - (v_rec[x] / D_gal[x] - D_galerr[x]))
                return [H_0, H_0err]
        if type(v_rec) is float or int:
            H_0 = v_rec / D_gal
            return H_0
        return None
    
    def func(self, x, slope):
        '''form of slope for curve_fit'''
        line =slope*x
        return line
    
    def chi2(self, O, E):
        '''calculate chi squared without knowing sigma balls
            args: observed values, expected values | type = list
            returns: chi squared'''
        chisq = 0
        for q in range(len(O)):
            # chipart = (((O[q] - E[q]) ** 2) / E[q] ) + 1
            chipart = (((O[q] - E[q]) ** 2) / ((E[q]))) #+ 31000) )
            # print(chipart)
            chisq += chipart
        return chisq

def partthree():
    '''does all the calls necessary for part 3, generates graphs and prints
        to terminal important values'''
    global v_rec_ngc4527
    v_rec_ngc4527 = 1152
    three.getData('other_galaxies.dat')
    # plt.scatter(distance, Recession)
    # plt.show()
    ngdisaverageMpc = ngdisaverage / 1000000
    ngdisaverageerrMpc = ngdisaverageerr / 1000000
    print('Hubble constant calculated from only ngc4527 (km/s per Mpc):',three.hbblconst(v_rec_ngc4527, ngdisaverageMpc),\
        '±', (three.hbblconst(v_rec_ngc4527, ngdisaverageMpc - ngdisaverageerrMpc) - three.hbblconst(v_rec_ngc4527, ngdisaverageMpc + ngdisaverageerrMpc)))
    hubbleconst = three.hbblconst(Recession, distance, distanceerr)
    # print('Hubble constant calculated from other_galaxies.dat (km/s per Mpc):', *hubbleconst[0], '±', *hubbleconst[1])
    
    start_slope = 10
    start_intercept = -100
    popt1, pcov1 = opt.curve_fit(f=three.func, xdata=Recession, ydata=distance, \
                                        sigma=distanceerr, p0=(start_slope),\
                                        absolute_sigma=True)
    velocitycalc = []
    for x in range(len(distance)):
        velocitycalc.append((1 / popt1[0] * distance[x]))
    # print(one.chi2(Recession, velocitycalc, distanceerr))
    

    slope_err = np.sqrt(pcov1[0, 0])
    # intercept_err = np.sqrt(pcov1[1, 1])
    print('Hubble constant calculated from only other_galaxies.dat (km/s per Mpc):', 1 / popt1[0], '±', slope_err)
    # print(slope_err, intercept_err)
    plt.plot(distance, velocitycalc)
    plt.title('just other_galaxies.dat')
    plt.ylabel('Velocity of Recession (km/s)')
    plt.xlabel('Distance of galaxy from Earth (Mpc)')
    plt.errorbar(distance, Recession, xerr = distanceerr, ls = 'none')
    plt.scatter(distance, Recession, marker = 'x')
    plt.show()

    # print(distance)
    distance.append(ngdisaverageMpc)
    # print(distance)
    distanceerr.append(ngdisaverageerrMpc)
    Recession.append(v_rec_ngc4527)
    # print(ngdisaverageerrMpc)
    popt2, pcov2 = opt.curve_fit(f=three.func, xdata=distance, ydata=Recession, \
                                        sigma=None, p0=(start_slope),\
                                        absolute_sigma=True)
    newvelocitycalc = []
    for x in range(len(distance)):
        newvelocitycalc.append((popt2[0] * distance[x]))
    newvelocityerrcalc = []
    for x in range(len(distance)):
        newvelocityerrcalc.append((popt2[0] * distanceerr[x]))
    for x in range(len(distance)):
        newvelocityerrcalc[x] = newvelocityerrcalc[x] + 147
    slope_err = np.sqrt(pcov2[0, 0])
    # intercept_err = np.sqrt(pcov2[1, 1])
    print('Hubble constant calculated from other_galaxies.dat and ngc4527 (km/s per Mpc):', popt2[0], '±', slope_err)
    # print(slope_err, intercept_err)
    plt.plot(distance, newvelocitycalc)
    plt.title('other_galaxies.dat + ngc4527')
    plt.ylabel('Velocity of Recession (km/s)')
    plt.xlabel('Distance of galaxy from Earth (Mpc)')
    plt.errorbar(distance, Recession, xerr = distanceerr, ls = 'none')
    plt.scatter(distance, Recession, marker = 'x')
    plt.show()
    # print(distanceerr)
    print('X^2:', (one.chi2(Recession, newvelocitycalc, newvelocityerrcalc)))
    print('X^2 reduced:', (one.chi2(Recession, newvelocitycalc, newvelocityerrcalc) / 7))
    # print(popt2[0])
    # print(one.chi2(Recession, newvelocitycalc, distanceerr))
    # n = 9
    # y = []
    # x = np.linspace(0, 10, 1000)
    # u = n/2 -1
    # for p in range(len(x)):
    #     y.append((2 ** (1-n/2)) * (x[p] ** (n-1)) * (np.e ** (-(x[p]**2)/2)) / (special.gamma(u)))
    # plt.plot(x, y)
    # plt.show()

    # chipart = (((Recession[5] - newvelocitycalc[5]) ** 2) / (newvelocitycalc[5]))
    # print(chipart / 7)

if __name__ == '__main__':
    '''if run as a script exec'''
    one = one()
    two = two()
    three = three()
    print('Part 1 results:')
    partone()
    print()
    print()
    print('Part 2 results:')
    parttwo()
    print()
    print()
    print('Part 3 results:')
    partthree()
