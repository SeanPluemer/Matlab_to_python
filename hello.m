%years = 30

%Hs_yrmax = rand(30)

%R = ​[5]; %returned years, does not work with 1 for 1st var, 5 years, 50 years
%the user inputs hs_max and the 1.01 and 5 and 50

%pex = 1./R;

%Hs_param = evfit(-1*Hs_yrmax);
%Hs_r = -1*evinv(pex,Hs_param(1),Hs_param(2)); %anual max hs 

%for evey year, there will be  1 returned data
 

years = 10;
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
    19] %this is the data
%Hs_yrmax = rand(years,1);
R = [2]; %this is the "next years"  Return year
 
pex = 1./R; %probability of each event 

[Hs_param] = evfit(-1*Hs_yrmax) %takes in max height and returns location parameter and scale
%returns maximum likelihood estimates of the parameters of the type 1 extreme value distribution given the sample data in data. 
% The sample data data must be a double-precision vector. 
% parmhat(1) is the location parameter µ, and parmhat(2) is the scale parameter σ.


Hs_r = -1*evinv(pex,Hs_param(1), Hs_param(2)) %takes in splits, location, and scale, returns the inverse cumulation function
%nverse cumulative distribution function




%once this is converted to python, make sub_rout

%1st script, pre process of input data 
%2nd part, computation (this part of script) 

%
