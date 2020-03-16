import numpy as np


def l_histo(RP):
    """
    Returns the histogram of diagonal line lengths of the recurrence plot 'RP'
    """
    N = RP.shape

    # preallocate storing vector for diagonal lines
    l_hist = np.zeros((N[0]))

    # first triangle of the RP
    # walk along the raws (upper triangle)
    for i in np.arange(1,N[0]+1): 
       cnt = 0
       for j in np.arange(0,N[1]-i):
            # are we on a rec. point? (walk along a diagonal)
            if RP[i+j,j]!=0:
                # count number of points on a diagonal line
                cnt += 1
            # line has ended
            else:
                # store line length
                if cnt!=0:
                    l_hist[cnt-1] +=1 
                # set back to zero for a new line 
                cnt = 0

       if cnt!=0: 
           l_hist[cnt-1] += 1


    # second triangle of the RP
    # walk along the columns (lower triangle)
    for j in np.arange(1,N[1]+1): 
       cnt = 0
       for i in np.arange(0,N[0]-j):
            # are we on a rec. point? (walk along a diagonal)
            if RP[i,j+i]!=0:
                # count number of points on a diagonal line
                cnt += 1
            # line has ended
            else:
                # store line length
                if cnt!=0:
                    l_hist[cnt-1] +=1 
                # set back to zero for a new line 
                cnt = 0

       if cnt!=0: 
           l_hist[cnt-1] += 1
            
    return l_hist

# set minimum line length parameter
l_min = 2;

# get the line length histogram
l_hist = l_histo(RP)

# determinism
num = np.sum(np.multiply(l_hist[l_min-1:N[0]],np.arange(l_min,N[0]+1)))
denom = np.sum(np.multiply(l_hist[0:N[0]],np.arange(1,N[0]+1)))
det =  num/denom 

# max diagonal line length
maxdl = np.max(np.nonzero(l_hist))+1

print(det)
print(maxdl)