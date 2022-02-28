from evfit import evfit
from evinv import evinv

def main():
    years = 10
#    Hs_yrmax = [1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09]
    Hs_yrmax = [0.1576,
    0.9706,
    0.9572,
    0.4854,
    0.8003,
    0.1419,
    0.4218,
    0.9157,
    0.7922,
    0.9595]
    R = 5 #this is the "next years"  Return year
    pex = 1/R #probability of each event

    inverse_hs_yrmax = [element * -1 for element in Hs_yrmax]
    Hs_param = evfit(inverse_hs_yrmax)
    '''takes in max height and returns location parameter and scale
    returns maximum likelihood estimates of the parameters of the type 1 extreme value distribution given the sample data in data. 
    The sample data data must be a double-precision vector. 
    parmhat(1) is the location parameter µ, and parmhat(2) is the scale parameter σ.'''

    print(Hs_param)
    Hs_r = evinv(pex, Hs_param[0], Hs_param[1]) * -1
    '''
    takes in splits, location, and scale, returns the inverse cumulation function
    %nverse cumulative distribution function'''
    print(Hs_r)


if __name__ == "__main__":
    main()
