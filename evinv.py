import  numpy as np
def evinv(p,mu = 0,sigma =1 ,pcov=0,alpha = 0.05):
    if(p>0 and p<1):
        q = np.log(-1* np.log(1 - p))
    else:
        #todo, logic here
        pass
    #todo, sigma(sigma <= 0) = NaN;

    try:
        x = sigma.dot(q) + mu

    except:
        print("stats:evinv:InputSizeMismatch")
        return 0



    return x