#!/usr/bin/env python

"""main.py: This program is a conversion from matlab.
    its goal is to take in some waveform data, and output
    the inverse cumulative distribution function"""

"""What this does is basically take in x amount of years data.
Then it finds what the max wave height will be during the next n years"""
from evfit import evfit
from evinv import evinv
import test

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

    ste_gum,cdf = test.ste_block_maxima_Gumbel_with_evinv(Hs_yrmax,pex)
    print(ste_gum.kwds,cdf)
    helloasdf = test.evinv(pex, ste_gum.kwds['loc'], ste_gum.kwds['scale'])
    print(ste_gum.kwds, helloasdf)



if __name__ == "__main__":
    main()
