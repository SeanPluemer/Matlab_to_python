from evfit import evfit
from evinv import evinv

def main():
    years = 10
    Hs_yrmax = [
    16,
    15,
    17,
    19,
    16,
    15,
    17,
    15,
    17,
    15,
    19,
    17,
    18,
    18,
    18,
    19,
    16,
    15,
    18,
    16,
    20,
    16,
    19,
    16,
    17,
    18,
    20,
    16,
    20,
    19]

    R = 10 #this is the "next years"  Return year
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
